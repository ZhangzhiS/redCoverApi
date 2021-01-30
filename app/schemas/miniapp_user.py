#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MiniAppUserBase(BaseModel):
    app_id: int
    openid: str
    # session_key: str


class MiniAppUserCreate(MiniAppUserBase):
    session_key: str
    created_at: Optional[datetime]


class MiniAppUserUpdate(MiniAppUserBase):
    pass


class MiniAppUserInDbBase(MiniAppUserBase):
    id: Optional[int] = None
    app_id: int
    openid: str

    class Config:
        orm_mode = True


class MiniAppUser(MiniAppUserInDbBase):
    pass
