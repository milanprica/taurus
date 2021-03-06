#!/usr/bin/env python

#############################################################################
##
# This file is part of Taurus
##
# http://taurus-scada.org
##
# Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
##
# Taurus is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# Taurus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
##
# You should have received a copy of the GNU Lesser General Public License
# along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################

"""This package contains a collection of Qt based widgets designed to interact with
taurus models. The widgets are generic in the sence that they do not assume any
behavior associated with a specific HW device. They intend to represent only
abstract model data."""

__docformat__ = 'restructuredtext'


# register icon path files and icon theme on import of taurus.qt.qtgui
import icon as __icon
import os
import glob
from taurus import tauruscustomsettings as __S

icon_dir = os.path.join(os.path.dirname(os.path.abspath(__icon.__file__)))
# TODO: get .path file glob pattern from tauruscustomsettings
__icon.registerPathFiles(glob.glob(os.path.join(icon_dir,'*.path')))
# TODO: get theme name and path from tauruscustomsettings
__icon.registerTheme(name=getattr(__S, 'QT_THEME_NAME', 'Tango'),
                     path=getattr(__S, 'QT_THEME_DIR', ''),
                     force=getattr(__S, 'QT_THEME_FORCE_ON_LINUX', False))

del os, glob, __icon, icon_dir