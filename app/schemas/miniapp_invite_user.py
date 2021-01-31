#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MiniAppInviteUserBase(BaseModel):
    openid: str
    invite_openid: str


class MiniAppInviteUserCreate(MiniAppInviteUserBase):
    id: Optional[int] = None
    app_id: Optional[int]
    created_at: Optional[datetime]


class MiniAppInviteUserUpdate(MiniAppInviteUserBase):
    pass


class MiniAppInviteUserInDbBase(MiniAppInviteUserBase):
    pass

    class Config:
        orm_mode = True


class MiniAppInviteUser(MiniAppInviteUserInDbBase):
    pass
