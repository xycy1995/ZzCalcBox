"""
  @FileName   : ParityCheck.py
  @Abstract   : 奇偶校验码计算
  @Create Date: 2021-8-3 17:00
  @Version    : v0.1.2
  @Author     : 斜影重阳xycy
  @Contact    : https://space.bilibili.com/178094634
  @License    : GNU General Public License, version 3 (GPL-3.0)

  Copyright (C)2021 斜影重阳xycy.

  This dll is open source: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This dll is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.If not, see < https://www.gnu.org/licenses/>.
"""


def calc_check(code: str, code_type: str) -> bool:
    """
    检查类型的正确与否
    :param code:        数值（7位）
    :param code_type:   Odd - 奇校验     Even - 偶校验
    :return:            数值与校验匹配 - True  不匹配 - False
    """
    if len(code) == 8:
        count = 0
        i = 0
        while i < 8:
            if code[i] == '1':
                count += 1
            i += 1

        if code_type == 'Odd':  # 如果为奇校验
            if count % 2 == 0:  # 如果能除尽，说明是偶数个1
                return False
            else:
                return True
        elif code_type == 'Even':  # 如果为偶校验
            if count % 2 == 0:
                return True
            else:
                return False


def calc_type(code: str) -> str:
    """
    判断数值使用的校验类型
    :param code:    校验位+数值（8位）
    :return:        Odd - 奇校验     Even - 偶校验
    """
    if len(code) == 8:
        count = 0
        i = 0
        while i < 8:
            if code[i] == '1':
                count += 1
            i += 1

        if count % 2 == 0:
            return 'Even'
        else:
            return 'Odd'


def calc_flag(code_value: str, code_type: str) -> int:
    """
    计算数值的校验位
    :param code_value:  数值（7位）
    :param code_type:   Odd - 奇校验     Even - 偶校验
    :return:            返回校验位0/1
    """
    if len(code_value) == 7:
        count = 0
        i = 0
        while i < 7:
            if code_value[i] == '1':
                count += 1
            i += 1

        if code_type == 'Even':
            if count % 2 == 0:
                return 0
            else:
                return 1
        elif code_type == 'Odd':
            if count % 2 == 0:
                return 1
            else:
                return 0
