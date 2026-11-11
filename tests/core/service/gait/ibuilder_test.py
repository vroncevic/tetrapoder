# -*- coding: UTF-8 -*-

'''
Module
    ibuilder_test.py
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
    Unit tests for IGaitPlanBuilder structural protocol.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.service.gait.builder import GaitPlanBuilder
from tetrapoder.core.service.gait.ibuilder import IGaitPlanBuilder

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestIGaitPlanBuilder(TestCase):
    '''
        Test cases verifying IGaitPlanBuilder protocol conformance.

        It defines:

            :methods:
                | test_structural_conformance - Verifies GaitPlanBuilder satisfies IGaitPlanBuilder.
    '''

    def test_structural_conformance(self) -> None:
        '''
            Verifies GaitPlanBuilder satisfies IGaitPlanBuilder.

            :exceptions: None.
        '''
        builder: GaitPlanBuilder = GaitPlanBuilder([])
        self.assertTrue(isinstance(builder, IGaitPlanBuilder))


if __name__ == '__main__':
    main()
