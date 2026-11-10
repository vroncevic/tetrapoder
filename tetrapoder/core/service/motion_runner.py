# -*- coding: UTF-8 -*-

'''
Module
    motion_runner.py
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
    Hardware execution runner transmitting compiled frames with ACK validation.
'''

from __future__ import annotations

from tetrapoder.core.model.command_id import CommandId
from tetrapoder.core.model.motion_plan import MotionPlan
from tetrapoder.core.model.response_id import ResponseId
from tetrapoder.core.service.itransport import ITransport
from tetrapoder.core.service.protocol_frame_builder import ProtocolFrameBuilder

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class MotionRunner:
    '''
        Defines class MotionRunner implementing IMotionRunner structurally.
        Streams compiled motion plan frames across transport with handshake verification.

        It defines:

            :methods:
                | execute - Streams motion plan frames with ACK/NACK validation.
                | ping - Verifies robot heartbeat connectivity.
    '''

    @classmethod
    def execute(cls, plan: MotionPlan, transport: ITransport) -> bool:
        '''
            Executes compiled motion plan commands over hardware transport.

            :param plan: Target MotionPlan to transmit.
            :param transport: Hardware transport instance.
            :return: True if all commands acknowledged successfully, False otherwise.
            :exceptions: None.
        '''
        if not transport.is_open():
            transport.open()

        for cmd in plan.commands:
            frame: bytes = ProtocolFrameBuilder.build_frame(cmd.cmd_id, cmd.payload)
            transport.write(frame)

            response_bytes: bytes = transport.read(5)
            unpacked = ProtocolFrameBuilder.unpack_frame(response_bytes)
            if unpacked is None or unpacked[0] != int(ResponseId.ACK):
                return False

        return True

    @classmethod
    def ping(cls, transport: ITransport) -> bool:
        '''
            Tests serial connectivity with robot heartbeat.

            :param transport: Hardware transport instance.
            :return: True if pong response received, False otherwise.
            :exceptions: None.
        '''
        if not transport.is_open():
            transport.open()

        frame: bytes = ProtocolFrameBuilder.build_frame(int(CommandId.PING), b'')
        transport.write(frame)

        resp: bytes = transport.read(4)
        unpacked = ProtocolFrameBuilder.unpack_frame(resp)
        return unpacked is not None and unpacked[0] == int(ResponseId.PONG)
