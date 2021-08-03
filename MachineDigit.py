"""
  @FileName   : MachineDigit.py
  @Abstract   : 真值数、机器数（原码、反码、补码）之间互相转换（仅限1个字节即8个位的范围）
  @Create Date: 2021-8-3 13:10
  @Version    : v0.1.3
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


def truth2sc(truth: int) -> int:
    """
    根据真值数计算对应的原码（只限1字节即8位）
    长度范围的处理在Gui上解决
    :param truth:   真值数
    :return:        返回原码（int形式）
    """
    truth_abs = abs(truth)  # 获取真值数的绝对值
    if truth < 0:  # 如果是负数
        return truth_abs | 0b10000000  # 在第8位加上1
    else:  # 如果为0或正数，返回本身
        return truth


def sc2truth(sc: int) -> int:
    #     """
    #     根据原码计算真值数（只限1字节即8位）
    #     :param sc:  原码
    #     :return:    真值数
    #     """
    flag = sc & 0b10000000  # 获取标志位
    if flag == 0b10000000:  # 如果最高位是1（负数）
        value = sc & 0b01111111  # 获取数值
        return -value
    else:  # 如果是正数
        return sc


def sc2ic(sc: int) -> int:
    """
    根据原码计算反码（只限1字节即8位）
    :param sc:  原码
    :return:    返回对应的反码
    """
    flag = sc & 0b10000000  # 获取标志位
    if flag == 0b10000000:  # 如果最高位是1（负数）
        return sc ^ 0b01111111  # 除标志位，其余取反
    else:  # 如果是正数
        return sc


def ic2sc(cc: int) -> int:
    """
    根据反码计算原码（只限1字节即8位）
    :param cc:  反码
    :return:    返回对应的原码
    """
    return sc2ic(cc)  # 过程和原码-->反码是一样的，所以套个壳一样用


def ic2cc(ic: int) -> int:
    """
    根据反码计算补码（只限1字节即8位）
    :param ic:  反码
    :return:    返回对应的补码
    """
    flag = ic & 0b10000000  # 获取标志位
    if flag == 0b10000000:  # 如果最高位是1（负数）
        value = ic & 0b01111111  # 获取数值
        value_plus = (value + 1) & 0b1111111  # 给低7位+1，并只取7位，高于7位的内容丢弃
        return value_plus | 0b10000000  # 给最第8位设为1
    else:  # 如果是正数
        return ic


def cc2ic(cc: int) -> int:
    """
    根据补码计算反码（只限1字节即8位）
    :param cc:  补码
    :return:    返回对应的反码
    """
    flag = cc & 0b10000000  # 获取标志位
    if flag == 0b10000000:  # 如果最高位是1（负数）
        value = cc & 0b01111111  # 获取数值
        value_plus = value - 1
        return value_plus | 0b10000000  # 给最第8位设为1
    else:  # 如果是正数
        return cc
