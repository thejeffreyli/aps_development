import numpy as np
import scipy as sp
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt
import numpy as np


class RigakuReader():
    def __init__(self, file):
        self.file = file
    
    def load(self):
        with open(self.file, 'r') as f:
            a = np.fromfile(f, dtype=np.uint64)

            b = (a >> 5+11)
            pix_ind = (b & 2**21-1).astype(int)
            pix_count = (a & 2**12-1).astype(int)
            pix_frame = (a >> 64-24).astype(int)
            
            img = csr_matrix((pix_count, (pix_frame, pix_ind)), shape=(max(pix_frame)+1, 1024*512), dtype='float')
            
            
            img_2D = np.transpose(img.mean(axis=0).reshape(512,1024))
        return img_2D  




if __name__ == "__main__":


    file = 'C:/Users/jeffr/Desktop/sheyfer202106/sheyfer202106/A004_D100_att0_25C_Rq0_00001/A004_D100_att0_25C_Rq0_00001.bin'
    reader = RigakuReader(file)
    
    img_2D = reader.load()
    
    # Notes, img_2D is multidim array. Need to find way to select only certain values that 
    # fit range we want
    
    plt.contourf(img_2D, vmin=0, vmax=6*(10**(-8)))


    plt.imshow(img_2D)
    plt.colorbar()
    
