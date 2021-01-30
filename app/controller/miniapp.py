#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
小程序相关的接口操作
"""
import requests

from app import crud
from app.schemas import MiniAppUserCreate


def get_user_info(app_id: int, code: str, db):
    """
    从微信服务器获取用户信息
    :param db: 数据库连接
    :param app_id: 小程序id
    :param code: 前端传的code
    :return: 返回用户信息
    """
    config = crud.mini_app_config.get(db, app_id)
    print(config)
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
