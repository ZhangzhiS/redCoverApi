#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
小程序项目相关的模型
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.db.base_class import Base


class MiniAppConfig(Base):
    """小程序配置"""
    id = Column(Integer, primary_key=True, index=True)
    appid = Column(String, comment="微信小程序appid")
    app_secret = Column(String, comment="微信小程序app_secret")
    author = Column(String, comment="小程序作者")
    remarks = Column(String, comment="备注")


class MiniAppUser(Base):
    """小程序用户信息"""
    id = Column(Integer, primary_key=True)
    app_id = Column(Integer, comment="系统中小程序的id", index=True)
    openid = Column(String, comment="微信用户在此小程序中的openid")
    session_key = Column(String, comment="用户的session_key")
    created_at = Column(DateTime, default=datetime.now, comment="注册时间")


class InviteUser(Base):
    """用户邀请关系表"""
    id = Column(Integer, primary_key=True)
    app_id = Column(Integer, comment="系统中小程序的id", index=True)
    openid = Column(String, comment="用户的openid")
    invite_openid = Column(String, comment="被邀请的用户的openid")
    created_at = Column(DateTime, default=datetime.now, comment="邀请时间")
