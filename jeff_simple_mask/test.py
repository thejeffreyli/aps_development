import numpy as np
import h5py
import os 
import matplotlib.pyplot as plt


        
def test(file):
    with h5py.File(file, 'r') as hf:
        # print(hf['lambda_pre_mask'])
        test = np.squeeze(hf.get('/lambda_pre_mask')[()])  
        test = np.rot90(test, 3)
        test = np.flip(test, 1)
        # print(test)
        # test = test.flatten()

        # fig, ax = plt.subplots(1, 1, figsize=(15, 10))
        # im = ax.imshow(test, cmap='jet')
        
        # plt.imshow(test, cmap='jet')
        
        return test
    
def mask(file):
    with h5py.File(file, 'r') as hf:
        # print(hf['/data/dynamicMap'])
        test = np.squeeze(hf.get('/data/mask')[()])  
        # test = np.rot90(test, 3)
        # test = np.flip(test, 1)
        # print(test)
        # test = test.flatten()

        # fig, ax = plt.subplots(1, 1, figsize=(15, 10))
        # im = ax.imshow(test, cmap='jet')
        
        # plt.imshow(test, cmap='jet')
        
        return test

if __name__ == '__main__':
    # file = '/Users\jeffr\Desktop\suli_fall_2021\data\H432_OH_100_025C_att05_001/H432_OH_100_025C_att05_001_0001-1000.hdf' #IMM
    # file = '/Users/jeffr/Desktop/suli_fall_2021/data/sheyfer202106/sheyfer202106/A004_D100_att0_25C_Rq0_00001/A004_D100_att0_25C_Rq0_00001_0001-100000.hdf'    #RIGAKU
    # file = '/Users\jeffr\Desktop\suli_fall_2021\data\yuyin202109\D093_Lut_20C_att02_Lq0_001/D093_Lut_20C_att02_Lq0_001_1001-1000.hdf'# H5 RAW
    # file = '/Users\jeffr\Desktop\suli_fall_2021\Week_06/Lambda750k.tiff'
    file1 = '/Users\jeffr\Desktop\suli_fall_2021\Week_06/Blemish_Th5p5keV.h5'
    file1 = test(file1)


    file2 = '/Users\jeffr\Desktop\data\H432_OH_100_025C_att05_001/jaeger202106_Lq0_S360_D36.h5'
    file2 = mask(file2)    
    
    # res = np.logical_and(file1, file2)
    # res = np.logical_xor(file1, file2) 
    res = np.logical_or(file1, file2)
    plt.imshow(res)
    