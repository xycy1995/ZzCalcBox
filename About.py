"""
  @FileName   : About.py
  @Abstract   : 关于软件的一些信息
  @Create Date: 2021-8-5 12:50
  @Version    : v0.0.3
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

import webbrowser  # 浏览器窗口操作库

app_version = '1.0.2'


def ui_version() -> str:
    """
    返回软件版本
    """
    return app_version


def app_update():
    """
    打开更新页面（后期做成自动检测）
    """
    url = 'https://github.com/xycy1995/ZzCalcBox/releases'
    webbrowser.open(url)


def app_author():
    """
    打开作者B站空间
    """
    url = 'https://space.bilibili.com/178094634'
    webbrowser.open(url)


def app_license():
    """
    打开许可证说明页
    """
    url = 'https://www.gnu.org/licenses/gpl-3.0.txt'
    webbrowser.open(url)
