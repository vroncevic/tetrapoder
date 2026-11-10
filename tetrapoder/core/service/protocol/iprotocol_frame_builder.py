# -*- coding: UTF-8 -*-

'''
Module
    iprotocol_frame_builder.py
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
    Structural interface for binary protocol frame serialization.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class IProtocolFrameBuilder(Protocol):
    '''
        Structural protocol defining binary serial frame serialization and deserialization.

        It defines:

            :methods:
                | build_frame - Encapsulates payload into wire-level frame with CRC-8.
                | unpack_frame - Parses and validates an incoming wire frame.
    '''

    def build_frame(self, msg_id: int, payload: bytes = b'') -> bytes:
        '''
            Packs message ID and payload into binary frame protected by CRC-8.

            :param msg_id: Numeric message or command ID.
            :param payload: Binary payload bytes.
            :return: Formatted wire-level frame bytes.
        '''

    def unpack_frame(self, data: bytes) -> tuple[int, bytes]:
        '''
            Unpacks and verifies CRC-8 on an incoming frame.

            :param data: Wire bytes starting with SYNC byte.
            :return: Tuple of (msg_id, payload).
        '''
