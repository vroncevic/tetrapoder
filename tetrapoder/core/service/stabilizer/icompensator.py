# -*- coding: UTF-8 -*-

'''
Module
    icompensator.py
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
    Structural interface for quadruped closed-loop posture compensator.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

from tetrapoder.core.model.imu_telemetry import ImuTelemetry
from tetrapoder.core.model.point3d import Point3D

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class IPostureCompensator(Protocol):
    '''
        Structural protocol defining posture attitude stabilization compensator.

        It defines:

            :methods:
                | calculate_offset - Calculates differential Cartesian offset for a leg.
                | compensate - Applies posture tilt compensation to a nominal target point.
    '''

    def calculate_offset(self, leg: int, telemetry: ImuTelemetry) -> Point3D:
        '''
            Calculates differential Cartesian offset for a leg from IMU telemetry.

            :param leg: Leg index (0..3).
            :param telemetry: ImuTelemetry attitude sensor data.
            :return: Point3D offset adjustment in mm.
        '''

    def compensate(self, leg: int, nominal: Point3D, telemetry: ImuTelemetry) -> Point3D:
        '''
            Applies posture tilt compensation to a nominal target point.

            :param leg: Leg index (0..3).
            :param nominal: Nominal uncompensated Point3D target.
            :param telemetry: ImuTelemetry attitude sensor data.
            :return: Stabilized Point3D target.
        '''
