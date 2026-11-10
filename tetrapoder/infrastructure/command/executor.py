# -*- coding: UTF-8 -*-

'''
Module
    executor.py
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
    Command execution strategy for tetrapoder robot operations.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.utils.reflection import to_str

from tetrapoder.core.model.exceptions.runner_error import RunnerError
from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.service.compiler.motion import MotionCompiler
from tetrapoder.core.service.gait.builder import GaitPlanBuilder
from tetrapoder.core.service.crc8.crc import CRC8
from tetrapoder.core.service.protocol.frame import ProtocolFrameBuilder
from tetrapoder.core.service.runner.runner import MotionRunner
from tetrapoder.infrastructure.command.idefinition import ICommandDefinition
from tetrapoder.infrastructure.storage.binary_writer import BinaryWriter
from tetrapoder.infrastructure.transport.serial import SerialTransport

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TetrapoderCommandExecutor:
    '''
        Command executor implementing tetrapoder CLI commands.

        It defines:

            :attributes:
                | definition - Associated subcommand definition.
            :methods:
                | __init__ - Initializes the command executor.
                | execute - Executes subcommand strategy according to CLI params.
                | get_definition - Returns command definition metadata.
                | __str__ - Returns string representation of executor.
    '''

    definition: ICommandDefinition

    def __init__(self, definition: ICommandDefinition) -> None:
        '''
            Initializes the command executor.

            :param definition: Associated subcommand definition.
            :exceptions: None.
        '''
        self.definition = definition

    def execute(self, *, params: Mapping[str, object]) -> Mapping[str, object]:
        '''
            Executes subcommand strategy according to CLI params.

            :param params: Subcommand parameters from CLI parser.
            :return: Mapping containing returncode, stdout, stderr.
            :exceptions: None.
        '''
        action: str = str(params.get('action', 'ping'))
        port: str = str(params.get('port', '/dev/ttyUSB0'))
        baud: int = int(params.get('baud', 57600))
        gait_name: str = str(params.get('gait', 'stand'))
        output: str = str(params.get('output', 'motion.bin'))

        builder: GaitPlanBuilder = GaitPlanBuilder([])

        match gait_name:
            case 'sit':
                builder.sit()
            case 'walk':
                builder.walk(steps=2)
            case 'wave':
                builder.stand()
            case _:
                builder.stand()

        plan: MotionPlan = builder.build()

        match action:
            case 'compile':
                frame_builder: ProtocolFrameBuilder = ProtocolFrameBuilder(CRC8())
                data: bytes = MotionCompiler(frame_builder).compile(plan)
                count: int = BinaryWriter().write(output, data)
                return {
                    'returncode': 0,
                    'stdout': f'Compiled {len(plan.commands)} commands ({count} bytes) to {output}',
                    'stderr': '',
                }
            case 'ping':
                try:
                    transport: SerialTransport = SerialTransport(port=port, baudrate=baud)
                    frame_builder = ProtocolFrameBuilder(CRC8())
                    pong: bool = MotionRunner(frame_builder).ping(transport)
                    status_str: str = 'PONG received' if pong else 'Ping failed or timed out'
                    return {
                        'returncode': 0 if pong else 1,
                        'stdout': f'Ping {port} at {baud} baud: {status_str}',
                        'stderr': '' if pong else 'No PONG response from robot',
                    }
                except RunnerError as exc:
                    return {
                        'returncode': 1,
                        'stdout': '',
                        'stderr': f'Ping failed: {exc}',
                    }
            case _:
                return {
                    'returncode': 0,
                    'stdout': f'Generated {len(plan.commands)} gait commands for {gait_name}',
                    'stderr': '',
                }

    def get_definition(self) -> ICommandDefinition:
        '''
            Returns command definition metadata.

            :return: Associated command definition.
            :exceptions: None.
        '''
        return self.definition

    def __str__(self) -> str:
        '''
            Returns string representation of executor.

            :return: String representation.
            :exceptions: None.
        '''
        return to_str(self)
