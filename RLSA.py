from __future__ import print_function
from skimage import io, exposure,util
import matplotlib.pyplot as plt
import numpy as np




scanned_page = io.imread('im2.jpg')
# plt.figure(figsize=(10,10))
scanned_page_bw = util.img_as_bool(scanned_page[:,:,0])
# io.imshow(scanned_page_bw)


print('scanned page shape', scanned_page_bw.shape)
horizontal_RLSA = np.sum(scanned_page_bw, axis=1)
h_shape  = horizontal_RLSA.shape

ax = np.linspace(0, h_shape[0], h_shape[0], dtype = 'uint16' )

# plt.figure
# plt.plot(ax,horizontal_RLSA)


plt.figure(figsize=(10,3))
scanned_page = (scanned_page_bw[910:1000,:])
# io.imshow(scanned_page)
vertical_RLSA = np.sum(scanned_page, axis=0)
v_shape = vertical_RLSA.shape
bx = np.linspace(0, h_shape[0], h_shape[0], dtype = 'uint16' )

plt.plot(bx,vertical_RLSA)
#plt.figure(figsize=(5,3))
#plt.subplot(1,2,1)
#io.imshow(util.invert(scanned_page_bw[60:90,175:195]))
#plt.subplot(1,2,2)
#io.imshow(morphology.convex_hull_image(util.invert(scanned_page_bw[60:90,175:195])))

plt.show()