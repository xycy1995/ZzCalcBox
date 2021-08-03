"""
  @FileName   : Radix.py
  @Abstract   : 进制的转换，支持常用进制之间的转换
  @Create Date: 2021-8-1 15:10
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


def convert(source_num: str, source_type: str, target_radix: str) -> str:
    """
    二、八、十、十六进制之间的转换
    核心思想：先手动转为十进制，再自动转为对应进制
    :param source_num:      要转换数据的值
    :param source_type:     要转换数据的进制（BIN/OCT/DEC/HEX）
    :param target_radix:    转换后（目标）的进制（BIN/OCT/DEC/HEX）
    :return:                转换后的数据值
    """
    if source_type == 'BIN':  # 如果源数据为BIN
        if target_radix == 'BIN':  # 如果目标进制为BIN(其实用不到)
            return source_num  # 直接返回输入值
        else:  # 否则要进行计算转换为DEC
            source_num_dec = int(source_num, base=2)  # BIN --> DEC
            if source_num_dec > 0:  # 如果源数据为正数
                if target_radix == 'OCT':  # 如果目标进制为OCT
                    return str((oct(source_num_dec))[2:])  # 截取重要部分
                elif target_radix == 'DEC':  # 如果目标进制为DEC
                    return str(source_num_dec)  # 直接返回计算结果
                elif target_radix == 'HEX':  # 如果目标进制为HEX
                    return str((hex(source_num_dec)[2:])).upper()  # 截取重要部分，并转为大写形式
            else:  # 如果源数据为负数，转换后长度就不一样，需要修改，并手动加上'-'
                if target_radix == 'OCT':  # 如果目标进制为OCT
                    return '-' + str((oct(source_num_dec))[3:])  # 截取重要部分
                elif target_radix == 'DEC':  # 如果目标进制为DEC
                    return str(source_num_dec)  # 直接返回计算结果
                elif target_radix == 'HEX':  # 如果目标进制为HEX
                    return '-' + str((hex(source_num_dec)[3:])).upper()  # 截取重要部分，并转为大写形式

    elif source_type == 'OCT':  # 如果源数据为OCT
        if target_radix == 'OCT':
            return source_num
        else:
            source_num_dec = int(source_num, base=8)
            if source_num_dec > 0:
                if target_radix == 'BIN':
                    return str((bin(source_num_dec))[2:])
                elif target_radix == 'DEC':
                    return str(source_num_dec)
                elif target_radix == 'HEX':
                    return str((hex(source_num_dec)[2:])).upper()
            else:
                if target_radix == 'BIN':
                    return '-' + str((bin(source_num_dec))[3:])
                elif target_radix == 'DEC':
                    return str(source_num_dec)
                elif target_radix == 'HEX':
                    return '-' + str((hex(source_num_dec)[3:])).upper()

    elif source_type == 'DEC':  # 如果源数据为DEC
        if target_radix == 'DEC':
            return source_num
        else:
            source_num_dec = int(source_num, base=10)  # 直接使用即可
            if source_num_dec > 0:
                if target_radix == 'BIN':
                    return str((bin(source_num_dec))[2:])
                elif target_radix == 'OCT':
                    return str((oct(source_num_dec))[2:])
                elif target_radix == 'HEX':
                    return str((hex(source_num_dec)[2:])).upper()
            else:
                if target_radix == 'BIN':
                    return '-' + str((bin(source_num_dec))[3:])
                elif target_radix == 'OCT':
                    return '-' + str((oct(source_num_dec))[3:])
                elif target_radix == 'HEX':
                    return '-' + str((hex(source_num_dec)[3:])).upper()

    elif source_type == 'HEX':  # 如果源数据为OCT
        if target_radix == 'HEX':
            return source_num
        else:
            source_num_hex = int(source_num, base=16)
            if source_num_hex > 0:
                if target_radix == 'BIN':
                    return str((bin(source_num_hex))[2:])
                elif target_radix == 'OCT':
                    return str((oct(source_num_hex))[2:])
                elif target_radix == 'DEC':
                    return str(int(source_num_hex))
            else:
                if target_radix == 'BIN':
                    return '-' + str((bin(source_num_hex))[3:])
                elif target_radix == 'OCT':
                    return '-' + str((oct(source_num_hex))[3:])
                elif target_radix == 'DEC':
                    return str(int(source_num_hex))

# print(convert('123', 'OCT', 'BIN'))
