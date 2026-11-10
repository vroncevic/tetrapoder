# -*- coding: UTF-8 -*-

'''
Module
    posture_compensator_test.py
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
    Unit tests for PostureCompensator service.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.model.exceptions.kinematics_error import KinematicsError
from tetrapoder.core.model.imu_telemetry import ImuTelemetry
from tetrapoder.core.model.point3d import Point3D
from tetrapoder.core.service.stabilizer.posture_compensator import PostureCompensator

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestPostureCompensator(TestCase):
    '''
        Test cases verifying PostureCompensator tilt compensation.

        It defines:

            :methods:
                | test_level_attitude - Verifies zero offset when body is level.
                | test_roll_compensation - Verifies lateral offset on roll tilt.
                | test_pitch_compensation - Verifies longitudinal offset on pitch tilt.
                | test_compensate_target - Verifies applying offset to nominal target point.
                | test_invalid_leg_index - Verifies KinematicsError on invalid leg index.
    '''

    def test_level_attitude(self) -> None:
        '''
            Verifies zero offset when body is level.

            :exceptions: None.
        '''
        compensator: PostureCompensator = PostureCompensator(body_width=120.0, body_length=120.0)
        telemetry: ImuTelemetry = ImuTelemetry(
            roll=0.0,
            pitch=0.0,
            accel_x=0.0,
            accel_y=0.0,
            accel_z=1.0,
            gyro_z=0.0,
        )
        for leg_id in range(4):
            offset: Point3D = compensator.calculate_offset(leg_id, telemetry)
            self.assertAlmostEqual(offset.x, 0.0)
            self.assertAlmostEqual(offset.y, 0.0)
            self.assertAlmostEqual(offset.z, 0.0)

    def test_roll_compensation(self) -> None:
        '''
            Verifies lateral offset on roll tilt.

            :exceptions: None.
        '''
        compensator: PostureCompensator = PostureCompensator(body_width=120.0, body_length=120.0)
        telemetry: ImuTelemetry = ImuTelemetry(
            roll=10.0,
            pitch=0.0,
            accel_x=0.0,
            accel_y=0.0,
            accel_z=1.0,
            gyro_z=0.0,
        )
        offset_fr: Point3D = compensator.calculate_offset(0, telemetry)
        offset_fl: Point3D = compensator.calculate_offset(1, telemetry)
        offset_rl: Point3D = compensator.calculate_offset(2, telemetry)
        offset_rr: Point3D = compensator.calculate_offset(3, telemetry)

        self.assertLess(offset_fr.z, 0.0)
        self.assertGreater(offset_fl.z, 0.0)
        self.assertGreater(offset_rl.z, 0.0)
        self.assertLess(offset_rr.z, 0.0)

    def test_pitch_compensation(self) -> None:
        '''
            Verifies longitudinal offset on pitch tilt.

            :exceptions: None.
        '''
        compensator: PostureCompensator = PostureCompensator(body_width=120.0, body_length=120.0)
        telemetry: ImuTelemetry = ImuTelemetry(
            roll=0.0,
            pitch=10.0,
            accel_x=0.0,
            accel_y=0.0,
            accel_z=1.0,
            gyro_z=0.0,
        )
        offset_fr: Point3D = compensator.calculate_offset(0, telemetry)
        offset_fl: Point3D = compensator.calculate_offset(1, telemetry)
        offset_rl: Point3D = compensator.calculate_offset(2, telemetry)
        offset_rr: Point3D = compensator.calculate_offset(3, telemetry)

        self.assertGreater(offset_fr.z, 0.0)
        self.assertGreater(offset_fl.z, 0.0)
        self.assertLess(offset_rl.z, 0.0)
        self.assertLess(offset_rr.z, 0.0)

    def test_compensate_target(self) -> None:
        '''
            Verifies applying offset to nominal target point.

            :exceptions: None.
        '''
        compensator: PostureCompensator = PostureCompensator(body_width=120.0, body_length=120.0)
        telemetry: ImuTelemetry = ImuTelemetry(
            roll=5.0,
            pitch=-5.0,
            accel_x=0.0,
            accel_y=0.0,
            accel_z=1.0,
            gyro_z=0.0,
        )
        nominal: Point3D = Point3D(x=10.0, y=80.0, z=-50.0)
        adjusted: Point3D = compensator.compensate(0, nominal, telemetry)
        offset: Point3D = compensator.calculate_offset(0, telemetry)

        self.assertEqual(adjusted.x, nominal.x)
        self.assertEqual(adjusted.y, nominal.y)
        self.assertAlmostEqual(adjusted.z, nominal.z + offset.z)

    def test_invalid_leg_index(self) -> None:
        '''
            Verifies KinematicsError on invalid leg index.

            :exceptions: None.
        '''
        compensator: PostureCompensator = PostureCompensator()
        telemetry: ImuTelemetry = ImuTelemetry(
            roll=0.0,
            pitch=0.0,
            accel_x=0.0,
            accel_y=0.0,
            accel_z=1.0,
            gyro_z=0.0,
        )
        with self.assertRaises(KinematicsError):
            compensator.calculate_offset(4, telemetry)

        with self.assertRaises(KinematicsError):
            compensator.compensate(-1, Point3D(x=0.0, y=0.0, z=0.0), telemetry)


if __name__ == '__main__':
    main()
