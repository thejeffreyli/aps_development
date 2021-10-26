Requirements:
os, numpy, PyQt5, h5py, matplotlib, scipy, pyqtgraph

HDFView application


Experimental data file: H432_OH_100_025C_att05_001 (imm)
H432_OH_100_025C_att05_001_0001-1000.HDF (meta data)
H432_OH_100_025C_att05_001_00001-01000.imm (raw data)
H432_OH_100_025C_att05_001_0001-1000.batchinfo

Blemish:
Blemish_Th5p5keV.h5



How to run GUI

1) Open mask_gui and run. python mask_gui.py
2) Load meta data and blemish. You should see the scattering on the plot.
3) Edit/lock to attain/display data from meta data file. 
4) Draw your Mask (roi). You can choose whatever shape or color for the mask, then click 'add roi.'You can move or adjust the shape on the plot.
5) Click 'add roi' after you have configured your shape.
6) Click 'compute' to compute partitions. The dynamic q partition and static q partition should show up on the plot. You can toggle the drop down bar below 'Scattering, Mask and Partitions.'
7) Save qmap file (.h5). Be sure to designate a directory when saving.


Note: The section File under Mask is for preloading masks. It is still a work in progress. 


