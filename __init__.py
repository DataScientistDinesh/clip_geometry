# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ClipWithGeometry
                                 A QGIS plugin
 The plugin clips and gives updated geometry columns
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-03-26
        copyright            : (C) 2023 by Dinesh Kumar
        email                : dineshkumardeekey@gmail.com
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
    """Load ClipWithGeometry class from file ClipWithGeometry.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .clip_geometry import ClipWithGeometry
    return ClipWithGeometry(iface)
