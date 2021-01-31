#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
红包封面小程序接口
"""
from fastapi import APIRouter, Depends, Body
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.api import deps
from app.controller import miniapp
from app import schemas
from app.schemas import MiniAppInviteUserCreate, MiniAppInviteUser

route = APIRouter()


class Code(BaseModel):
    code: str


@route.post("/{app_id}/login", response_model=schemas.MiniAppUser)
def login(
        *,
        db: Session = Depends(deps.get_db),
        app_id: int,
        code: Code = Body(None)
):
    """
    微信小程序获取登录，获取用户信息
    """
    result = miniapp.get_user_info(app_id, code.code, db)
    return result


@route.post("/{app_id}/invite/track", response_model=MiniAppInviteUser)
def invite_track(
        *,
        db: Session = Depends(deps.get_db),
        app_id: int,
        invite_user: MiniAppInviteUserCreate
):
    result = miniapp.track_invite_user(
        app_id, invite_user.openid, invite_user.invite_openid, db
    )
    return result
