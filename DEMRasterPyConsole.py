import gdal, ogr, os , osr
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

##Open Raster
in_path = os.path.join ("C:\\Users\\ngavish\\Data\\DEM_100meter.tif")
test = gdal.Open(in_path)
gt = test.GetGeoTransform()

#Read data from raster as numpy
dem=test.ReadAsArray()

#Get cell size
col = test.RasterXSize
row = test.RasterYSize

# col, row to x, y
x = (col * gt[1]) + gt[0]
y = (row * gt[5]) + gt[3]
xres = gt[1]
yres = gt[5]
X = np.arange(gt[0], gt[0] + dem.shape[1]*xres, xres)
Y = np.arange(gt[3], gt[3] + dem.shape[0]*yres, yres)

# creation of a simple grid without interpolation
X, Y = np.meshgrid(X, Y)

# plot the raster
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
surf = ax.plot_surface(X, Y, dem, rstride=1, cstride=1, cmap=cm.terrain,linewidth=0, antialiased=False)

plt.show()

##Animate image 
#for angle in range(0, 360):
#    ax.view_init(30, angle)
#    plt.draw()
#    plt.pause(.001)