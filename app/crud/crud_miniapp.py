#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.miniapp import MiniAppConfig, MiniAppUser, InviteUser
from app.schemas import MiniAppUserUpdate, MiniAppUserCreate, MiniAppInviteUser
from app.schemas import MiniAppInviteUserCreate, MiniAppInviteUserUpdate
from app.schemas import MiniAppConfigCreate, MiniAppConfigUpdate


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
    CRUDBase[MiniAppInviteUser, MiniAppInviteUserCreate, MiniAppInviteUserUpdate]
):
    """
    小程序用户相关
    """
    def check_invite(
            self,
            db: Session,
            app_id: int,
            openid: str,
            invite_openid: str
    ) -> Optional[MiniAppUser]:
        return db.query(self.model).filter(
            self.model.openid == openid,
            self.model.app_id == app_id,
            self.model.invite_openid == invite_openid
        ).first()


mini_app_config = CRUDMiniAppConfig(MiniAppConfig)
mini_app_user = CRUDMiniAppUser(MiniAppUser)
mini_app_invite = CRUDMiniAppInviteUser(InviteUser)
