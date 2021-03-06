#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
红包封面小程序接口
"""
from typing import List, Optional

from fastapi import APIRouter, Depends, Body
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.api import deps
from app.api.api_v1.endpoints.index import templates
from app.controller import miniapp
from app import schemas
from app.schemas import MiniAppInviteUserCreate, MiniAppInviteUser, Cps, RedCover
from app.schemas import MiniAppTip

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
    """openid: 分享链接所属的openid，invite_openid: 被邀请的用户的openid"""
    # print(invite_user.json())
    result = miniapp.track_invite_user(
        app_id, invite_user.openid, invite_user.invite_openid, db, invite_user.cover_id
    )
    return result


@route.get("/{app_id}/cps", response_model=List[Cps])
def get_cps_list(
        *,
        db: Session = Depends(deps.get_db),
        app_id: int
):
    result = miniapp.get_cps_list(app_id, db)
    return result


@route.get("/{app_id}/cover", response_model=List[RedCover])
def get_covers(
        *,
        db: Session = Depends(deps.get_db),
        app_id: int
):
    return miniapp.get_covers(app_id, db)


@route.get("/{app_id}/tip", response_model=List[str])
def get_tips(
        *,
        db: Session = Depends(deps.get_db),
        app_id: int,
        page: Optional[str] = None,
        item_id: Optional[int] = None
):
    res = miniapp.get_tips(app_id, db, page, item_id)
    return [i.tip for i in res]


@route.get("/{app_id}/cover/detail")
def get_cover_detail(
        *,
        db: Session = Depends(deps.get_db),
        app_id: int,
        cover_id: int,
        openid: str
):
    return miniapp.get_cover_detail(cover_id, openid, app_id, db)


class AdTrack(BaseModel):
    openid: str
    status: bool
    cover_id: int


@route.post("/{app_id}/ad/track")
def do_ad_track(
        *,
        db: Session = Depends(deps.get_db),
        app_id: int,
        ad_track: AdTrack = Body(None)
):

    return miniapp.track_ad_history(
        app_id=app_id,
        openid=ad_track.openid,
        cover_id=ad_track.cover_id,
        status=ad_track.status,
        db=db
    )


@route.get("/{app_id}/cmVjZWl2ZWQ")
def user_cover_received(
        *,
        db: Session = Depends(deps.get_db),
        app_id: int,
        receive_str: str,
        request: Request,
):
    """用户领取封面"""
    res = miniapp.do_received(db, app_id, receive_str)
    if not res:
        res = "输入有误"
    return templates.TemplateResponse(
        "received_cover.html",
        {"request": request, "context": {"code": res}}
    )
