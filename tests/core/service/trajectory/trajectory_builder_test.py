# -*- coding: UTF-8 -*-

'''
Module
    trajectory_builder_test.py
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
    Unit tests for TrajectoryBuilder class.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.model.command_id import CommandId
from tetrapoder.core.model.leg_angles import LegAngles
from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.model.point3d import Point3D
from tetrapoder.core.service.kinematics.solver import KinematicsSolver
from tetrapoder.core.service.trajectory.trajectory_builder import TrajectoryBuilder

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestTrajectoryBuilder(TestCase):
    '''
        Test cases verifying TrajectoryBuilder trajectory planning.

        It defines:

            :methods:
                | test_add_keyframe - Verifies adding Cartesian keyframe.
                | test_add_joint_keyframe - Verifies adding joint angle keyframe directly.
                | test_build_empty - Verifies building empty plan by default.
    '''

    def test_add_keyframe(self) -> None:
        '''
            Verifies adding Cartesian keyframe.

            :exceptions: None.
        '''
        builder: TrajectoryBuilder = TrajectoryBuilder(KinematicsSolver(), [])
        target: Point3D = Point3D(x=0.0, y=80.0, z=-50.0)
        builder.add_keyframe(0, target, duration_ms=250)
        plan: MotionPlan = builder.build()
        self.assertEqual(len(plan.commands), 1)
        self.assertEqual(plan.commands[0].cmd_id, int(CommandId.QUEUE_KEYFRAME))

    def test_add_joint_keyframe(self) -> None:
        '''
            Verifies adding joint angle keyframe directly.

            :exceptions: None.
        '''
        builder: TrajectoryBuilder = TrajectoryBuilder(KinematicsSolver(), [])
        angles: LegAngles = LegAngles(coxa=90.0, femur=90.0, tibia=90.0)
        builder.add_joint_keyframe(0xFF, angles, duration_ms=100)
        plan: MotionPlan = builder.build()
        self.assertEqual(len(plan.commands), 1)
        self.assertEqual(plan.commands[0].cmd_id, int(CommandId.QUEUE_KEYFRAME))

    def test_build_empty(self) -> None:
        '''
            Verifies building empty plan by default.

            :exceptions: None.
        '''
        builder: TrajectoryBuilder = TrajectoryBuilder(KinematicsSolver(), [])
        plan: MotionPlan = builder.build()
        self.assertEqual(len(plan.commands), 0)


if __name__ == '__main__':
    main()
