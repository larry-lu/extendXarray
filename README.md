# extendXarray
Provides higher level functionality to the Python xarray project by integrating methods from GDAL and OGR.

### Why? 

I was scrambling to prepare some results for AGU and having a hard time finding pre-packaged methods for rasterizing shapefiles against MODIS data arrays. This package aims to leverage GDAL/OGR vector processing tools to simplify geosciences research that requires vector/raster processing (e.g. shapefile masking, zonal statistics, regional weighting, etc.)

### Status

Project is in its infancy. Only one class so far. Simple but robust class for rastering shapefile against input `xarray.Dataset` objects with methods for outputting to several `xarray` data structures.

See the demo in the Jupyter Notebook:
[examples/class_GridVectors.ipynb](examples/class_GridVectors.ipynb)