import numpy as np
import h5py

d1 = np.random.random(size = (1000,20))
d2 = np.random.random(size = (1000,200))

print (d1.shape, d2.shape)


hf = h5py.File('test.h5', 'w')
dt = h5py.special_dtype(vlen=str)
dset = hf.create_dataset('vlen_str', (1,), dtype=dt)
dset[0] = 'the change of water into water vapour'

hf.close()


# In [27]: dt = h5py.special_dtype(vlen=str)

# In [28]: dset = h5File.create_dataset('vlen_str', (100,), dtype=dt)

# In [29]: dset[0] = 'the change of water into water vapour'

# In [30]: dset[0]
# Out[30]: 'the change of water into water vapour'