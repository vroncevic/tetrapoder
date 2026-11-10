# -*- coding: UTF-8 -*-

'''
Module
    posture_compensator.py
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
    Concrete implementation of closed-loop posture compensator.
'''

from __future__ import annotations

from math import radians, sin

from tetrapoder.core.model.exceptions.kinematics_error import KinematicsError
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


class PostureCompensator:
    '''
        Defines class PostureCompensator implementing IPostureCompensator structurally.
        Calculates differential Cartesian leg adjustments to level body based on IMU tilt.

        It defines:

            :attributes:
                | _half_width - Half of lateral distance between leg mounts in mm.
                | _half_length - Half of longitudinal distance between leg mounts in mm.
            :methods:
                | __init__ - Initializes PostureCompensator with body dimensions.
                | calculate_offset - Calculates differential Cartesian offset for a leg.
                | compensate - Applies posture tilt compensation to a nominal target point.
    '''

    _half_length: float
    _half_width: float

    def __init__(
        self,
        *,
        body_width: float = 120.0,
        body_length: float = 120.0,
    ) -> None:
        '''
            Initializes PostureCompensator with chassis dimensions.

            :param body_width: Lateral distance between leg mounts in mm.
            :param body_length: Longitudinal distance between leg mounts in mm.
            :exceptions: None.
        '''
        self._half_width = body_width / 2.0
        self._half_length = body_length / 2.0

    def calculate_offset(self, leg: int, telemetry: ImuTelemetry) -> Point3D:
        '''
            Calculates differential Cartesian offset for a leg from IMU telemetry.

            :param leg: Leg index (0..3).
            :param telemetry: ImuTelemetry attitude sensor data.
            :return: Point3D offset adjustment in mm.
            :exceptions:
                | KinematicsError: If leg index is invalid.
        '''
        leg_x: float
        leg_y: float
        match leg:
            case 0:
                leg_x = self._half_width
                leg_y = self._half_length
            case 1:
                leg_x = -self._half_width
                leg_y = self._half_length
            case 2:
                leg_x = -self._half_width
                leg_y = -self._half_length
            case 3:
                leg_x = self._half_width
                leg_y = -self._half_length
            case _:
                raise KinematicsError(f'Invalid leg index {leg}: must be 0, 1, 2, or 3')

        r_rad: float = radians(telemetry.roll)
        p_rad: float = radians(telemetry.pitch)
        delta_z: float = -leg_x * sin(r_rad) + leg_y * sin(p_rad)
        return Point3D(x=0.0, y=0.0, z=delta_z)

    def compensate(self, leg: int, nominal: Point3D, telemetry: ImuTelemetry) -> Point3D:
        '''
            Applies posture tilt compensation to a nominal target point.

            :param leg: Leg index (0..3).
            :param nominal: Nominal uncompensated Point3D target.
            :param telemetry: ImuTelemetry attitude sensor data.
            :return: Stabilized Point3D target.
            :exceptions:
                | KinematicsError: If leg index is invalid.
        '''
        offset: Point3D = self.calculate_offset(leg, telemetry)
        return Point3D(
            x=nominal.x + offset.x,
            y=nominal.y + offset.y,
            z=nominal.z + offset.z,
        )
