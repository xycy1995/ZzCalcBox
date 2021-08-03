"""
  @FileName   : Image.py
  @Abstract   : 计算图片文件的大小
  @Create Date: 2021-8-2 15:20
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


def calc(pix_h: int, pix_v: int, depth: int) -> int:
    """
    计算图片的容量（bit）
    :param pix_h:   水平像素的数量
    :param pix_v:   垂直像素的数量
    :param depth:   颜色深度
    :return:        返回容量大小（bit）
    """
    return pix_h * pix_v * depth
