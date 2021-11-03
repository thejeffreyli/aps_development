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


def extract_triangle(file):
    with h5py.File(file, 'r') as hf:
        test = np.squeeze(hf.get('/mask_triangular')[()])  
        test = np.rot90(test, 3)
        test = np.flip(test, 1)
    hf.close()
    return test
    
def extract_blemish(file):
    with h5py.File(file, 'r') as hf:
        test = np.squeeze(hf.get('/lambda_pre_mask')[()])  
        test = np.rot90(test, 3)
        test = np.flip(test, 1)    
    hf.close()
    return test    
    
def generate_qmap_template(name, triangle_mask):

    hf = h5py.File(name +'.h5', 'w')
    
    # empty
    empty_arr = np.array([])
    
    # defining directories
    data = hf.create_group("data")
    data.create_dataset('mask', data=triangle_mask) 

    hf.close()


def compute_partition(self):
    
    mask = self.apply_roi()
    self.test_output("test", mask)
    
    
    kwargs = {
        'sq_num': self.sb_sqnum.value(),
        'dq_num': self.sb_dqnum.value(),
        'sp_num': self.sb_spnum.value(),
        'dp_num': self.sb_dpnum.value(),
    }
    res = self.sm.compute_partition(mask, **kwargs)
            
    dmap = res['dynamicMap'] #<------------------------------------------------dmap
    smap = res['staticMap'] #<------------------------------------------------smap

    new_map = smap * dmap 
    # self.sm.test_plot(new_map)
    
    self.plot_index.setCurrentIndex(3) #<----?
    self.sm.update_compute_partition(res)

def compute_partition(self, mask, dq_num=10, sq_num=100, mode='linear',
                          dp_num=36, sp_num=360):

        # print(mask)
        if sq_num % dq_num != 0:
            raise ValueError('sq_num must be multiple of dq_num')

        if sp_num % dp_num != 0:
            raise ValueError('sq_num must be multiple of dq_num')

        qmap = self.qmap['qr'] * mask
        
        # print(qmap)
        qmap_valid = qmap[self.mask == True]

        qmin = np.min(qmap_valid)
        qmax = np.max(qmap_valid)

        if mode == 'linear':
            dqlist = np.linspace(qmin, qmax, dq_num + 1)
            sqlist = np.linspace(qmin, qmax, sq_num + 1)
            dphi = np.linspace(0, np.pi * 2.0, dp_num + 1)
            sphi = np.linspace(0, np.pi * 2.0, sp_num + 1)
            
        dqmap_partition = np.zeros_like(qmap, dtype=np.uint32)
        sqmap_partition = np.zeros_like(qmap, dtype=np.uint32)




        # dqval
        dqval_list = []
        for n in range(dq_num):
            qval = dqlist[n]
            dqmap_partition[qmap * self.mask >= qval] = n + 1
            dqval_list.append(qval)

        # sqval 
        sqval_list = []
        for n in range(sq_num):
            qval = sqlist[n]
            sqmap_partition[qmap * self.mask >= qval] = n + 1
            sqval_list.append(qval)

        dphi_partition = np.zeros_like(qmap, dtype=np.uint32)
        sphi_partition = np.zeros_like(qmap, dtype=np.uint32)

        for n in range(dp_num):
            dphi_partition[self.qmap['phi'] >= dphi[n]] = n
        dphival = np.unique(dphi_partition)
        
        # print(np.unique(dphi_partition).sort())    
        for n in range(sp_num):
            sphi_partition[self.qmap['phi'] >= sphi[n]] = n
        sphival = np.unique(sphi_partition)


        # print(sphi_partition)
        dyn_combined = np.zeros_like(dqmap_partition, dtype=np.uint32)
        sta_combined = np.zeros_like(dqmap_partition, dtype=np.uint32)

        # dqmap, dqlist
        for n in range(dp_num):
            idx = dphi_partition == n
            dyn_combined[idx] = dqmap_partition[idx] + n * dq_num
        dqlist =  np.unique(dqmap_partition, axis=1)
        

        # sqmap, sqlist
        for n in range(sp_num):
            idx = sphi_partition == n
            sta_combined[idx] = sqmap_partition[idx] + n * sq_num
        sqlist =  np.unique(sqmap_partition, axis=1)
        

        "NOTE: REMOVED THIS PORTION BECAUSE OF BUG ISSUES -----------------------"
        # self.data[3] = dyn_combined * self.mask
        # self.data[4] = sta_combined * self.mask
        # self.hdl.setImage(self.data)
        # self.hdl.setCurrentIndex(3)
        

        res = {
            'dqval': dqval_list,
            'sqval': sqval_list,
            'dynamicMap': dqmap_partition,
            'dynamicQList': dqlist,
            'staticMap': sqmap_partition,
            'staticQList': sqlist,
            'dphival': dphival,
            'sphival': sphival
        }        
        

        return res
    
if __name__ == '__main__':

    triangle_mask = '/Users/jeffr\Desktop/data/triangle_mask/mask_lambda_test.h5'
    triangle_mask = extract_triangle(triangle_mask)
    
    blemish = '/Users/jeffr\Desktop/data/blemish/Blemish_Th5p5keV.h5'
    blemish = extract_blemish(blemish)  

    triangle_mask = np.multiply(blemish, triangle_mask)



    # generate_qmap_template("dmap", triangle_mask)    
    
    