#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


import os
os.listdir()


# In[8]:


#import bands as separate 1 band raster
band4 = rasterio.open('yanginsonrasi_red.tif') #red
band8 = rasterio.open('yanginsonrasi_nir.tif') #nir


# In[15]:


#number of raster rows
band4.height
#number of raster columns
band4.width
#plot band 
plot.show(band4)
#type of raster byte
band4.dtypes[0]
#raster sytem of reference
band4.crs
#raster transform parameters
band4.transform
#raster values as matrix array
band4.read(1)
#multiple band representation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
plot.show(band4, ax=ax1, cmap='Blues') #red
plot.show(band8, ax=ax2, cmap='Blues') #nir
fig.tight_layout()
#generate nir and red objects as arrays in float64 format
red = band4.read(1).astype('float64')
nir = band8.read(1).astype('float64')

nir
#ndvi calculation, empty cells or nodata cells are reported as 0
ndvi=np.where(
    (nir+red)==0., 
    0, 
    (nir-red)/(nir+red))
ndvi[:5,:5]
#export ndvi image
ndviImage = rasterio.open('C:/Users/PC/mehves/ndviImage.tiff','w',driver='Gtiff',
                          width=band4.width, 
                          height = band4.height, 
                          count=1, crs=band4.crs, 
                          transform=band4.transform, 
                          dtype='float64')
ndviImage.write(ndvi,1)
ndviImage.close()
#plot ndvi
ndvi = rasterio.open('C:/Users/PC/mehves/ndviImage.tiff')
fig = plt.figure(figsize=(18,12))
plot.show(ndvi)


# In[12]:


#import bands as separate 1 band raster
bandonce4 = rasterio.open('Yangınöncesi_ReD.tif') #red
bandonce8 = rasterio.open('Yangınöncesi_NIR.tif') #nir


# In[17]:


#number of raster rows
bandonce4.height
#number of raster columns
bandonce4.width
#plot band 
plot.show(bandonce4)
#type of raster byte
bandonce4.dtypes[0]
#raster sytem of reference
bandonce4.crs
#raster transform parameters
bandonce4.transform
#raster values as matrix array
bandonce4.read(1)
#multiple band representation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
plot.show(bandonce4, ax=ax1, cmap='Blues') #red
plot.show(bandonce8, ax=ax2, cmap='Blues') #nir
fig.tight_layout()
#generate nir and red objects as arrays in float64 format
red = bandonce4.read(1).astype('float64')
nir = bandonce8.read(1).astype('float64')

nir
#ndvi calculation, empty cells or nodata cells are reported as 0
ndvi=np.where(
    (nir+red)==0., 
    0, 
    (nir-red)/(nir+red))
ndvi[:5,:5]
#export ndvi image
ndvionceImage = rasterio.open('C:/Users/PC/mehves/ndvionceImage.tiff','w',driver='Gtiff',
                          width=bandonce4.width, 
                          height = bandonce4.height, 
                          count=1, crs=bandonce4.crs, 
                          transform=bandonce4.transform, 
                          dtype='float64')
ndvionceImage.write(ndvi,1)
ndvionceImage.close()
#plot ndvi
ndvionce = rasterio.open('C:/Users/PC/mehves/ndvionceImage.tiff')
fig = plt.figure(figsize=(18,12))
plot.show(ndvionce)


# In[ ]:




