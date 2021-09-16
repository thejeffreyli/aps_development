import numpy as np
import h5py
import os

# import other programs
from imm_reader_with_plot import IMMReader8ID
from rigaku_reader import RigakuReader

def read_params(HDF5_FILE):
    # parameters: center x, center y, energy (kEv), detector distance, pixel size, detector shape

    # dict
    config = {}
    
    with h5py.File(HDF5_FILE, 'r') as f1:
        
        # parameters
        config['rows'] = np.squeeze(f1.get('/measurement/instrument/detector/x_dimension')[()])
        config['cols'] = np.squeeze(f1.get('/measurement/instrument/detector/y_dimension')[()])
        config['pixels'] = config['rows']*config['cols']
        config['beam_center_x'] = np.squeeze(f1.get('/measurement/instrument/acquisition/beam_center_x')[()])
        config['beam_center_y'] = np.squeeze(f1.get('/measurement/instrument/acquisition/beam_center_y')[()])
        config['detector_distance'] = np.squeeze(f1.get('/measurement/instrument/detector/distance')[()])
        config['pixel_size'] = np.squeeze(f1.get('/measurement/instrument/detector/x_pixel_size')[()])
        config['x_energy']  = np.squeeze(f1.get('/measurement/instrument/source_begin/energy')[()])
        
        print(config)
    return config


def file_search_plot(file, config):
    # seeks directory of existing hdf program
    dir_path = os.path.dirname(os.path.realpath(file))
    for root, dirs, files in os.walk(dir_path):
        for file in files: 
            
            # seeks .imm file
            if file.endswith('.imm'):
                print("-----------.imm found.-----------")
                imm_file = root+'/'+str(file)
                reader = IMMReader8ID(imm_file)
                # reader.__load__()
                pixel_avg = reader.calc_avg_pixel()
                reader.plot_pix_avg(pixel_avg, config)
                
            # seeks .bin file
            elif file.endswith('.bin'):
                print("-----------.bin found.-----------")
                bin_file = root+'/'+str(file)                
                reader = RigakuReader(bin_file)
                img_2D = reader.load()
                reader.test_plot(img_2D, config)

    return None

if __name__ == "__main__":
    
    # input HDF file
    
    # imm
    # HDF5_FILE = "/Users/jeffr/Desktop/H432_OH_100_025C_att05_001/H432_OH_100_025C_att05_001_0001-1000.hdf"
    # bin    
    HDF5_FILE = '/Users/jeffr/Desktop/sheyfer202106/sheyfer202106/A004_D100_att0_25C_Rq0_00005/A004_D100_att0_25C_Rq0_00005_0001-100000.hdf'    
    print("Check if hdf5 file exists:", os.path.isfile(HDF5_FILE))


    config = read_params(HDF5_FILE)
    file_search_plot(HDF5_FILE, config)

    
