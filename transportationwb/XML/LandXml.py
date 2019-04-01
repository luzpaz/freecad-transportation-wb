# -*- coding: utf-8 -*-
# **************************************************************************
# *                                                                        *
# *  Copyright (c) 20XX Joel Graff <monograff76@gmail.com>                         *
# *                                                                        *
# *  This program is free software; you can redistribute it and/or modify  *
# *  it under the terms of the GNU Lesser General Public License (LGPL)    *
# *  as published by the Free Software Foundation; either version 2 of     *
# *  the License, or (at your option) any later version.                   *
# *  for detail see the LICENCE text file.                                 *
# *                                                                        *
# *  This program is distributed in the hope that it will be useful,       *
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *  GNU Library General Public License for more details.                  *
# *                                                                        *
# *  You should have received a copy of the GNU Library General Public     *
# *  License along with this program; if not, write to the Free Software   *
# *  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *  USA                                                                   *
# *                                                                        *
# **************************************************************************

'''
Importer for LandXML files
'''

from shutil import copyfile
from xml.etree import ElementTree as etree

import FreeCAD as App

from transportationwb.ScriptedObjectSupport import Units, Utils

XML_VERSION = 'v1.2'
XML_NAMESPACE = {XML_VERSION: 'http://www.landxml.org/schema/LandXML-1.2'}

def add_child(node, node_name):
    '''
    Add a new child to the passed node, returning a reference to it
    '''

    return etree.SubElement(node, node_name)

def get_child(node, node_name):
    '''
    Return the first child matching node_name in node
    '''
    return node.find(XML_VERSION + ":" + node_name, XML_NAMESPACE)

def get_child_as_vector(node, node_name, delimiter=' '):
    '''
    Return the first child matching node_name in node as App.Vector
    '''

    result = get_child(node, node_name)

    if result is None:
        return None

    vec_list = result.text.strip().split(delimiter)

    #validate values as floating point
    try:
        vec_list = [float(_v) for _v in vec_list]
    except:
        return None

    _len = len(vec_list)

    #pad the vector if it's too short
    if _len < 3:
        vec_list = vec_list + [0.0]*(3-_len)

    return App.Vector(vec_list)

def get_children(node, node_name):
    '''
    Return all children mathcing node_name in node
    '''
    return node.findall(XML_VERSION + ':' + node_name, XML_NAMESPACE)

def get_float_list(text, delimiter=' '):
    '''
    Return a list of floats from a text string of delimited values
    '''

    values = text.replace('\n', '')
    return list(filter(None, values.split(delimiter)))

def build_vector(coords):
    '''
    Returns an App.Vector of the passed coordinates,
    ensuring they are float-compatible
    '''

    if not coords:
        return None

    float_coords = Utils.to_float(coords)

    if not all(float_coords):
        return None

    return App.Vector(float_coords)

def write_meta_data(data, tree):
    '''
    Write out the meta data into the internal XML file
    '''

    pass

def _write_station_data(data, tree):
    '''
    Write out the station data into the internal XML file
    '''

    pass

def _write_curve_data(data, tree):
    '''
    Write out the alignment / curve data into the internal XML file
    '''

    pass

def write_file(data, tree, target):
    '''
    Write the data to a land xml file in the target location
    '''

    #_write_meta_data(data['meta'], )
    #_write_station_data(data['station'])
    #_write_curve_data(data['curve'])

    pass

def export_file(source, target):
    '''
    Export a LandXML file
    source - The source filepath (the transient LandXML file)
    target - The target datapath external to the FCStd
    '''

    copyfile(source, target)
