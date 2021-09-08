import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.axes_grid1.axes_grid import ImageGrid

x,y = np.ogrid[-4:4:31j,-4:4:31j]
z = 120000*np.exp(-x**2-y**2)

fig = plt.figure()
grid = ImageGrid(fig, 111,  # similar to subplot(141)
                     nrows_ncols=(2, 1),
                     axes_pad=0.05,
                     label_mode='L',
                     cbar_location='right',
                     cbar_mode='each'
                     )

im0 = grid.axes_all[0].imshow(z)
im1 = grid.axes_all[1].imshow(z, norm = LogNorm(z.min(), z.max()))

cb0 = grid.cbar_axes[0].colorbar(im0)
cb1 = grid.cbar_axes[1].colorbar(im1)

plt.show()