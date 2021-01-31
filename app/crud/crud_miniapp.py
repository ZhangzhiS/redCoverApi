#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.miniapp import MiniAppConfig, MiniAppUser, InviteUser, Coupon, RedCover, MiniAppTip, AdHistory
from app.schemas import MiniAppUserUpdate, MiniAppUserCreate, WxAdCreate, WxAdUpdate
from app.schemas import MiniAppInviteUserCreate, MiniAppInviteUserUpdate
from app.schemas import MiniAppConfigCreate, MiniAppConfigUpdate
from app.schemas import CpsCreate, CpsUpdate
from app.schemas import RedCoverCreate, RedCoverUpdate
from app.schemas import MiniAppTipCreate, MiniAppTipUpdate


class CRUDMiniAppConfig(
    CRUDBase[MiniAppConfig, MiniAppConfigCreate, MiniAppConfigUpdate]
):
    """
    小程序配置相关
    """
    pass


class CRUDMiniAppUser(
    CRUDBase[MiniAppUser, MiniAppUserCreate, MiniAppUserUpdate]
):
    """
    小程序用户相关
    """
    def get_by_openid(self, db: Session, openid: str) -> Optional[MiniAppUser]:
        return db.query(self.model).filter(
            self.model.openid == openid
        ).first()


class CRUDMiniAppInviteUser(
    CRUDBase[InviteUser, MiniAppInviteUserCreate, MiniAppInviteUserUpdate]
):
    """
    小程序用户相关
    """
    def check_invite(
            self,
            db: Session,
            app_id: int,
            invite_openid: str
    ) -> Optional[InviteUser]:
        """
        校验用户是否被邀请过，如果被邀请过，则不算入邀请人数
        :param db:
        :param app_id:
        :param invite_openid:
        :return:
        """
        return db.query(self.model).filter(
            self.model.app_id == app_id,
            self.model.invite_openid == invite_openid
        ).first()

    def get_invite_count(
            self, db: Session, openid: str, app_id: int, cover_id: int
    ):
        """获取用户邀请好友的总数"""
        return db.query(self.model).filter(
            self.model.app_id == app_id,
            self.model.openid == openid,
            self.model.cover_id == cover_id,
        ).count()


class CRUDCps(CRUDBase[Coupon, CpsCreate, CpsUpdate]):

    def get_cps_list_by_app_id(self, db: Session, app_id: int):
        return db.query(self.model).filter(
            self.model.app_id == app_id
        ).all()


class CRUDRedCover(CRUDBase[RedCover, RedCoverCreate, RedCoverUpdate]):

    def get_cover_list_by_app_id(self, db: Session, app_id: int):
        return db.query(self.model).filter(
            self.model.app_id == app_id
        ).all()


class CRUDTip(CRUDBase[MiniAppTip, MiniAppTipCreate, MiniAppTipUpdate]):

    def get_tips_list(
            self,
            db: Session, app_id: int,
            page: Optional[str] = None,
            item_id: Optional[int] = None
    ):
        query = self.model.app_id == app_id
        if page:
            query &= self.model.page == page
        if item_id:
            query &= self.model.item_id == item_id
        return db.query(self.model).filter(
            query
        ).all()


class CRUDWxAd(CRUDBase[AdHistory, WxAdCreate, WxAdUpdate]):
    def get_look_history_count(
        self, db: Session, app_id: int, cover_id: int, openid: str,
        status: bool = True
    ):
        return db.query(self.model).filter(
            self.model.app_id == app_id,
            self.model.openid == openid,
            self.model.cover_id == cover_id,
            self.model.status == status
        ).count()


mini_app_config = CRUDMiniAppConfig(MiniAppConfig)
mini_app_user = CRUDMiniAppUser(MiniAppUser)
mini_app_invite = CRUDMiniAppInviteUser(InviteUser)
cps = CRUDCps(Coupon)
red_cover = CRUDRedCover(RedCover)
tip = CRUDTip(MiniAppTip)
wx_ad = CRUDWxAd(AdHistory)
