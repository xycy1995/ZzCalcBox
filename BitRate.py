"""
  @FileName   : BitRate.py
  @Abstract   : 计算比特率为字节形式
  @Create Date: 2021-8-2 16:30
  @Version    : v0.0.2
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


def calc_bit2byte(source_num: int, source_unit: str, target_unit: str) -> float:
    """
    将bps转为Bps
    核心思想：b与B之间差8倍，b与Kb之间差1024倍
    :param source_num:  原数值
    :param source_unit: 原数值的单位 bps / Kbps / Mbps / Gbps
    :param target_unit: 目标单位    B/s / KB/s / MB/s / GB/s
    :return:            常用的字节形式的传输速率
    """

    ret_byte = 0.00

    if source_unit == 'bps':
        if target_unit == 'B/s':
            ret_byte = source_num / 8
        elif target_unit == 'KB/s':
            ret_byte = source_num / 8 / 1024
        elif target_unit == 'MB/s':
            ret_byte = source_num / 8 / 1024 / 1024
        elif target_unit == 'GB/s':
            ret_byte = source_num / 8 / 1024 / 1024 / 1024
        return ret_byte
    elif source_unit == 'Kbps':
        if target_unit == 'B/s':
            ret_byte = source_num * 1024 / 8
        elif target_unit == 'KB/s':
            ret_byte = source_num * 1024 / 8 / 1024
        elif target_unit == 'MB/s':
            ret_byte = source_num * 1024 / 8 / 1024 / 1024
        elif target_unit == 'GB/s':
            ret_byte = source_num * 1024 / 8 / 1024 / 1024 / 1024
        return ret_byte
    elif source_unit == 'Mbps':
        if target_unit == 'B/s':
            ret_byte = source_num * 1024 * 1024 / 8
        elif target_unit == 'KB/s':
            ret_byte = source_num * 1024 * 1024 / 8 / 1024
        elif target_unit == 'MB/s':
            ret_byte = source_num * 1024 * 1024 / 8 / 1024 / 1024
        elif target_unit == 'GB/s':
            ret_byte = source_num * 1024 * 1024 / 8 / 1024 / 1024 / 1024
        return ret_byte
    elif source_unit == 'Gbps':
        if target_unit == 'B/s':
            ret_byte = source_num * 1024 * 1024 * 1024 / 8
        elif target_unit == 'KB/s':
            ret_byte = source_num * 1024 * 1024 * 1024 / 8 / 1024
        elif target_unit == 'MB/s':
            ret_byte = source_num * 1024 * 1024 * 1024 / 8 / 1024 / 1024
        elif target_unit == 'GB/s':
            ret_byte = source_num * 1024 * 1024 * 1024 / 8 / 1024 / 1024 / 1024
        return ret_byte

# print(calc_bit2byte(115200, 'Mbps', 'KB/s'))
