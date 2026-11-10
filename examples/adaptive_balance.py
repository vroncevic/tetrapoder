# -*- coding: UTF-8 -*-

'''
Module
    adaptive_balance.py
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
    Demonstration of closed-loop posture stabilization from IMU telemetry.
'''

from __future__ import annotations

from struct import pack
from sys import exit as sys_exit, stdout

from tetrapoder.core.model.imu_telemetry import ImuTelemetry
from tetrapoder.core.model.leg_angles import LegAngles
from tetrapoder.core.model.point3d import Point3D
from tetrapoder.core.service.kinematics.kinematics_solver import KinematicsSolver
from tetrapoder.core.service.stabilizer.posture_compensator import PostureCompensator
from tetrapoder.core.service.telemetry.telemetry_decoder import TelemetryDecoder

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/tetrapoder/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


def main() -> bool:
    '''
        Demonstrates receiving IMU telemetry and computing closed-loop posture leveling.

        :return: True if executed successfully.
        :exceptions: None.
    '''
    decoder: TelemetryDecoder = TelemetryDecoder()
    compensator: PostureCompensator = PostureCompensator(body_width=120.0, body_length=120.0)
    solver: KinematicsSolver = KinematicsSolver()

    # Step 1: Simulate raw binary telemetry packet received from robot (e.g. roll=+12.0°, pitch=-8.0°)
    raw_payload: bytes = pack('>hhhhhh', 120, -80, 20, -10, 990, 0)
    telemetry: ImuTelemetry = decoder.decode(raw_payload)

    stdout.write('=== Closed-Loop Posture Stabilization ===\n')
    stdout.write(
        f'Received IMU Telemetry: Roll={telemetry.roll:+.1f}°, Pitch={telemetry.pitch:+.1f}°, '
        f'Accel=({telemetry.accel_x:+.2f}, {telemetry.accel_y:+.2f}, {telemetry.accel_z:+.2f})g\n\n'
    )

    # Step 2: Compensate nominal stand posture for each of 4 legs
    nominal_foot: Point3D = Point3D(x=0.0, y=80.0, z=-50.0)
    stdout.write(f'Nominal Foot Target: ({nominal_foot.x:.1f}, {nominal_foot.y:.1f}, {nominal_foot.z:.1f}) mm\n')

    for leg_id in range(4):
        offset: Point3D = compensator.calculate_offset(leg_id, telemetry)
        stabilized: Point3D = compensator.compensate(leg_id, nominal_foot, telemetry)
        angles: LegAngles = solver.solve(leg_id, stabilized)
        c_i16, f_i16, t_i16 = solver.to_tenths(angles)

        stdout.write(
            f'  Leg {leg_id}: Δz={offset.z:+.1f}mm -> '
            f'target=({stabilized.x:.1f}, {stabilized.y:.1f}, {stabilized.z:.1f}) mm | '
            f'coxa={angles.coxa:.1f}° ({c_i16}), femur={angles.femur:.1f}° ({f_i16}), tibia={angles.tibia:.1f}° ({t_i16})\n'
        )

    stdout.write('\nStabilization plan computed successfully.\n')
    return True


if __name__ == '__main__':
    sys_exit(0 if main() else 1)
