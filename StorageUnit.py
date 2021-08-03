"""
  @FileName   : StorageUnit.py
  @Abstract   : 存储单位的转换
  @Create Date: 2021-8-1 14:19
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


def convert(source_num: float, source_unit: str, target_unit: str) -> float:
    """
    各种存储单位之间的转换
    :param source_num:  要转换的数值
    :param source_unit: 要转换的单位
    :param target_unit:    转换后的单位
    :return             转换后的数值
    """

    unit_dict = {'b': 0, 'B': 1, 'KB': 2, 'MB': 3, 'GB': 4, 'TB': 5, 'PB': 6, 'EB': 7, 'ZB': 8,
                 'YB': 9, 'NB': 10, 'DB': 11}  # 设置字典，用于后面判断单位的大小

    source_unit_id = unit_dict[source_unit]  # 获取源单位的索引值
    target_unit_id = unit_dict[target_unit]  # 获取新单位的索引值
    unit_diff = abs(target_unit_id - source_unit_id)  # 计算单位之间的级数差

    # 如果 单位 小-->大
    if source_unit_id < target_unit_id:
        if source_unit == 'b':  # 如果由 b 开始转换（要考虑b与B之间的8倍关系）
            if target_unit == 'B':
                target_unit_num = source_num / 8
            else:
                target_unit_num = source_num / 8 / pow(1024, unit_diff - 1)  # 将b-->B的过程单独提炼出来，然后进行剩下的计算 source/8/1024^n
        else:  # 如果不是由 b 开始转换（无需考虑b与B之间的8倍关系）
            target_unit_num = source_num / pow(1024, unit_diff)

    # 如果 单位 大-->小
    elif source_unit_id > target_unit_id:
        if target_unit == 'b':  # 如果最终单位为b（要考虑b与B之间的8倍关系）
            if source_unit == 'B':
                target_unit_num = source_num * 8
            else:
                target_unit_num = source_num * pow(1024, unit_diff - 1) * 8
        else:  # 无需考虑b与B之间的8倍关系
            target_unit_num = source_num * pow(1024, unit_diff)

    # 如果一样（即不变）
    else:
        return source_num  # 直接返回源数据

    return target_unit_num

# print(convert(1, 'TB', 'b'))
# print(convert(1, 'TB', 'B'))
# print(convert(1, 'TB', 'KB'))
# print(convert(1, 'TB', 'MB'))
# print(convert(1, 'TB', 'GB'))
# print(convert(1, 'TB', 'TB'))
# print(convert(1, 'TB', 'PB'))
# print(convert(1, 'TB', 'EB'))
# print(convert(1, 'TB', 'ZB'))
# print(convert(1, 'TB', 'YB'))
# print(convert(1, 'TB', 'NB'))
# print(convert(1, 'TB', 'DB'))
