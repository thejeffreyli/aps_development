import h5py
import numpy as np

"""
read blemish file
change given array locations to 0
write into hdf
"""


def read_data(file):
    # blemish file if the fname is specified;
    with h5py.File(file, 'r') as hf:
        blemish = np.squeeze(hf.get('/lambda_pre_mask')[()])
        blemish = np.rot90(blemish, 3)
        blemish = np.flip(blemish, 1)

    # print(type(blemish))
    return blemish

def write_data(file, blemish_new):
    with h5py.File(file, 'a') as hf:
        print("Saving directories...")               
        hf.create_dataset('lambda_pre_mask', data=blemish_new)

def replace_blem(blemish, x_list, y_list):
    for i in range(len(x_list)):
        blemish[x_list[i]][y_list[i]] = 0
        # print(blemish[x_list[i]][y_list[i]])
        
    return blemish
    


def read_txt(file):
    x_list = []
    y_list = []
    with open(file) as f:
        for line in f:
            x, y = line.strip().split(",")
            x_list.append(int(x) + 1)
            y_list.append(int(y) + 1)
    return x_list, y_list
    
def main():
    file1 = '/Users/jeffr/Desktop/data/blemish/Blemish_Th5p5keV.h5'
    blemish = read_data(file1)
    
    
    txtfile = '/Users/jeffr/Desktop/data/blemish/blemish_imm_750k.txt'
    x_list, y_list = read_txt(txtfile)
    
    
    file2 = '/Users/jeffr/Desktop/data/blemish/test.h5'
    blemish_new = replace_blem(blemish, x_list, y_list)    

    write_data(file2, blemish_new)

if __name__ == '__main__':
    main()


    

    

