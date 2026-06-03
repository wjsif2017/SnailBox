"""
Flipbook 模块导入

本模块使用前后端分离架构:

后端数据类 (fb_item.py):
    Fb_Manager - Flipbook 管理器
    Item_Text - 文字项数据模型
    State_Text - Viewport 文字绘制
    State - Viewport 状态管理

前端 UI 类 (fb_ui.py):
    Ui_Main - 主界面布局
    ItemTextWidget - 文字项 UI 组件
"""

# 后端数据类导入
from .fb_item import Fb_Manager, Item_Text, State_Text, State

# 前端 UI 类导入
from .fb_ui import Ui_Main, ItemTextWidget
