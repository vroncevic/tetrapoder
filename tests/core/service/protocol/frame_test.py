# -*- coding: UTF-8 -*-

'''
Module
    frame_test.py
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
    Unit tests for ProtocolFrameBuilder frame packing and unpacking.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.model.command_id import CommandId
from tetrapoder.core.model.exceptions.protocol_error import ProtocolError
from tetrapoder.core.service.crc8.crc import CRC8
from tetrapoder.core.service.protocol.frame import ProtocolFrameBuilder

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestProtocolFrameBuilder(TestCase):
    '''
        Test cases verifying ProtocolFrameBuilder frame serialization.

        It defines:

            :methods:
                | test_build_and_unpack - Verifies packing and unpacking valid frames.
                | test_payload_exceeded - Verifies exception when payload exceeds limit.
                | test_corrupt_crc - Verifies unpacking raises ProtocolError on CRC corruption.
                | test_short_frame - Verifies unpacking raises ProtocolError on short frame.
                | test_incomplete_frame - Verifies unpacking raises ProtocolError on incomplete frame.
    '''

    def test_build_and_unpack(self) -> None:
        '''
            Verifies packing and unpacking valid frames.

            :exceptions: None.
        '''
        builder: ProtocolFrameBuilder = ProtocolFrameBuilder(CRC8())
        frame: bytes = builder.build_frame(int(CommandId.PING), b'')
        self.assertEqual(len(frame), 4)
        self.assertEqual(frame[0], builder.SYNC_BYTE)
        self.assertEqual(frame[1], int(CommandId.PING))

        msg_id, payload = builder.unpack_frame(frame)
        self.assertEqual(msg_id, int(CommandId.PING))
        self.assertEqual(payload, b'')

    def test_payload_exceeded(self) -> None:
        '''
            Verifies exception when payload exceeds limit.

            :exceptions: None.
        '''
        builder: ProtocolFrameBuilder = ProtocolFrameBuilder(CRC8())
        with self.assertRaises(ProtocolError):
            builder.build_frame(0x01, b'x' * 17)

    def test_corrupt_crc(self) -> None:
        '''
            Verifies unpacking raises ProtocolError on CRC corruption.

            :exceptions: None.
        '''
        builder: ProtocolFrameBuilder = ProtocolFrameBuilder(CRC8())
        frame: bytearray = bytearray(builder.build_frame(0x01, b'\x05'))
        corrupt_frame: bytes = bytes(frame[:-1] + bytes([frame[-1] ^ 0xFF]))
        with self.assertRaises(ProtocolError):
            builder.unpack_frame(corrupt_frame)

    def test_short_frame(self) -> None:
        '''
            Verifies unpacking raises ProtocolError on short frame.

            :exceptions: None.
        '''
        builder: ProtocolFrameBuilder = ProtocolFrameBuilder(CRC8())
        with self.assertRaises(ProtocolError):
            builder.unpack_frame(b'\xAA\x01')

    def test_incomplete_frame(self) -> None:
        '''
            Verifies unpacking raises ProtocolError on incomplete frame.

            :exceptions: None.
        '''
        builder: ProtocolFrameBuilder = ProtocolFrameBuilder(CRC8())
        with self.assertRaises(ProtocolError):
            builder.unpack_frame(b'\xAA\x01\x05\x01\x02')


if __name__ == '__main__':
    main()
