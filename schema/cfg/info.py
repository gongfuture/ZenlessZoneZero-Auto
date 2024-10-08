# -*- coding: utf-8 -*-
"""
@file:      info
@time:      2024/8/21 01:00
@author:    sMythicalBird
"""

from .zero_info import ZeroConfig
from .fight_info import FightConfig
from .load import load_config, get_fight_logic, load_tactics

zero_cfg = load_config("zero.yaml", ZeroConfig)  # 零号空洞配置信息
fight_cfg = load_config("fight.yaml", FightConfig)  # 战斗配置信息

# 战斗逻辑读取
fight_logic_all = get_fight_logic()  # 角色战斗逻辑存储位置列表
fight_logic_zero = load_tactics(
    fight_cfg.zero_fight, fight_logic_all
)  # 零号空洞战斗读取
fight__logic_daily = load_tactics(
    fight_cfg.daily_fight, fight_logic_all
)  # 日常战斗读取


# 选择项列表
buff_list = [
    "以太",
    "冻结",
    "暴击",
    "引燃",
    "感电",
    "能量",
    "强袭",
    "支援",
    "决斗",
    "护盾",
    "协助",
    "通用",
    "闪避",
    "研究",
    "邦布",
    "空洞",
    "诡术",
    "契合",
]

char_list = [
    "青衣",
    "朱鸢",
    "艾莲",
    "莱卡恩",
    "猫又",
    "11号",
    "丽娜",
    "珂蕾妲",
    "格莉丝",
    "露西",
    "派派",
    "妮可",
    "比利",
    "本",
    "苍角",
    "安比",
    "可琳",
    "安东",
]
