"""
  @FileName   : Ascii.py
  @Abstract   : 计算ASCII对于的十进制值
  @Create Date: 2021-8-2 21:14
  @Version    : v0.1.0
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


def calc(character: str) -> int:
    """
    计算对应的十进制值
    :param character:   字符
    :return:            对应的十进制值
    """
    return ord(character)


def compare(character1: str, character2: str) -> int:
    """
    比较ASCII码的先后顺序
    :param character1:  字符1（也可以词）
    :param character2:  字符2（也可以词）
    :return:            字符1 > 字符2 - 1; 字符1 < 字符2 - 2; 字符1 = 字符2 - 0;
                        字符越大，说明越排后面
    """
    if character1 > character2:
        return 1
    elif character1 < character2:
        return 2
    else:
        return 0

# print(compare('A1','A2'))
