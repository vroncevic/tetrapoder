# -*- coding: UTF-8 -*-

'''
Module
    leg_angles.py
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
    Immutable 3-DOF leg joint angles value object.
'''

from __future__ import annotations

from dataclasses import dataclass

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@dataclass(frozen=True, slots=True)
class LegAngles:
    '''
        Defines immutable joint angles in degrees for a 3-DOF leg.

        It defines:

            :attributes:
                | coxa - Coxa horizontal hip servo angle in degrees (0..180).
                | femur - Femur shoulder elevation servo angle in degrees (0..180).
                | tibia - Tibia knee elevation servo angle in degrees (0..180).
            :methods:
                | to_tuple - Returns angles as float 3-tuple in degrees.
                | to_tenths - Returns angles rounded to tenths of a degree (0..1800).
    '''

    coxa: float
    femur: float
    tibia: float

    def to_tuple(self) -> tuple[float, float, float]:
        '''
            Converts joint angles to float degrees 3-tuple.

            :return: Tuple of (coxa, femur, tibia) in degrees.
            :exceptions: None.
        '''
        return (self.coxa, self.femur, self.tibia)

    def to_tenths(self) -> tuple[int, int, int]:
        '''
            Converts joint angles to integer tenths of a degree for firmware transmission.

            :return: Tuple of (coxa, femur, tibia) in tenths of a degree (0..1800).
            :exceptions: None.
        '''
        return (
            int(round(self.coxa * 10.0)),
            int(round(self.femur * 10.0)),
            int(round(self.tibia * 10.0)),
        )
