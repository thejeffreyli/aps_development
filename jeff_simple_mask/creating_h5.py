import numpy as np
import h5py

d1 = []
d2 = []

hf = h5py.File('data.h5', 'w')

hf.create_dataset('dataset_1', data=d1)
hf.create_dataset('dataset_2', data=d2)

hf.close()