# -*- coding: UTF-8 -*-

'''
Module
    motion_compiler_test.py
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
    Unit tests for MotionCompiler class.
'''

from __future__ import annotations

from os import remove
from os.path import exists
from unittest import TestCase, main

from tetrapoder.core.model.command_id import CommandId
from tetrapoder.core.model.exceptions.compiler_error import CompilerError
from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.model.plan_command import PlanCommand
from tetrapoder.core.service.motion_compiler import MotionCompiler
from tetrapoder.core.service.protocol_frame_builder import ProtocolFrameBuilder

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestMotionCompiler(TestCase):
    '''
        Test cases verifying MotionCompiler binary compilation.

        It defines:

            :methods:
                | test_compile_bytes - Verifies compilation of motion plan into bytes.
                | test_compile_to_file - Verifies compilation and file export.
                | test_compile_error - Verifies exception raised on file write failure.
    '''

    def test_compile_bytes(self) -> None:
        '''
            Verifies compilation of motion plan into bytes.

            :exceptions: None.
        '''
        cmd: PlanCommand = PlanCommand(cmd_id=int(CommandId.PING), payload=b'', description='Ping')
        plan: MotionPlan = MotionPlan(commands=(cmd,))
        data: bytes = MotionCompiler.compile(plan)
        self.assertEqual(len(data), 4)
        self.assertEqual(data[0], ProtocolFrameBuilder.SYNC_BYTE)

    def test_compile_to_file(self) -> None:
        '''
            Verifies compilation and file export.

            :exceptions: None.
        '''
        file_path: str = '/tmp/test_plan.bin'
        cmd: PlanCommand = PlanCommand(cmd_id=int(CommandId.PING), payload=b'', description='Ping')
        plan: MotionPlan = MotionPlan(commands=(cmd,))

        try:
            bytes_written: int = MotionCompiler.compile_to_file(plan, file_path)
            self.assertEqual(bytes_written, 4)
            self.assertTrue(exists(file_path))
        finally:
            if exists(file_path):
                remove(file_path)

    def test_compile_error(self) -> None:
        '''
            Verifies exception raised on file write failure.

            :exceptions: None.
        '''
        plan: MotionPlan = MotionPlan(commands=())
        with self.assertRaises(CompilerError):
            MotionCompiler.compile_to_file(plan, '/non_existent_directory_xyz/test.bin')


if __name__ == '__main__':
    main()
