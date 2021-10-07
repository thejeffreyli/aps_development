import numpy as np
import h5py
import os 
import matplotlib.pyplot as plt


        

if __name__ == '__main__':
    # file = '/Users\jeffr\Desktop\suli_fall_2021\data\H432_OH_100_025C_att05_001/H432_OH_100_025C_att05_001_0001-1000.hdf' #IMM
    # file = '/Users/jeffr/Desktop/suli_fall_2021/data/sheyfer202106/sheyfer202106/A004_D100_att0_25C_Rq0_00001/A004_D100_att0_25C_Rq0_00001_0001-100000.hdf'    #RIGAKU
    # file = '/Users\jeffr\Desktop\suli_fall_2021\data\yuyin202109\D093_Lut_20C_att02_Lq0_001/D093_Lut_20C_att02_Lq0_001_1001-1000.hdf'# H5 RAW
    file = '/Users\jeffr\Desktop\suli_fall_2021\Week_06/Lambda750k.tiff'

    # file = '/Users\jeffr\Desktop\suli_fall_2021\jeff_simple_mask'
    I = plt.imread(file)
    
    # print(len(I))
    
    rows = len(I)

    print(rows)
    columns = len(I[0])
    print(columns)
    total_length = rows * columns

    plt.imshow(I)
    print(total_length)