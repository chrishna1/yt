"""
API for lightcone

Author: Matthew Turk <matthewturk@gmail.com>
Affiliation: UCSD
Author: J.S. Oishi <jsoishi@gmail.com>
Affiliation: KIPAC/SLAC/Stanford
Author: Britton Smith <brittonsmith@gmail.com>
Affiliation: MSU
Homepage: http://yt.enzotools.org/
License:
  Copyright (C) 2010 Matthew Turk.  All Rights Reserved.

  This file is part of yt.

  yt is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from .common_n_volume import \
    commonNVolume, \
    commonSegment

from .halo_mask import \
    light_cone_halo_mask, \
    light_cone_halo_map

from .light_cone import \
    LightCone

from .unique_solution import \
    project_unique_light_cones, \
    find_unique_solutions