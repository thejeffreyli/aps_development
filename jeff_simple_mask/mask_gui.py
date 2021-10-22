from PyQt5 import QtCore
from simple_mask_ui import Ui_MainWindow as Ui
from simple_mask_kernel import SimpleMask
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pyqtgraph as pg
from matplotlib.backend_bases import KeyEvent

import os
import numpy as np
import sys
import json
import shutil
import logging

import h5py


home_dir = os.path.join(os.path.expanduser('~'), '.simple-mask')
if not os.path.isdir(home_dir):
    os.mkdir(home_dir)
log_filename = os.path.join(home_dir, 'viewer.log')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-24s: %(message)s',
                    handlers=[
                        logging.FileHandler(log_filename, mode='a'),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger(__name__)


def exception_hook(exc_type, exc_value, exc_traceback):
    logger.error("Uncaught exception",
                 exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = exception_hook


class SimpleMaskGUI(QtWidgets.QMainWindow, Ui):
    def __init__(self, path=None):
        

        super(SimpleMaskGUI, self).__init__()
        
        self.setupUi(self)

        # more setup; buttons
        self.btn_load.clicked.connect(self.load) # <------------------------------load
        self.btn_add_roi.clicked.connect(self.add_roi) # <------------------------------add roi
        self.btn_apply_roi.clicked.connect(self.apply_roi) # <------------------------------apply roi
        self.btn_plot.clicked.connect(self.plot)
        self.btn_editlock.clicked.connect(self.editlock)
        self.btn_compute_qpartition.clicked.connect(self.compute_partition) #<------------------------------compute partition
        
        # need a function for save button -- simple_mask_ui
        self.pushButton.clicked.connect(self.save_mask) # <------------------------------save mask
        # self.test_button.clicked.connect(self.test)


        self.plot_index.currentIndexChanged.connect(self.mp1.setCurrentIndex)
        

        # simple mask kernel
        self.sm = SimpleMask(self.mp1, self.infobar)
        self.mp1.sigTimeChanged.connect(self.update_index)

        self.state = 'lock'

        # ------------
        
        # first we see the blemish when the program is started up
        blemish = self.preload_blemish()  
        self.sm.test_plot(blemish)     # <-----------------------------------------------------------------------   PLOT


        self.show()

    def update_index(self):
        idx = self.mp1.currentIndex
        self.plot_index.setCurrentIndex(idx)

    def editlock(self):
        pvs = (self.db_cenx, self.db_ceny, self.db_energy, self.db_pix_dim,
               self.db_det_dist)

        if self.state == 'lock':
            self.state = 'edit'
            for pv in pvs:
                pv.setEnabled(True)
        elif self.state == 'edit':
            self.state = 'lock'
            values = []
            for pv in pvs:
                pv.setDisabled(True)
                values.append(pv.value())

            # update value
            self.sm.update_parameters(values)

        self.groupBox.repaint()
        self.plot()

    # starting function
    def load(self):
        fname = QFileDialog.getOpenFileName(self, 'Open directory')[0]
        # fname = "/Users/mqichu/Documents/local_dev/xpcs_mask/data/H187_D100_att0_Rq0_00001_0001-100000.hdf"
        self.fname.setText(os.path.basename(fname))

        # read data file
        self.sm.read_data(fname)

        # actual plotting <--------------------------------------------------------------
        self.db_cenx.setValue(self.sm.center[1])
        self.db_ceny.setValue(self.sm.center[0])
        self.db_energy.setValue(self.sm.energy)
        self.db_pix_dim.setValue(self.sm.pix_dim)
        self.db_det_dist.setValue(self.sm.det_dist)
        self.le_shape.setText(str(self.sm.shape[1:]))
        self.groupBox.repaint()
        self.plot() #<---------------------------------------------------------------------

        # generate qmap
        self.sm.generate_qmap_template(fname)
        self.sm.preload_meta(fname)
        
        # self.sm.test_func(fname, mask)        
        # self.write_qmap(fname)


    def plot(self):
        kwargs = {
            'cmap': self.plot_cmap.currentText(),
            'log': self.plot_log.isChecked(),
            'invert': self.plot_invert.isChecked(),
            'rotate': self.plot_rotate.isChecked(),
            'plot_center': self.plot_center.isChecked(),
        }
        self.sm.show_saxs(**kwargs) #<---------------------------------------------------
        # self.plot_index.setCurrentIndex(0)

    # def add_roi(self):
    #     color = ('g', 'y', 'b', 'r', 'c', 'm', 'k', 'w')[
    #             self.cb_selector_color.currentIndex()]
    #     kwargs = {
    #         'color': color,
    #         'sl_type': self.cb_selector_type.currentText(),
    #         'sl_mode': self.cb_selector_mode.currentText(),
    #         'width': self.plot_width.value()
    #     }
    #     self.sm.add_roi(**kwargs)
    #     return

    # def apply_roi(self):
    #     self.sm.apply_roi()
    #     # self.plot_index.setCurrentIndex(2)
    #     return 



    # predetermined mask

    def add_roi(self):
        print("PASS 2")
        triangle = self.preload_triangle()  
        self.sm.test_plot(triangle)
        
        return triangle     
        
    
    def apply_roi(self):
        
        blemish = self.preload_blemish() 
        triangle = self.preload_triangle()  
        
        mask = blemish * triangle # overall mask
        # self.test_output("test", mask)
        self.sm.test_plot(mask)
        
        return mask

    def compute_partition(self):
        
        mask = self.apply_roi()
        # self.test_output("test", mask)
        
        print(self.sb_sqnum)
        
        kwargs = {
            'sq_num': self.sb_sqnum.value(),
            'dq_num': self.sb_dqnum.value(),
            'sp_num': self.sb_spnum.value(),
            'dp_num': self.sb_dpnum.value(),
        }
        res = self.sm.compute_partition(mask, **kwargs)
                
        dmap = res['dynamicMap'] #<------------------------------------------------dmap
        smap = res['staticMap'] #<------------------------------------------------smap
        
        # self.test_output("test", dmap)

        
        # dmap = np.multiply(dmap, mask)    #<------------------------------------------------operation
        # dmap = dmap.astype(int)
        # res['dynamicMap'] = dmap

        # smap = np.multiply(smap, mask)    #<------------------------------------------------operation
        # smap = smap.astype(int)
        # res['staticMap'] = smap

        # plotting new map
        new_map = smap * dmap 
        # self.sm.test_plot(new_map)
        
        self.plot_index.setCurrentIndex(3) #<----?
        self.sm.update_compute_partition(res)

    # save button 
    def save_mask(self):
        # mask = self.sm.apply_roi()
        # self.test_output("test", mask)
        blemish = self.preload_blemish() 
        triangle = self.preload_triangle()  
        
        mask = blemish * triangle # overall mask
        
        self.sm.update_mask(mask)
    
    
    def preload_blemish(self):
        print("PASS 1")
        file = '/Users/jeffr/Desktop/data/blemish/Blemish_Th5p5keV.h5'
        with h5py.File(file, 'r') as hf:
            blemish = np.squeeze(hf.get('/lambda_pre_mask')[()])  
            blemish = np.rot90(blemish, 3)
            blemish = np.flip(blemish, 1)
        hf.close()  
        return blemish    


    def preload_triangle(self):
        file = '/Users/jeffr\Desktop/data/triangle_mask/mask_lambda_test.h5'
        with h5py.File(file, 'r') as hf:
            test = np.squeeze(hf.get('/mask_triangular')[()])  
            test = np.rot90(test, 3)
            test = np.flip(test, 1)
        hf.close()             
        return test
    





    # def test_output(self, name, triangle_mask):
    
    #     hf = h5py.File(name +'.h5', 'w')
        
    #     # empty
    #     empty_arr = np.array([])
        
    #     # defining directories
    #     data = hf.create_group("data")
    #     data.create_dataset('mask', data=triangle_mask) 
    
    #     hf.close()




    
    # def test(self):
    #     print("PASSSSSS")
        
def run():
    # if os.name == 'nt':
    #     setup_windows_icon()
    # QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    app = QtWidgets.QApplication(sys.argv)
    window = SimpleMaskGUI()
    app.exec_()
    # print("test")

if __name__ == '__main__':
    run()
