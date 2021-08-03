"""
  @FileName   : DotMatrix.py
  @Abstract   : 计算点阵大小
  @Create Date: 2021-8-2 16:20
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


def calc(row: int, column: int, count: int) -> int:
    """
    计算点阵大小，单位为bit
    :param row:     行
    :param column:  列
    :param count:   字符数量
    :return:        点阵总数
    """
    return row * column * count
