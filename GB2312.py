"""
  @FileName   : GB2312.py
  @Abstract   : 国标码、区位码、机内码之间互相转换
  @Create Date: 2021-8-2 21:00
  @Version    : v0.1.1
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


def calc_machine_by_gb(gb: int) -> str:
    """
    由国标码计算机内码
    :param gb:  国标码（十六进制）
    :return:    机内码（十进制）
    """
    return str(hex(gb + 32896))[2:].upper()


def calc_gb_by_qw(qw: int) -> str:
    """
    由区位码计算国标码
    :param qw:  区位码（十进制）
    :return:    国标码（16进制的字符串）
    """
    qw_high = int(str(qw)[0:2])
    qw_low = int(str(qw)[2:4])
    gb_high = qw_high + 32
    gb_low = qw_low + 32
    gb_str = str(hex(gb_high)[2:]) + str(hex(gb_low)[2:])
    return gb_str.upper()


def calc_machine_by_qw(qw: int) -> str:
    """
    由区位码计算国标码
    :param qw:  区位码（十进制）
    :return:    机内码（16进制的字符串）
    """
    qw_high = int(str(qw)[0:2])
    qw_low = int(str(qw)[2:4])
    machine_high = qw_high + 160
    machine_low = qw_low + 160
    machine_str = str(hex(machine_high)[2:]) + str(hex(machine_low)[2:])
    return machine_str.upper()


def calc_compare_chz(chz1: str, chz2: str) -> int:
    """
    比较汉字顺序
    :param chz1:    汉字1（也可以词）
    :param chz2:    汉字2（也可以词）
    :return:        汉字1 > 汉字2 - 1; 汉字1 < 汉字2 - 2; 汉字1 = 汉字2 - 0;
                    汉字越大，说明越排后面
    """
    if chz1 > chz2:
        return 1
    elif chz1 < chz2:
        return 2
    else:
        return 0

# print(calc_compare_chz('教授', '教师'))
