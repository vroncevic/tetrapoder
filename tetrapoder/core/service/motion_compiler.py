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
    Motion plan binary compiler producing byte streams and flashable binary files.
'''

from __future__ import annotations

from tetrapoder.core.model.exceptions.compiler_error import CompilerError
from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.service.protocol_frame_builder import ProtocolFrameBuilder

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

            :methods:
                | compile - Compiles MotionPlan into contiguous binary byte sequence.
                | compile_to_file - Compiles and saves byte sequence to binary file.
    '''

    @classmethod
    def compile(cls, plan: MotionPlan) -> bytes:
        '''
            Compiles all commands in the plan into binary frames with CRC-8 checksums.

            :param plan: Target MotionPlan instance.
            :return: Contiguous bytes representing the wire protocol transmission.
            :exceptions: None.
        '''
        stream: bytearray = bytearray()
        for cmd in plan.commands:
            frame: bytes = ProtocolFrameBuilder.build_frame(cmd.cmd_id, cmd.payload)
            stream.extend(frame)
        return bytes(stream)

    @classmethod
    def compile_to_file(cls, plan: MotionPlan, file_path: str) -> int:
        '''
            Compiles plan and writes output directly to binary file.

            :param plan: Target MotionPlan.
            :param file_path: Absolute or relative output file path.
            :return: Number of bytes written.
            :exceptions:
                | CompilerError: If file writing fails due to I/O error.
        '''
        data: bytes = cls.compile(plan)
        try:
            with open(file_path, 'wb') as file_handle:
                file_handle.write(data)
            return len(data)
        except OSError as exc:
            raise CompilerError(f'Failed to write binary plan to {file_path}: {exc}') from exc
