# -*- coding: UTF-8 -*-

'''
Module
    builder.py
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
    Builder for standard quadruped robot gait and posture sequences.
'''

from __future__ import annotations

from struct import pack
from typing import Self

from tetrapoder.core.model.command_id import CommandId
from tetrapoder.core.model.gait_type import GaitType
from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.model.plan_command import PlanCommand

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GaitPlanBuilder:
    '''
        Defines class GaitPlanBuilder implementing IGaitPlanBuilder structurally.
        Constructs standard gait sequences: sit, stand, walk, turn.

        It defines:

            :attributes:
                | _commands - Mutable accumulator list of plan commands.
            :methods:
                | __init__ - Initializes GaitPlanBuilder with commands accumulator list.
                | stand - Adds stand posture command.
                | sit - Adds sit posture command.
                | walk - Adds walking step command (forward/backward).
                | turn - Adds turn command (left/right).
                | build - Constructs immutable MotionPlan from accumulated commands.
    '''

    _commands: list[PlanCommand]

    def __init__(self, commands: list[PlanCommand]) -> None:
        '''
            Initializes GaitPlanBuilder with commands accumulator list.

            :param commands: Injected mutable accumulator list.
            :exceptions: None.
        '''
        self._commands = commands

    def stand(self) -> Self:
        '''
            Adds stand posture command.

            :return: Self for chaining.
            :exceptions: None.
        '''
        payload: bytes = pack('>BB', int(GaitType.STAND), 1)
        self._commands.append(
            PlanCommand(cmd_id=int(CommandId.GAIT_STEP), payload=payload, description='Stand Up')
        )
        return self

    def sit(self) -> Self:
        '''
            Adds sit posture command.

            :return: Self for chaining.
            :exceptions: None.
        '''
        payload: bytes = pack('>BB', int(GaitType.SIT), 1)
        self._commands.append(
            PlanCommand(cmd_id=int(CommandId.GAIT_STEP), payload=payload, description='Sit Down')
        )

        return self

    def walk(self, steps: int = 1, backward: bool = False) -> Self:
        '''
            Adds forward or backward walk command.

            :param steps: Number of walk cycles.
            :param backward: True to walk backward, False for forward.
            :return: Self for chaining.
            :exceptions: None.
        '''
        gait: GaitType = GaitType.STEP_BACKWARD if backward else GaitType.STEP_FORWARD
        name: str = 'Walk Backward' if backward else 'Walk Forward'
        payload: bytes = pack('>BB', int(gait), steps & 0xFF)
        self._commands.append(
            PlanCommand(cmd_id=int(CommandId.GAIT_STEP), payload=payload, description=f'{name} {steps} steps')
        )

        return self

    def turn(self, steps: int = 1, to_right: bool = False) -> Self:
        '''
            Adds turn left or turn right command.

            :param steps: Number of turn cycles.
            :param to_right: True to turn right, False to turn left.
            :return: Self for chaining.
            :exceptions: None.
        '''
        gait: GaitType = GaitType.TURN_RIGHT if to_right else GaitType.TURN_LEFT
        name: str = 'Turn Right' if to_right else 'Turn Left'
        payload: bytes = pack('>BB', int(gait), steps & 0xFF)
        self._commands.append(
            PlanCommand(cmd_id=int(CommandId.GAIT_STEP), payload=payload, description=f'{name} {steps} steps')
        )

        return self

    def build(self) -> MotionPlan:
        '''
            Constructs immutable MotionPlan from accumulated commands.

            :return: Immutable MotionPlan instance.
            :exceptions: None.
        '''
        return MotionPlan(commands=tuple(self._commands))
