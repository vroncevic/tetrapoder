# -*- coding: UTF-8 -*-

'''
Module
    ikinematics_solver_test.py
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
    Unit tests for IKinematicsSolver structural protocol.
'''

from __future__ import annotations

from unittest import TestCase, main

from tetrapoder.core.service.kinematics.ikinematics_solver import IKinematicsSolver
from tetrapoder.core.service.kinematics.kinematics_solver import KinematicsSolver

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestIKinematicsSolver(TestCase):
    '''
        Test cases verifying IKinematicsSolver protocol conformance.

        It defines:

            :methods:
                | test_structural_conformance - Verifies KinematicsSolver satisfies IKinematicsSolver.
    '''

    def test_structural_conformance(self) -> None:
        '''
            Verifies KinematicsSolver satisfies IKinematicsSolver.

            :exceptions: None.
        '''
        self.assertTrue(isinstance(KinematicsSolver(), IKinematicsSolver))


if __name__ == '__main__':
    main()
