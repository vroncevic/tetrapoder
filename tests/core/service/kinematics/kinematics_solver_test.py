# -*- coding: UTF-8 -*-

'''
Module
    kinematics_solver_test.py
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
    Unit tests for KinematicsSolver class.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.model.exceptions.kinematics_error import KinematicsError
from tetrapoder.core.model.leg_angles import LegAngles
from tetrapoder.core.model.point3d import Point3D
from tetrapoder.core.service.kinematics.kinematics_solver import KinematicsSolver

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestKinematicsSolver(TestCase):
    '''
        Test cases verifying KinematicsSolver computations.

        It defines:

            :methods:
                | test_reachability - Verifies reachable workspace calculation for neutral pose.
                | test_out_of_reach_error - Verifies exception raised when target exceeds leg reach.
                | test_invalid_leg_index - Verifies exception raised for invalid leg index.
                | test_to_tenths - Verifies conversion of angles to integer tenths of a degree.
    '''

    def test_reachability(self) -> None:
        '''
            Verifies reachable workspace calculation for neutral pose.

            :exceptions: None.
        '''
        solver: KinematicsSolver = KinematicsSolver()
        target: Point3D = Point3D(x=0.0, y=80.0, z=-50.0)
        angles: LegAngles = solver.solve(0, target)
        self.assertGreaterEqual(angles.coxa, 0.0)
        self.assertLessEqual(angles.coxa, 180.0)
        self.assertGreaterEqual(angles.femur, 0.0)
        self.assertLessEqual(angles.femur, 180.0)
        self.assertGreaterEqual(angles.tibia, 0.0)
        self.assertLessEqual(angles.tibia, 180.0)

    def test_out_of_reach_error(self) -> None:
        '''
            Verifies exception raised when target exceeds leg reach.

            :exceptions: None.
        '''
        solver: KinematicsSolver = KinematicsSolver()
        target: Point3D = Point3D(x=0.0, y=500.0, z=-500.0)
        with self.assertRaises(KinematicsError):
            solver.solve(0, target)

    def test_invalid_leg_index(self) -> None:
        '''
            Verifies exception raised for invalid leg index.

            :exceptions: None.
        '''
        solver: KinematicsSolver = KinematicsSolver()
        target: Point3D = Point3D(x=0.0, y=80.0, z=-50.0)
        with self.assertRaises(KinematicsError):
            solver.solve(4, target)

    def test_to_tenths(self) -> None:
        '''
            Verifies conversion of angles to integer tenths of a degree.

            :exceptions: None.
        '''
        solver: KinematicsSolver = KinematicsSolver()
        angles: LegAngles = LegAngles(coxa=90.0, femur=45.5, tibia=120.3)
        self.assertEqual(solver.to_tenths(angles), (900, 455, 1203))


if __name__ == '__main__':
    main()
