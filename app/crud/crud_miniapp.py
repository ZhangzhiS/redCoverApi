#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.miniapp import MiniAppConfig, MiniAppUser
from app.schemas import MiniAppUserUpdate, MiniAppUserCreate
from app.schemas.miniapp import MiniAppConfigCreate, MiniAppConfigUpdate


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


mini_app_config = CRUDMiniAppConfig(MiniAppConfig)
mini_app_user = CRUDMiniAppUser(MiniAppUser)
