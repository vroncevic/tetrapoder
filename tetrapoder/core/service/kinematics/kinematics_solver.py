# -*- coding: UTF-8 -*-

'''
Module
    kinematics_solver.py
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
    3-DOF quadruped inverse kinematics solver with polar and servo projections.
'''

from __future__ import annotations

from math import acos, atan2, degrees, sqrt
from typing import ClassVar

from tetrapoder.core.model.exceptions.kinematics_error import KinematicsError
from tetrapoder.core.model.leg_angles import LegAngles
from tetrapoder.core.model.point3d import Point3D

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class KinematicsSolver:
    '''
        Defines class KinematicsSolver implementing IKinematicsSolver contract structurally.
        Solves geometric 3-DOF inverse kinematics for quadruped spider-style legs.

        It defines:

            :attributes:
                | COXA_LENGTH - Length of coxa link in millimeters (27.5 mm).
                | FEMUR_LENGTH - Length of femur link in millimeters (55.0 mm).
                | TIBIA_LENGTH - Length of tibia link in millimeters (55.0 mm).
            :methods:
                | cartesian_to_polar - Transforms 3D Cartesian coordinates to polar angles.
                | polar_to_servo - Converts polar angles to calibrated servo angles.
                | solve - Solves inverse kinematics for a target leg foot position.
                | to_tenths - Converts joint angles to integer tenths of a degree.
    '''

    COXA_LENGTH: ClassVar[float] = 27.5
    FEMUR_LENGTH: ClassVar[float] = 55.0
    TIBIA_LENGTH: ClassVar[float] = 55.0

    def cartesian_to_polar(self, point: Point3D) -> tuple[float, float, float]:
        '''
            Transforms Cartesian coordinate into polar leg angles (alpha, beta, gamma).

            :param point: Point3D Cartesian coordinates in mm.
            :return: Tuple of (alpha, beta, gamma) in radians.
            :exceptions:
                | KinematicsError: If target coordinates exceed physical leg reach.
        '''
        x: float = point.x
        y: float = point.y
        z: float = point.z
        dist_xy: float = sqrt(x * x + y * y)
        d_val: float = dist_xy - self.COXA_LENGTH
        l_eff: float = sqrt(d_val * d_val + z * z)

        femur: float = self.FEMUR_LENGTH
        tibia: float = self.TIBIA_LENGTH
        reach_max: float = femur + tibia
        reach_min: float = abs(femur - tibia)

        if l_eff > reach_max or l_eff < reach_min:
            raise KinematicsError(
                f'Target ({x:.1f}, {y:.1f}, {z:.1f}) outside reachable sphere '
                f'(effective length: {l_eff:.1f}mm, range: [{reach_min:.1f}..{reach_max:.1f}])'
            )

        alpha: float = atan2(x, y)
        cos_val: float = max(-1.0, min(1.0, (femur * femur + tibia * tibia - l_eff * l_eff) / (2.0 * femur * tibia)))
        gamma: float = acos(cos_val)

        phi_1: float = atan2(z, d_val)
        cos_beta: float = max(-1.0, min(1.0, (femur * femur + l_eff * l_eff - tibia * tibia) / (2.0 * femur * l_eff)))
        beta: float = phi_1 + acos(cos_beta)

        return (alpha, beta, gamma)

    def polar_to_servo(self, leg: int, alpha: float, beta: float, gamma: float) -> LegAngles:
        '''
            Transforms polar link angles to servo horn degrees.

            :param leg: Leg index (0..3).
            :param alpha: Hip yaw angle in radians.
            :param beta: Femur pitch angle in radians.
            :param gamma: Tibia pitch angle in radians.
            :return: LegAngles with degrees (0..180).
            :exceptions: None.
        '''
        a_deg: float = degrees(alpha)
        b_deg: float = degrees(beta)
        c_deg: float = degrees(gamma)

        coxa_deg: float = 90.0 - a_deg if leg in (0, 1) else 90.0 + a_deg
        femur_deg: float = 90.0 + b_deg if leg in (1, 2) else 90.0 - b_deg
        tibia_deg: float = 180.0 - c_deg if leg in (1, 2) else c_deg

        return LegAngles(
            coxa=max(0.0, min(180.0, coxa_deg)),
            femur=max(0.0, min(180.0, femur_deg)),
            tibia=max(0.0, min(180.0, tibia_deg)),
        )

    def solve(self, leg: int, target: Point3D) -> LegAngles:
        '''
            Solves full inverse kinematics mapping 3D Cartesian target to joint angles.

            :param leg: Leg index (0..3).
            :param target: Point3D Cartesian coordinates.
            :return: LegAngles containing servo angles in degrees.
            :exceptions:
                | KinematicsError: If target is out of reach or leg index is invalid.
        '''
        if leg not in (0, 1, 2, 3):
            raise KinematicsError(f'Invalid leg index {leg}: must be 0, 1, 2, or 3')

        alpha, beta, gamma = self.cartesian_to_polar(target)
        return self.polar_to_servo(leg, alpha, beta, gamma)

    def to_tenths(self, angles: LegAngles) -> tuple[int, int, int]:
        '''
            Converts joint angles to integer tenths of a degree.

            :param angles: LegAngles instance in degrees.
            :return: Tuple of (coxa, femur, tibia) in tenths of a degree.
            :exceptions: None.
        '''
        return (
            int(round(angles.coxa * 10.0)),
            int(round(angles.femur * 10.0)),
            int(round(angles.tibia * 10.0)),
        )
