# DEM Raster to 3D Plot
This plugin can visualize a digital elevation model (DEM) raster file as a 3D flying carpet to better understand landscape, using PyQGIS and Matplotlib. 

You can run the script in two ways:  
1. As a QGIS 2.X Plugin  
2. As a standalone code in the QGIS Python Console  

<img src="/cube.gif?raw=true" width="500px">

******************************************
## Instructions for running as a QGIS Plugin: 

1. Clone or download this repository and place items in a folder, e.g. "DEM-Raster-to-3D-Plugin"

1. Copy folder to your QGIS plugin directory, on Windows this is typically:   

C:\Users\yourusername\\.qgis2\python\plugins  

2. Open QGIS and enable the tool from Plugins>Manage and Install Plugins> ☑ "DEM Raster to 3D Plot"   

3. Run the tool from the toolbar (DEM icon) and follow instructions on interface.   

**************************************
## Instructions as a standalone code in QGIS Python Console

Simply open the **DEMRasterPyConsole.py**	file in the root directory in the [QGIS Python Console](https://docs.qgis.org/2.18/en/docs/user_manual/plugins/python_console.html), and change the input path to the raster file (keep in mind file size!) and run the code
