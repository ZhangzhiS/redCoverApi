#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
小程序项目相关的模型
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean

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
    cover_id = Column(Integer, comment="封面id")
    created_at = Column(DateTime, default=datetime.now, comment="邀请时间")


class Coupon(Base):
    """cps"""
    id = Column(Integer, primary_key=True)
    app_id = Column(Integer, comment="系统中小程序的id", index=True)
    border = Column(String, comment="便条")
    desc = Column(String, comment="描述")
    icon = Column(String, comment="icon")
    appid = Column(String, comment="需要跳转的小程序的appid")
    path = Column(String, comment="跳转小程序的路径")
    name = Column(String, comment="cps名称")
    platform = Column(String, comment="平台")
    sort = Column(Integer, comment="排序位置")
    tip = Column(String, comment="提示")


class MiniAppTip(Base):
    """提示"""
    id = Column(Integer, primary_key=True)
    app_id = Column(Integer, comment="系统中小程序的id", index=True)
    tip = Column(String, comment="提示")
    page = Column(String, comment="提示所在的页面")
    item_id = Column(Integer, comment="页面项目id")
    created_at = Column(DateTime, default=datetime.now, comment="邀请时间")


class MiniAppAd(Base):
    """小程序广告配置"""
    id = Column(Integer, primary_key=True)
    app_id = Column(Integer, comment="系统中小程序的id", index=True)
    ad_id = Column(String, comment="申请到的广告id")


class RedCover(Base):
    """红包封面"""
    id = Column(Integer, primary_key=True)
    app_id = Column(Integer, comment="系统中小程序的id", index=True)
    receive_desc = Column(String, comment="领取提示")
    invite_limit = Column(Integer, comment="领取的时候邀请用户的限制")
    is_free = Column(Boolean, comment="是否免费")
    ad_limit = Column(Integer, comment="领取是观看广告数的限制")
    pic = Column(String, comment="封面预览图")
    is_task_together = Column(Boolean, comment="是否需要同时完成两个任务")
    is_in_stock = Column(Boolean, comment="活动是否还在进行")
    notice_show = Column(Boolean, comment="是否展示通知")


class AdHistory(Base):
    id = Column(Integer, primary_key=True)
    app_id = Column(Integer, comment="系统中小程序的id", index=True)
    openid = Column(String, comment="用户的openid")
    status = Column(Boolean, comment="本次观看广告是否有效")
    cover_id = Column(Integer, comment="红包封面id")
    created_at = Column(DateTime, default=datetime.now, comment="创建时间")


class RedCoverReceived(Base):
    """红包封面领取记录"""
    id = Column(Integer, primary_key=True)
    app_id = Column(Integer, comment="系统中小程序的id", index=True)
    openid = Column(String, comment="用户的openid")
    cover_id = Column(Integer, comment="红包封面的id")
    red_cover_serial = Column(String, comment="使用的序列号")
    created_at = Column(DateTime, default=datetime.now)


class RedCoverSerial(Base):
    """红包封面序列号"""
    id = Column(Integer, primary_key=True)
    app_id = Column(Integer, comment="系统中小程序的id", index=True)
    cover_id = Column(Integer, comment="红包封面的id")
    red_cover_serial = Column(String, comment="封面序列号")
    status = Column(Boolean, default=True, comment="序列号状态，False表示被人领取了")
    created_at = Column(DateTime, default=datetime.now)

