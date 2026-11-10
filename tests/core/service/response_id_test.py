# -*- coding: UTF-8 -*-

'''
Module
    response_id_test.py
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
    Unit tests for ResponseId enumeration.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.service.response_id import ResponseId

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestResponseId(TestCase):
    '''
        Test cases verifying ResponseId enumeration.

        It defines:

            :methods:
                | test_response_values - Verifies integer values for response IDs.
    '''

    def test_response_values(self) -> None:
        '''
            Verifies integer values for response IDs.

            :exceptions: None.
        '''
        self.assertEqual(ResponseId.ACK, 0x80)
        self.assertEqual(ResponseId.NACK, 0x81)
        self.assertEqual(ResponseId.PONG, 0x84)
        self.assertEqual(ResponseId.STATUS, 0x90)


if __name__ == '__main__':
    main()
