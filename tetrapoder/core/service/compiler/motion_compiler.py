# -*- coding: UTF-8 -*-

'''
Module
    motion_compiler.py
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
    Motion plan binary compiler producing contiguous wire-protocol byte streams.
'''

from __future__ import annotations

from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.model.plan_command import PlanCommand
from tetrapoder.core.service.protocol.iprotocol_frame_builder import IProtocolFrameBuilder

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class MotionCompiler:
    '''
        Defines class MotionCompiler implementing IMotionCompiler structurally.
        Serializes high-level motion plans into contiguous binary protocol frames.

        It defines:

            :attributes:
                | _frame_builder - Injected protocol frame serialization provider.
            :methods:
                | __init__ - Initializes MotionCompiler with frame builder dependency.
                | compile - Compiles MotionPlan into contiguous binary byte sequence.
                | compile_command - Compiles a single motion command into wire-level frame.
    '''

    _frame_builder: IProtocolFrameBuilder

    def __init__(self, frame_builder: IProtocolFrameBuilder) -> None:
        '''
            Initializes MotionCompiler with frame builder provider.

            :param frame_builder: Injected IProtocolFrameBuilder implementation.
            :exceptions: None.
        '''
        self._frame_builder = frame_builder

    def compile_command(self, cmd: PlanCommand) -> bytes:
        '''
            Compiles a single motion command into wire-level binary frame.

            :param cmd: PlanCommand instance to compile.
            :return: Formatted wire-level frame bytes.
            :exceptions: None.
        '''
        return self._frame_builder.build_frame(cmd.cmd_id, cmd.payload)

    def compile(self, plan: MotionPlan) -> bytes:
        '''
            Compiles all commands in the plan into binary frames with CRC-8 checksums.

            :param plan: Target MotionPlan instance.
            :return: Contiguous bytes representing the wire protocol transmission.
            :exceptions: None.
        '''
        stream: bytearray = bytearray()

        for cmd in plan.commands:
            stream.extend(self.compile_command(cmd))

        return bytes(stream)
