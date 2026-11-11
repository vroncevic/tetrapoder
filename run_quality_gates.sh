#!/bin/bash
#
# @brief   tetrapoder
# @version 1.0.0
# @date    Tue Nov 10 09:20:00 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 gates/gates/interfaces_checker.py tetrapoder
python3 gates/gates/isp_checker.py tetrapoder
python3 gates/gates/limits_checker.py tetrapoder
python3 gates/gates/srp_checker.py tetrapoder

echo "Done"
