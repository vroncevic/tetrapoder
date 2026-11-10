# -*- coding: UTF-8 -*-

'''
Module
    protocol_frame_builder.py
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
    Binary serial protocol frame definitions, constants, and packet encoders.
'''

from __future__ import annotations

from struct import pack
from typing import ClassVar

from tetrapoder.core.model.exceptions.protocol_error import ProtocolError
from tetrapoder.core.service.protocol.crc8 import CRC8

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProtocolFrameBuilder:
    '''
        Defines class ProtocolFrameBuilder implementing IProtocolFrameBuilder structurally.
        Builds and parses binary serial protocol frames protected by CRC-8 checksums.

        It defines:

            :attributes:
                | SYNC_BYTE - 0xAA frame synchronization byte.
                | MAX_PAYLOAD_SIZE - Maximum allowed payload length (16 bytes).
            :methods:
                | build_frame - Encapsulates payload into wire-level frame with CRC-8.
                | unpack_frame - Parses and validates an incoming wire frame.
    '''

    SYNC_BYTE: ClassVar[int] = 0xAA
    MAX_PAYLOAD_SIZE: ClassVar[int] = 16

    @classmethod
    def build_frame(cls, msg_id: int, payload: bytes = b'') -> bytes:
        '''
            Packs message ID and payload into binary frame protected by CRC-8.

            :param msg_id: Command or response ID.
            :param payload: Binary payload bytes.
            :return: Formatted wire-level frame.
            :exceptions:
                | ProtocolError: If payload length exceeds MAX_PAYLOAD_SIZE.
        '''
        if len(payload) > cls.MAX_PAYLOAD_SIZE:
            raise ProtocolError(
                f'Payload length {len(payload)} exceeds maximum {cls.MAX_PAYLOAD_SIZE} bytes'
            )

        header: bytes = pack('>BBB', cls.SYNC_BYTE, msg_id & 0xFF, len(payload))
        crc_data: bytes = pack('>BB', msg_id & 0xFF, len(payload)) + payload
        crc: int = CRC8.calculate(crc_data)
        return header + payload + pack('>B', crc)

    @classmethod
    def unpack_frame(cls, data: bytes) -> tuple[int, bytes] | None:
        '''
            Unpacks and verifies CRC-8 on an incoming frame.

            :param data: Wire bytes starting with SYNC byte.
            :return: Tuple of (msg_id, payload) if valid, None if invalid.
            :exceptions: None.
        '''
        if len(data) < 4 or data[0] != cls.SYNC_BYTE:
            return None

        msg_id: int = data[1]
        length: int = data[2]
        if len(data) < 4 + length:
            return None

        payload: bytes = data[3:3 + length]
        received_crc: int = data[3 + length]

        expected_crc: int = CRC8.calculate(data[1:3 + length])
        if received_crc != expected_crc:
            return None

        return (msg_id, payload)
