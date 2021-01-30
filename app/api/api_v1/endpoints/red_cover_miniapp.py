#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
红包封面小程序接口
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.controller import miniapp
from app import schemas

route = APIRouter()


@route.post("/{app_id}/login", response_model=schemas.MiniAppUser)
def login(*, db: Session = Depends(deps.get_db), app_id: int, code: str):
    """
    微信小程序获取登录，获取用户信息
    """
    result = miniapp.get_user_info(app_id, code, db)
    return result
