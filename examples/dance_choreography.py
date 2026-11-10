# -*- coding: UTF-8 -*-

'''
Module
    dance_choreography.py
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
    Demonstration high-level motion plan choreography compiled via tetrapoder.
'''

from __future__ import annotations

from sys import exit as sys_exit, stdout

from tetrapoder.core.model.foot_position import FootPosition
from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.model.plan_command import PlanCommand
from tetrapoder.core.service.compiler.motion_compiler import MotionCompiler
from tetrapoder.core.service.gait.gait_plan_builder import GaitPlanBuilder
from tetrapoder.core.service.trajectory.choreography_builder import ChoreographyBuilder
from tetrapoder.core.service.trajectory.trajectory_builder import TrajectoryBuilder
from tetrapoder.infrastructure.storage.binary_writer import BinaryWriter

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
        Demonstrates creating and compiling a motion plan choreography.

        :return: True if compiled successfully.
        :exceptions: None.
    '''
    commands: list[PlanCommand] = []
    choreography: ChoreographyBuilder = ChoreographyBuilder(commands=commands)
    gait: GaitPlanBuilder = GaitPlanBuilder(commands=commands)
    trajectory: TrajectoryBuilder = TrajectoryBuilder(commands=commands)

    # 1. High-level sequence
    choreography.set_speed(speed=5)
    gait.stand()
    gait.walk(steps=4)
    gait.turn(steps=2, to_right=False)
    choreography.action_wave(count=2)
    gait.walk(steps=2, backward=True)

    # 2. Keyframe sequence (direct foot coordinates)
    trajectory.add_keyframe(
        leg=0, target=FootPosition(x=62.0, y=20.0, z=-30.0), duration_ms=250
    )
    trajectory.add_keyframe(
        leg=0, target=FootPosition(x=62.0, y=20.0, z=-50.0), duration_ms=250
    )

    gait.sit()

    # 3. Create immutable MotionPlan and compile to binary wire protocol
    plan: MotionPlan = MotionPlan(commands=tuple(commands))
    binary_data: bytes = MotionCompiler().compile(plan=plan)
    stdout.write(f'Generated {len(plan.commands)} motion commands.\n')
    stdout.write(f'Compiled binary size: {len(binary_data)} bytes.\n')
    stdout.write(f'Raw binary packet stream (hex):\n{binary_data.hex()}\n')

    # Save to file via infrastructure storage adapter
    BinaryWriter().write(file_path='dance_sequence.bin', data=binary_data)
    stdout.write('Compiled to dance_sequence.bin successfully.\n')
    return True


if __name__ == '__main__':
    sys_exit(0 if main() else 1)
