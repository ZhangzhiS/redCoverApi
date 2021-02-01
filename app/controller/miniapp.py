#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
小程序相关的接口操作
"""
from typing import Any, Optional

import requests

from app import crud
from app.schemas import MiniAppUserCreate, MiniAppInviteUserCreate, WxAdCreate


def get_user_info(app_id: int, code: str, db):
    """
    从微信服务器获取用户信息
    :param db: 数据库连接
    :param app_id: 小程序id
    :param code: 前端传的code
    :return: 返回用户信息
    """
    config = crud.mini_app_config.get(db, app_id)
    result = requests.get(
        url="https://api.weixin.qq.com/sns/jscode2session",
        params={
            "appid": config.appid,
            "secret": config.app_secret,
            "js_code": code,
            "grant_type": "authorization_code"
        },
    ).json()
    # return result
    openid = result.get("openid")
    user = crud.mini_app_user.get_by_openid(db, openid)
    if user:
        return user
    return crud.mini_app_user.create(
        db, obj_in=MiniAppUserCreate(
            app_id=config.id,
            openid=openid,
            session_key="t",
        )
    )


def track_invite_user(app_id: int, openid: str, invite_openid: str, db: Any):
    """
    邀请新用户的逻辑
    :param app_id:
    :param openid:
    :param invite_openid:
    :param db:
    :return: 返回邀请之后的数据
    """
    invite_user = crud.mini_app_invite.check_invite(
        db, app_id, invite_openid
    )
    if invite_user:
        return invite_user
    return crud.mini_app_invite.create(
        db,
        obj_in=MiniAppInviteUserCreate(
            app_id=app_id,
            openid=openid,
            invite_openid=invite_openid
        )
    )


def get_cps_list(app_id: int, db: Any):
    """获取cps列表"""
    return crud.cps.get_cps_list_by_app_id(db, app_id)


def get_covers(app_id: int, db: Any):
    """获取红包封面列表"""
    return crud.red_cover.get_cover_list_by_app_id(db, app_id)


def get_tips(app_id: int, db: Any, page: Optional[str], item_id: Optional[int]):
    """获取首页的通知"""
    return crud.tip.get_tips_list(db, app_id, page, item_id)


def get_cover_detail(cover_id: int, openid: str, app_id: int, db: Any):
    """获取封面详情"""
    cover = crud.red_cover.get(db, cover_id)
    if not cover:
        return {}
    look_ad_count = crud.wx_ad.get_look_history_count(db, app_id, cover_id, openid)
    invite_count = crud.mini_app_invite.get_invite_count(db, openid, app_id, cover_id)
    tips = crud.tip.get_tips_list(db, app_id, page="cover_detail", item_id=cover_id)
    is_task_success = False
    result = {
        "cover_detail": cover,
        "look_ad_count": look_ad_count,
        "invite_count": invite_count,
        "tips": [i.tip for i in tips],
        "receive_data": cover.receive_desc if cover.is_free else f"领取封面-{cover.id}-{openid}",
        "ad_config": {
            "one": "",
            "two": "",
            "three": "",
            "four": "",
            "five": ""
        }
    }
    if cover.is_free:
        result["is_task_success"] = is_task_success
        return result
    if cover.is_task_together:
        if look_ad_count >= cover.ad_limit and invite_count >= cover.invite_limit:
            is_task_success = True
    else:
        if look_ad_count >= cover.ad_limit or invite_count >= cover.invite_limit:
            is_task_success = True
    result["is_task_success"] = is_task_success
    return result


def track_ad_history(
        app_id: int, openid: str, cover_id: int, status: bool, db: Any
):
    result = crud.wx_ad.create(
        db,
        obj_in=WxAdCreate(
            app_id=app_id,
            openid=openid,
            cover_id=cover_id,
            status=status,
        )
    )
    return result
