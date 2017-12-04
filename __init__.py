# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DEMRasterTo3D
                                 A QGIS plugin
 This plugin plots a given raster to a 3D Plot 'Flying Carpet'
                             -------------------
        begin                : 2017-08-13
        copyright            : (C) 2017 by Nimrod Gavish
        email                : gavishnimrod@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DEMRasterTo3D class from file DEMRasterTo3D.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .DEMRaster_3D import DEMRasterTo3D
    return DEMRasterTo3D(iface)
