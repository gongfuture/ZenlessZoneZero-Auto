# -*- coding: utf-8 -*-
"""
@file:      readme_group
@time:      2024/9/2 12:16
@author:    sMythicalBird
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontMetrics
from PySide6.QtWidgets import QFrame


class BaseGroup(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.vBoxLayout = QVBoxLayout(self)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.vBoxLayout.setSpacing(0)

        self.vBoxLayout.addSpacing(12)


class AutoAdjustTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.textChanged.connect(self.adjust_edit_height)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjust_edit_height()

    def adjust_edit_height(self):
        font_metrics = QFontMetrics(self.font())
        text = self.toPlainText()
        line_spacing = font_metrics.lineSpacing()
        text_edit_width = self.viewport().width()
        line_count = 0
        for line in text.split("\n"):
            line_count += (font_metrics.horizontalAdvance(line) // text_edit_width) + 1
        line_height = font_metrics.lineSpacing()
        self.setFixedHeight(line_count * (line_height + 3) + 2)


class ReadmeCard(QWidget):
    def __init__(self, title: str):
        super().__init__()
        self.area = QWidget()
        self.title_label = QLabel(title)
        self.text_edit = AutoAdjustTextEdit()
        self.v_layout = QVBoxLayout(self.area)
        self.init_ui()

    def init_ui(self):
        # 设置标签字体字号和加粗
        label_font = QFont()
        label_font.setPointSize(12)  # 设置字号
        label_font.setBold(True)  # 设置加粗
        self.title_label.setFont(label_font)
        self.adjust_label_width(label_font)

        lay1 = QVBoxLayout()
        lay1.addWidget(self.title_label)
        lay1.setContentsMargins(10, 0, 0, 0)

        lay2 = QVBoxLayout()
        lay2.addWidget(self.text_edit)
        self.v_layout.addLayout(lay1)
        self.v_layout.addLayout(lay2)

        self.text_edit.setFrameShape(QFrame.Shape.NoFrame)
        self.text_edit.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )  # 禁用垂直滚动条
        self.text_edit.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )  # 禁用水平滚动条

        # 设置内边距和外边距
        self.v_layout.setContentsMargins(5, 5, 5, 5)  # 左, 上, 右, 下
        self.v_layout.setSpacing(5)  # 控件之间的间距

        self.area.setStyleSheet(
            """
            background-color: lightgray;
            border-radius: 5px;
            """
        )

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.area.setFixedHeight(
            self.text_edit.height() + self.title_label.height() + 20
        )

    # 调整标签宽度以适应文本
    def adjust_label_width(self, font):
        font_metrics = QFontMetrics(font)
        text_width = font_metrics.horizontalAdvance(self.title_label.text())
        self.title_label.setFixedWidth(text_width)


class ReadmeGroup(BaseGroup):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.prj_edit_card = ReadmeCard(self.tr("项目说明"))
        self.setting_edit_card = ReadmeCard(self.tr("配置说明"))
        self.previous_width = self.width()
        self.init_ui()
        self.init_layout()

    def init_ui(self):
        prj_edit_edit = self.prj_edit_card.text_edit
        prj_edit_edit.setReadOnly(True)
        prj_edit_edit.setPlainText(
            "本项目基于Python3.10进行开发，使用图像分类、模板匹配、OCR识别进行零号空洞自动寻路和相关事件处理\n"
            "！！！本项目开源免费，如果您遇到任何收费情况都属于被他人欺骗，请勿上当！！！\n"
            "本软件开源、免费，仅供学习交流使用，禁止用于商业用途。使用本软件产生的所有问题与本项目与开发者无关。若您遇到商家使用本软件进行代练并收费，可能是设备与时间等费用，产生的问题及后果与本软件无关。"
        )
        setting_edit_edit = self.setting_edit_card.text_edit
        setting_edit_edit.setReadOnly(True)
        setting_edit_edit.setPlainText(
            "1. 设置->输入->棋盘镜头移动速度->1\n"
            "2. 设置->画面->显示模式->1280*720窗口\n"
            "3. 设置->键鼠设置->角色切换下一位->Space(战斗场景下的切人按键必须是Space)\n"
            "4. 脚本运行会占用键盘鼠标，在使用时不要操作键盘鼠标\n"
            "5. 脚本运行前游戏界面置于零号空洞副本选择界面\n"
            "6. 帧率设置为60帧，刷`拿命验收`的时候必须是60帧，否则会出现问题\n"
            "7. 显示屏防蓝光关闭，HDR也要关闭，否则影响截图做模板匹配\n"
            "8. 显示屏缩放比例设置为100%(4k屏自己测试一下不同缩放情况，一般150/250缩放比较合适)\n"
            "9. 目前脚本只支持游戏语言设置为简中，暂未对其他语言进行适配\n"
            "10. 游戏字体设置为细体"
        )

    # def resizeEvent(self, event):
    #     super().resizeEvent(event)
    #     current_width = self.width()
    #     if current_width != self.previous_width:
    #         self.previous_width = current_width
    #         self.adjust_height()

    def init_layout(self):
        self.vBoxLayout.setSpacing(10)
        self.vBoxLayout.addWidget(self.prj_edit_card.area)
        self.vBoxLayout.addWidget(self.setting_edit_card.area)

    # def adjust_height(self):
    #     total_height = (
    #         self.prj_edit_card.area.height()
    #         + self.setting_edit_card.area.height()
    #         + self.titleLabel.height()
    #         + 20  # 额外的间距
    #     )
    #     print(total_height)
    #     self.setFixedHeight(total_height)
