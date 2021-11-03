import numpy as np
import h5py
import os 
import matplotlib.pyplot as plt


        
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


if __name__ == '__main__':

    triangle_mask = '/Users/jeffr\Desktop/data/triangle_mask/mask_lambda_test.h5'
    triangle_mask = extract_triangle(triangle_mask)
    
    blemish = '/Users/jeffr\Desktop/data/blemish/Blemish_Th5p5keV.h5'
    blemish = extract_blemish(blemish)  

    triangle_mask = np.multiply(blemish, triangle_mask)



    generate_qmap_template("test", triangle_mask)
        