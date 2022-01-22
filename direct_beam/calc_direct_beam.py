import h5py
import numpy as np
import argparse
import pandas as pd 
import time

import matplotlib.pyplot as plt
import matplotlib.colors as colors

# import program
from imm_reader_with_plot import IMMReader8ID

def extract_pix2q(file):
    # blemish file if the fname is specified;
    with h5py.File(file, 'r') as hf:
        X_E = np.squeeze(hf.get('/measurement/instrument/source_begin/energy')[()])
        Det_Dist = np.squeeze(hf.get('/measurement/instrument/detector/distance')[()]) / 1000
        pix_size = np.squeeze(hf.get('/measurement/instrument/detector/x_pixel_size')[()]) * 1e-3       

        
    lam = 12.398/X_E;
    k0 = 2*np.pi/lam;
    pix2q = (pix_size/Det_Dist)*k0
    
    return pix2q

def read_imm(imm_file):
    reader = IMMReader8ID(imm_file)
    img_2D = reader.calc_avg_pixel()
    # check if 2d array
    # print( len(img_2D. shape))
    return img_2D

def plot_fig(ROI_Dev):
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    colormap = plt.cm.jet
    colormap.set_under(color='w')
    
    im = ax.imshow(ROI_Dev, 
                 cmap=colormap, 
                 norm=colors.LogNorm(vmin=np.min(ROI_Dev), vmax=np.max(ROI_Dev)),
                 interpolation='none')
    fig.colorbar(im, ax=ax)
    plt.rc('font', size=20)

    return ax

def main():
    
    ''' 
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()

    parser.add_argument("hdf_file",
                        help="filename for meta data (hdf)")
    parser.add_argument("imm_file",
                        help="filename for raw data (.imm)")
    
    parser.add_argument("x_guess",
                        help="value for x_guess")
    parser.add_argument("y_guess",
                        help="value for y_guess")
    parser.add_argument("dim_x",
                        help="value for dim_x")
    parser.add_argument("dim_y",
                        help="value for dim_y")    
    parser.add_argument("step_size",
                        help="value for step_size")

    args = parser.parse_args()
    # load the train and test data
    
    
    x_guess = args.x_guess
    y_guess = args.y_guess
    dim_x = args.dim_x
    dim_y = args.dim_y
    step_size = args.step_size    
    
    pix2q = extract_pix2q(args.hdf_file)
    img_2d = read_imm(args.imm_file)
    '''    
    #-----------------------------------------------------------------------------------
    t0 = time.time()
    print(t0)
    
    # hdf file
    file1 = '/Users/jeffr/Desktop/data/E005_D100_Lq1_025C_att03_001/E005_D100_Lq1_025C_att03_001_0001-1000.hdf'
    x_guess = 780.6 # change to input parameters
    y_guess = 259.4
    
    pix2q = extract_pix2q(file1)
    
    # IMM file    
    file2 = '/Users/jeffr/Desktop/data/E005_D100_Lq1_025C_att03_001/E005_D100_Lq1_025C_att03_001_00001-01000.imm'
    img_2D = read_imm(file2)
    
    # parameters for meshgrid                                                                 
    x = np.arange(0, len(img_2D[0]))
    y = np.arange(0, len(img_2D))    
                                                
    pix_pos_x, pix_pos_y = np.meshgrid(x,y)
    

    dim_x = 81 # change to input parameters
    dim_y = 91
    step_size = 0.11
    
    # row, col
    ROI_Dev = np.zeros((dim_y, dim_x))

    x0 = np.zeros(dim_x)    
    y0 = np.zeros(dim_y)


    for ii in range(dim_x):
        for jj in range(dim_y):        

            x0[ii] = x_guess + (ii-np.floor(dim_x/2))*step_size
            # x0[ii] = x_guess + (ii-(dim_x/2))*step_size
            # print(x0[ii])
            y0[jj] = y_guess + (jj-np.floor(dim_y/2))*step_size
            # y0[jj] = y_guess + (jj-(dim_y/2))*step_size
            # print(y0[jj])
            Q_map = np.sqrt((pix_pos_x-x0[ii])**2 + (pix_pos_y-y0[jj])**2)*pix2q
            
            # bool_arr = np.where((Q_map > 0.0060) & (Q_map < 0.0080), 1, 0)
            bool_arr = np.where((Q_map > 0.0067) & (Q_map < 0.0073), 1, 0)        
  
            # np.nonzero returns indices 
            nz = np.nonzero(bool_arr) # indices
            Int_ROI = img_2D[nz] # 1D array 
            
            ROI_Dev[jj][ii] = np.var(Int_ROI)/np.square(np.mean(Int_ROI)) # mean^2  # normalization

    # print(ROI_Dev)


    pd.DataFrame(ROI_Dev).to_csv("data.csv",header=False, index=False) # create plot


    plot_fig(ROI_Dev)
    
    # print(ROI_Dev.min())
    # print(np.min(ROI_Dev))

    # result = np.where(ROI_Dev == np.min(ROI_Dev))
    # print(result)
    
    
    t1 = time.time() # 148.85632467269897           
    total = t1-t0
    print(total)    
            
if __name__ == '__main__':
    main()