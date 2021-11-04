import h5py
import numpy as np
import argparse

# import program
from imm_reader_with_plot import IMMReader8ID




def read_data(file):
    # blemish file if the fname is specified;
    with h5py.File(file, 'r') as hf:
        blemish = np.squeeze(hf.get('/lambda_pre_mask')[()])
        blemish = np.rot90(blemish, 3)
        blemish = np.flip(blemish, 1)
    return blemish


def replace_blem(blemish, x_coord, y_coord, program):
    print(program)
    if program == "matlab":
        x_coord = x_coord - 1
        y_coord = y_coord - 1
    print(x_coord, y_coord)
    blemish[x_coord][y_coord] = 0
        
        
    return blemish


def write_data(file, blemish_new):
    with h5py.File(file, 'a') as hf:
        print("Saving directories...")               
        hf.create_dataset('lambda_pre_mask', data=blemish_new)


def main():
    file1 = '/Users/jeffr/Desktop/data/blemish/Blemish_Th5p5keV.h5'
    blemish = read_data(file1)

    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()

    parser.add_argument("x_coord",
                        help="int, blemish x coordinate")
    parser.add_argument("y_coord",
                        help="int, blemish y coordinate")
    parser.add_argument("program",
                        help="string, Python or Matlab")

    args = parser.parse_args()
    # load the train and test data
    
    
    x_coord = int(args.x_coord)
    y_coord = int(args.y_coord)
    program = args.program


    file2 = '/Users/jeffr/Desktop/data/blemish/test.h5'
    blemish_new = replace_blem(blemish, x_coord, y_coord, program)    

    # write_data(file2, blemish_new)


if __name__ == '__main__':
    main()