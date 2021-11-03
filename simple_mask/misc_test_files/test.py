import numpy as np
import h5py
import os 
import matplotlib.pyplot as plt


        
def extract_triangle(file):
    with h5py.File(file, 'r') as hf:
        test = np.squeeze(hf.get('/mask_triangular')[()])  
        test = np.rot90(test, 3)
        test = np.flip(test, 1)
        return test
    
def extract_blemish(file):
    with h5py.File(file, 'r') as hf:
        test = np.squeeze(hf.get('/lambda_pre_mask')[()])  
        test = np.rot90(test, 3)
        test = np.flip(test, 1)    

        return test

def extract_dmap(file):
    with h5py.File(file, 'r') as hf:
        test = np.squeeze(hf.get('/data/dynamicMap')[()])  
        
        return test
    
def extract_smap(file):
    with h5py.File(file, 'r') as hf:
        test = np.squeeze(hf.get('/data/staticMap')[()])  
        
        return test    



if __name__ == '__main__':
    # file = '/Users\jeffr\Desktop\suli_fall_2021\data\H432_OH_100_025C_att05_001/H432_OH_100_025C_att05_001_0001-1000.hdf' #IMM
    # file = '/Users/jeffr/Desktop/suli_fall_2021/data/sheyfer202106/sheyfer202106/A004_D100_att0_25C_Rq0_00001/A004_D100_att0_25C_Rq0_00001_0001-100000.hdf'    #RIGAKU
    # file = '/Users\jeffr\Desktop\suli_fall_2021\data\yuyin202109\D093_Lut_20C_att02_Lq0_001/D093_Lut_20C_att02_Lq0_001_1001-1000.hdf'# H5 RAW
    # file = '/Users\jeffr\Desktop\suli_fall_2021\Week_06/Lambda750k.tiff'
    triangle_mask = '/Users/jeffr\Desktop/data/triangle_mask/mask_lambda_test.h5'
    triangle_mask = extract_triangle(triangle_mask)

    # file2 =  '/Users\jeffr\Desktop\suli_fall_2021\results\H432_OH_100_025C_att05_001_0001-1000_v5.h5'
    blemish = '/Users/jeffr\Desktop/data/blemish/Blemish_Th5p5keV.h5'
    blemish = extract_blemish(blemish)    
        
    
    file =  '/Users/jeffr/Desktop/suli_fall_2021/results/H432_OH_100_025C_att05_001_0001-1000_v9.h5'
    dmap = extract_dmap(file)      
    smap = extract_smap(file)
    
    # dmap = (blemish)*dmap
    # smap = blemish *smap
    
    # plt.imshow(smap) 
    
    
    #compare
    file_comp = '/Users/jeffr/Desktop/data/triangle_mask/jeffrey_GUI_test.h5'
    comp_dmap = extract_dmap(file_comp)
    comp_smap = extract_smap(file_comp)
    
    
    mat = np.abs(comp_dmap - dmap)
    
    # print(res)
    
    # with h5py.File(file, 'a') as hf:
    #     print("Saving directories...")               
    #     # if directory exists, directories need to be updated
    #     data = hf['data']  
    #     data['dynamicMap'][...] = dmap
    #     data['staticMap'][...] = smap

    # hf.close()
    
    print(mat)
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    im = ax.imshow(mat, vmin=0, vmax=10)
    fig.colorbar(im, ax=ax)
        

    # plt.colorbar()
    
    # print(res)
    