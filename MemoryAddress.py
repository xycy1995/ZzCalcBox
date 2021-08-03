"""
  @FileName   : MemoryAddress.py
  @Abstract   : 内存地址得计算
  @Create Date: 2021-8-1 09:55
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


def calc_by_bus(num: int) -> int:
    """
    根据地址线的数量，求容量
    :param num: 地址线的数量
    :return:    容量，单位为Byte
    """
    if num == 0:  # 如果地址线为0时，返回0，不然变成【2^0=1】就有问题了
        return 0
    else:
        return pow(2, num)


def calc_by_address(address_start: str, address_end: str) -> int:
    """
    根据首末地址，求容量
    :param address_start:   首地址
    :param address_end:     末地址
    :return:                容量，单位为Byte
    """
    if int(address_end, base=16) == int(address_start, base=16):  # 如果首地址=末地址
        return 0
    elif int(address_end, base=16) > int(address_start, base=16):  # 如果首地址小于末地址
        return int(address_end, base=16) - int(address_start, base=16) + 1
    else:  # 如果首地址大于末地址
        return -1  # 返回-1表示出错


def calc_address_start(num: int, address_end: str) -> str:
    """
    已知内存容量和末地址，求得首地址
    :param num:         内存容量（Byte）
    :param address_end: 末地址
    :return:            首地址（十六进制形式）
    """
    if num == 0:
        return address_end
    else:
        return str(hex(int(address_end, base=16) - num + 1)[2:]).upper()


def calc_address_end(num: int, address_start: str) -> str:
    """
    已知内存容量和首地址，求得末地址
    :param num:             内存容量（Byte）
    :param address_start:   首地址
    :return:                末地址（十六进制形式）
    """
    if num == 0:
        return address_start
    else:
        return str(hex(num + int(address_start, base=16) - 1)[2:]).upper()

# print(calc_by_address('1000', '4FFF'))
# print(calc_address_start(16384, '7FFF'))
# print(calc_address_end(32768,'0000'))
