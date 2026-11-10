# -*- coding: UTF-8 -*-

'''
Module
    ikinematics_solver.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    tetrapoder is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    tetrapoder is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Structural interface for quadruped leg inverse kinematics solver.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

from tetrapoder.core.model.foot_position import FootPosition
from tetrapoder.core.model.leg_angles import LegAngles

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class IKinematicsSolver(Protocol):
    '''
        Structural protocol defining quadruped leg inverse kinematics.

        It defines:

            :methods:
                | cartesian_to_polar - Converts Cartesian coordinates to polar link angles.
                | polar_to_servo - Converts polar angles into servo shaft angles.
                | solve - Solves inverse kinematics for a target leg foot position.
    '''

    def cartesian_to_polar(self, x: float, y: float, z: float) -> tuple[float, float, float]:
        '''
            Transforms Cartesian coordinate into polar leg angles (alpha, beta, gamma).

            :param x: Lateral coordinate in mm.
            :param y: Forward coordinate in mm.
            :param z: Vertical elevation coordinate in mm.
            :return: Tuple of (alpha, beta, gamma) in radians.
        '''

    def polar_to_servo(self, leg: int, alpha: float, beta: float, gamma: float) -> LegAngles:
        '''
            Transforms polar link angles to servo horn degrees.

            :param leg: Leg index (0..3).
            :param alpha: Hip yaw angle in radians.
            :param beta: Femur pitch angle in radians.
            :param gamma: Tibia pitch angle in radians.
            :return: LegAngles with degrees (0..180).
        '''

    def solve(self, leg: int, target: FootPosition) -> LegAngles:
        '''
            Solves full inverse kinematics mapping 3D Cartesian target to joint angles.

            :param leg: Leg index (0..3).
            :param target: FootPosition Cartesian coordinates.
            :return: LegAngles containing servo angles in degrees.
        '''
