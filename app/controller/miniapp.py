#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
小程序相关的接口操作
"""
from typing import Any

import requests

from app import crud
from app.schemas import MiniAppUserCreate, MiniAppInviteUserCreate


def get_user_info(app_id: int, code: str, db):
    """
    从微信服务器获取用户信息
    :param db: 数据库连接
    :param app_id: 小程序id
    :param code: 前端传的code
    :return: 返回用户信息
    """
    config = crud.mini_app_config.get(db, app_id)
    print(code)
    # result = requests.get(
    #     url="https://api.weixin.qq.com/sns/jscode2session",
    #     params={
    #         "appid": config.appid,
    #         "app_secret": config.app_secret,
    #         "js_code": code,
    #         "grant_type": "authorization_code"
    #     },
    # ).json()
    # return result
    openid = "t"
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
        db, app_id, openid, invite_openid
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
