import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import pandas as pd

# converts csv to np array
def file_to_numpy(filename):
    df = pd.read_csv(filename, header=None)
    return df.to_numpy()


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


def find_com(X, Y, Z):
    sum_mass_X, sum_mass_Y, sum_mass  = 0, 0, 0

    for i in range(0, X):
        for j in range(0, Y):
            sum_mass_X = sum_mass_X + (i * Z[j,i])
            sum_mass_Y = sum_mass_Y + (j * Z[j,i])
            sum_mass = sum_mass + Z[j,i]
            
    return sum_mass_X, sum_mass_Y, sum_mass

            

file_data = open('data.csv')    
Z = file_to_numpy(file_data)

print(Z.shape)
Z = 1-Z

plot_fig(Z)

print(len(Z)) # Y = 91
Y = len(Z)

print(len(Z[0])) #X = 81
X = len(Z[0])

sum_mass_X, sum_mass_Y, sum_mass = find_com(X, Y, Z)
print(sum_mass_X, sum_mass_Y, sum_mass)

x_com = sum_mass_X/sum_mass
y_com = sum_mass_Y/sum_mass

print(x_com,y_com )






'''
295808.13535273884
332663.13535274006
968.1353527387722
'''