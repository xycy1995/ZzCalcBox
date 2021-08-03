"""
  @FileName   : Audio.py
  @Abstract   : 计算音频文件的大小
  @Create Date: 2021-8-2 12:39
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


def calc(hz: int, bit: int, channel: int, second: int) -> int:
    """
    计算音频文件的大小（bit）
    :param hz:      声音频率（Hz）
    :param bit:     声音位数
    :param channel: 声道数
    :param second:  秒数
    :return:        返回容量大小（bit）
    """
    return hz * bit * channel * second
