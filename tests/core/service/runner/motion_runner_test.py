# -*- coding: UTF-8 -*-

'''
Module
    motion_runner_test.py
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
    Unit tests for MotionRunner execution and ping logic.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.model.command_id import CommandId
from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.model.plan_command import PlanCommand
from tetrapoder.core.model.response_id import ResponseId
from tetrapoder.core.service.protocol.protocol_frame_builder import ProtocolFrameBuilder
from tetrapoder.core.service.runner.motion_runner import MotionRunner

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class MockTransport:
    '''
        Mock transport implementation of ITransport protocol for unit testing.

        It defines:

            :attributes:
                | is_channel_open - Flag tracking open status.
                | canned_response - Bytes returned on read.
            :methods:
                | open - Sets channel open.
                | close - Sets channel closed.
                | write - Records bytes written.
                | read - Returns canned response bytes.
                | is_open - Returns open state.
    '''

    is_channel_open: bool
    canned_response: bytes

    def __init__(self, canned_response: bytes = b'') -> None:
        '''
            Initializes MockTransport.

            :param canned_response: Default bytes returned on read.
            :exceptions: None.
        '''
        self.is_channel_open = False
        self.canned_response = canned_response

    def open(self) -> None:
        '''
            Sets channel open.

            :exceptions: None.
        '''
        self.is_channel_open = True

    def close(self) -> None:
        '''
            Sets channel closed.

            :exceptions: None.
        '''
        self.is_channel_open = False

    def write(self, data: bytes) -> int:
        '''
            Returns data byte count.

            :param data: Input data.
            :return: Byte length.
            :exceptions: None.
        '''
        return len(data)

    def read(self, size: int) -> bytes:
        '''
            Returns canned response bytes.

            :param size: Number of bytes requested.
            :return: Canned response bytes.
            :exceptions: None.
        '''
        return self.canned_response[:size]

    def is_open(self) -> bool:
        '''
            Returns open state.

            :return: True if channel open.
            :exceptions: None.
        '''
        return self.is_channel_open


class TestMotionRunner(TestCase):
    '''
        Test cases verifying MotionRunner execution and ping behaviors.

        It defines:

            :methods:
                | test_ping_success - Verifies successful ping handshake.
                | test_ping_failure - Verifies failed ping handling.
                | test_execute_ack - Verifies successful plan execution with ACK.
                | test_execute_nack - Verifies failed plan execution with NACK.
    '''

    def test_ping_success(self) -> None:
        '''
            Verifies successful ping handshake.

            :exceptions: None.
        '''
        runner: MotionRunner = MotionRunner()
        pong_frame: bytes = ProtocolFrameBuilder().build_frame(int(ResponseId.PONG), b'')
        transport: MockTransport = MockTransport(canned_response=pong_frame)
        self.assertTrue(runner.ping(transport))

    def test_ping_failure(self) -> None:
        '''
            Verifies failed ping handling.

            :exceptions: None.
        '''
        runner: MotionRunner = MotionRunner()
        transport: MockTransport = MockTransport(canned_response=b'\x00\x00\x00\x00')
        self.assertFalse(runner.ping(transport))

    def test_execute_ack(self) -> None:
        '''
            Verifies successful plan execution with ACK.

            :exceptions: None.
        '''
        runner: MotionRunner = MotionRunner()
        ack_frame: bytes = ProtocolFrameBuilder().build_frame(int(ResponseId.ACK), b'\x00')
        transport: MockTransport = MockTransport(canned_response=ack_frame)
        cmd: PlanCommand = PlanCommand(cmd_id=int(CommandId.PING), payload=b'', description='Ping')
        plan: MotionPlan = MotionPlan(commands=(cmd,))
        self.assertTrue(runner.execute(plan, transport))

    def test_execute_nack(self) -> None:
        '''
            Verifies failed plan execution with NACK.

            :exceptions: None.
        '''
        runner: MotionRunner = MotionRunner()
        nack_frame: bytes = ProtocolFrameBuilder().build_frame(int(ResponseId.NACK), b'\x01')
        transport: MockTransport = MockTransport(canned_response=nack_frame)
        cmd: PlanCommand = PlanCommand(cmd_id=int(CommandId.PING), payload=b'', description='Ping')
        plan: MotionPlan = MotionPlan(commands=(cmd,))
        self.assertFalse(runner.execute(plan, transport))


if __name__ == '__main__':
    main()
