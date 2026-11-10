# -*- coding: UTF-8 -*-

'''
Module
    choreography_builder.py
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
    Builder for robot choreography sequences and action commands.
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


class ChoreographyBuilder:
    '''
        Defines class ChoreographyBuilder implementing IChoreographyBuilder structurally.
        Constructs robot choreography sequences: speed adjustments, gestures, and emergency stop.

        It defines:

            :attributes:
                | _commands - Mutable accumulator list of plan commands.
            :methods:
                | __init__ - Initializes ChoreographyBuilder with optional commands list.
                | set_speed - Sets global speed multiplier (1..10).
                | action_wave - Adds hand wave choreographic gesture command.
                | emergency_stop - Adds emergency stop command.
                | build - Constructs immutable MotionPlan from accumulated commands.
    '''

    _commands: list[PlanCommand]

    def __init__(self, commands: list[PlanCommand] | None = None) -> None:
        '''
            Initializes ChoreographyBuilder with optional commands list.

            :param commands: Optional mutable accumulator list.
            :exceptions: None.
        '''
        self._commands = [] if commands is None else commands

    def set_speed(self, speed: int) -> Self:
        '''
            Sets global speed multiplier (1..10).

            :param speed: Speed multiplier integer.
            :return: Self for chaining.
            :exceptions: None.
        '''
        clamped_speed: int = max(1, min(10, speed))
        payload: bytes = pack('>B', clamped_speed)
        self._commands.append(
            PlanCommand(cmd_id=int(CommandId.SET_SPEED), payload=payload, description=f'Set Speed {clamped_speed}')
        )
        return self

    def action_wave(self, count: int = 2) -> Self:
        '''
            Adds hand wave choreographic action.

            :param count: Number of wave cycles.
            :return: Self for chaining.
            :exceptions: None.
        '''
        payload: bytes = pack('>BB', int(GaitType.HAND_WAVE), count & 0xFF)
        self._commands.append(
            PlanCommand(cmd_id=int(CommandId.GAIT_STEP), payload=payload, description=f'Wave {count} times')
        )
        return self

    def emergency_stop(self) -> Self:
        '''
            Adds emergency stop command.

            :return: Self for chaining.
            :exceptions: None.
        '''
        self._commands.append(
            PlanCommand(cmd_id=int(CommandId.STOP), payload=b'', description='Emergency Stop')
        )
        return self

    def build(self) -> MotionPlan:
        '''
            Constructs immutable MotionPlan from accumulated commands.

            :return: Immutable MotionPlan instance.
            :exceptions: None.
        '''
        return MotionPlan(commands=tuple(self._commands))
