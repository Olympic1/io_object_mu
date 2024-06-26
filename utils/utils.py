# vim:ts=4:et
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

def swapyz(vec):
    return vec[0], vec[2], vec[1]

def swizzleq(quaternion):
    # this works only for blender to unity
    return quaternion[1], quaternion[3], quaternion[2], -quaternion[0]

def strip_nnn(name):
    # ∧ separates the export name from the modeling name
    ind = name.rfind("∧")
    if ind >= 0:
        return name[:ind]
    # legacy check for blender's duplicate name separator
    # causes problems for naming schemes that includ the part size
    # but forcing people to add ∧ after all their objects isn't a
    # great idea, so it's useful anyway.
    ind = name.rfind(".")
    if ind < 0 or len(name) - ind != 4:
        return name
    if not name[ind+1:].isdigit():
        return name
    return name[:ind]

def vector_str(vec):
    if len(vec) == 2:
        return "%.9g, %.9g" % vec
    elif len(vec) == 3:
        return "%.9g, %.9g, %.9g" % vec
    elif len(vec) == 4:
        return "%.9g, %.9g, %.9g, %.9g" % vec
