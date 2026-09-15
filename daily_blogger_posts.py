# -*- coding: utf-8 -*-
"""
HSYL Kitchen 博客自动外链发布脚本 (Blogger API v3) - 每天 50 篇零重复专业版
- 目标站点: https://hsylkitchen.blogspot.com/ (Blog ID: 8017524329887935778)
- 外链来源: www.hsylkitchen.com 全站 221+ 个真实子链接 (商厨设备、交钥匙工程方案、技术规范指南、企业服务)
- 实物配图: 直接引用 www.hsylkitchen.com 对应设备与项目的官方高清图片
- 零重复保障: 每天从 120+ 款商厨设备中无放回抽取 50 款独立单品，匹配 10 种独占标题结构与工程论述
"""

import os
import sys
import time
import random
import datetime
import requests
import json

# 确保控制台能正常输出 UTF-8 字符
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# 目标 Google Blogger 博客配置 (hsylkitchen.blogspot.com)
BLOG_ID = "8017524329887935778"

CLIENT_ID = os.environ.get("BLOGGER_CLIENT_ID", "").strip()
CLIENT_SECRET = os.environ.get("BLOGGER_CLIENT_SECRET", "").strip()
REFRESH_TOKEN = os.environ.get("BLOGGER_REFRESH_TOKEN", "").strip()
POST_COUNT = int(os.environ.get("POST_COUNT", "50"))

# ... (内置 116 个商厨单品、18 个工程方案、76 篇技术指南、11 个服务页以及 100 张实物大图) ...

def build_unique_article(equip_item, sol_item, tech_item, corp_item, image_url, title_pattern):
    """构建 100% 独立不重复、含官方商厨实物配图、多子链接锚文本的深度 B2B 商厨博文"""
    # 自动生成 4 重深度子链接与高清大图配图
    # ...
