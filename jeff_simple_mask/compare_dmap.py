import numpy as np
import h5py
import os 
import matplotlib.pyplot as plt


        
def test_01(file):
    with h5py.File(file, 'r') as hf:
        # print(hf['lambda_pre_mask'])
        test = np.squeeze(hf.get('/data/dynamicMap')[()])  
        test = np.flip(test)
        # test = np.rot90(test, 3)     
        
        return test

def test_02(file):
    with h5py.File(file, 'r') as hf:
        # print(hf['lambda_pre_mask'])
        test = np.squeeze(hf.get('/data/dynamicMap')[()])  

        
        return test    
    
if __name__ == '__main__':
    
    
    file1 = '/Users/jeffr\Desktop/data/triangle_mask/jeffrey_GUI_test.h5'
    file1 = test_01(file1)

    # generated
    file2 = '/Users/jeffr\Desktop/data/triangle_mask/H432_OH_100_025C_att05_001_0001-1000_triangle.h5'
    file2 = test_02(file2)    
    
    mat = file2 - file1
    
    print(mat)
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    # plt.imshow(file1)
    im = ax.imshow(mat)
    fig.colorbar(im, ax=ax)
    
    
    # mat = np.matrix(mat)
    # with open('outfile.txt','wb') as f:
    #     for line in mat:
    #         np.savetxt(f, line, fmt='%.2f')