# -*- coding: UTF-8 -*-

'''
Module
    cartesian_kinematics.py
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
    Demonstration of 3D Cartesian inverse kinematics and trajectory generation.
'''

from __future__ import annotations

from sys import exit as sys_exit, stdout

from tetrapoder.core.model.leg_angles import LegAngles
from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.model.point3d import Point3D
from tetrapoder.core.service.compiler.motion import MotionCompiler
from tetrapoder.core.service.kinematics.solver import KinematicsSolver
from tetrapoder.core.service.protocol.crc8 import CRC8
from tetrapoder.core.service.protocol.protocol_frame_builder import ProtocolFrameBuilder
from tetrapoder.core.service.trajectory.trajectory_builder import TrajectoryBuilder

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


def main() -> bool:
    '''
        Demonstrates inverse kinematics solving and Cartesian trajectory construction.

        :return: True if compiled successfully.
        :exceptions: None.
    '''
    solver: KinematicsSolver = KinematicsSolver()
    builder: TrajectoryBuilder = TrajectoryBuilder(solver=solver, commands=[])

    # Step 1: Solve explicit IK for neutral leg position
    target: Point3D = Point3D(x=0.0, y=80.0, z=-50.0)
    stdout.write(f'Target Cartesian foot position: ({target.x:.1f}, {target.y:.1f}, {target.z:.1f}) mm\n')

    for leg_id in range(4):
        angles: LegAngles = solver.solve(leg=leg_id, target=target)
        c_i16, f_i16, t_i16 = solver.to_tenths(angles)
        stdout.write(
            f'  Leg {leg_id}: coxa={angles.coxa:.1f}° ({c_i16}), '
            f'femur={angles.femur:.1f}° ({f_i16}), tibia={angles.tibia:.1f}° ({t_i16})\n'
        )

    # Step 2: Build trajectory keyframes with interpolation
    builder.add_keyframe(leg=0, target=Point3D(x=30.0, y=70.0, z=-30.0), duration_ms=200)
    builder.add_keyframe(leg=0, target=Point3D(x=0.0, y=80.0, z=-50.0), duration_ms=200)
    builder.add_keyframe(leg=1, target=Point3D(x=-30.0, y=70.0, z=-30.0), duration_ms=200)
    builder.add_keyframe(leg=1, target=Point3D(x=0.0, y=80.0, z=-50.0), duration_ms=200)

    plan: MotionPlan = builder.build()
    frame_builder: ProtocolFrameBuilder = ProtocolFrameBuilder(CRC8())
    compiler: MotionCompiler = MotionCompiler(frame_builder=frame_builder)
    data: bytes = compiler.compile(plan=plan)
    stdout.write(f'Generated {len(plan.commands)} trajectory keyframe commands.\n')
    stdout.write(f'Compiled trajectory binary: {len(data)} bytes.\n')
    return True


if __name__ == '__main__':
    sys_exit(0 if main() else 1)
