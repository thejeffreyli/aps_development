import h5py
import numpy as np
import argparse

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
    
    file1 = '/Users/jeffr/Desktop/data/E005_D100_Lq1_025C_att03_001/E005_D100_Lq1_025C_att03_001_0001-1000.hdf'
    x_guess = 780.6 # change to input parameters
    y_guess = 259.4
    
    pix2q = extract_pix2q(file1)
    
    file2 = '/Users/jeffr/Desktop/data/E005_D100_Lq1_025C_att03_001/E005_D100_Lq1_025C_att03_001_00001-01000.imm'
    img_2D = read_imm(file2)
    
    print(img_2D)
    
    # parameters for meshgrid                                                                 # <------------------------?
    pix_pos_x, pix_pos_y = np.meshgrid(len(img_2D[0]),len(img_2D))
    
    dim_x = 81 # change to input parameters
    dim_y = 91
    step_size = 0.1
    
    ROI_Dev = np.zeros((dim_x, dim_y))
    # print(ROI_Dev)

    x0 = np.zeros(dim_x)
    y0 = np.zeros(dim_y)

    
    for ii in range(dim_x):
        for jj in range(dim_y):        

            x0[ii] = x_guess + (ii-np.floor(dim_x/2))*step_size
            # print(x0[ii])
            y0[jj] = y_guess + (jj-np.floor(dim_y/2))*step_size
            # print(y0[jj])
            Q_map = np.sqrt((pix_pos_x-x0[ii])**2 + (pix_pos_y-y0[jj])**2)*pix2q
    
            # print(Q_map)
            # if Q_map>0.0065 & Q_map < 0.0075 :
            #     Int_ROI = img_2D[Q_map]
            #     print(Int_ROI)
            # else:
            #     Int_ROI = img_2D[0]
                
                
            # Int_ROI = img_2D(Q_map>0.0065 & Q_map<0.0075) # <------------------------? # put 0 if outside  conditions
            # ROI_Dev[ii][jj] = np.var(Int_ROI)/np.mean(Int_ROI)/np.mean(Int_ROI);
            
            
if __name__ == '__main__':
    main()