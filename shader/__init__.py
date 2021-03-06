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

from .. import register_submodules

from .shader import make_shader

from .shader_config import load_shader_configs

submodule_names = (
    "colorprops",
    "float2props",
    "float3props",
    "imageprops",
    "textureprops",
    "vectorprops",

    "materialprops",
    "menus",
    "operators",
    "panels",
)
register_submodules(__name__, submodule_names)
load_shader_configs(__path__[0])
