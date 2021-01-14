
# Special Topic in Remote Sensing
![itu logo](itulogo.png)
## *Analysis of Burned Area with Remote Sensing : Çanakkale Forest Fire 2020*
``` Python
-#number of raster rows
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
```
