#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class WxAdBase(BaseModel):
    cover_id: Optional[int]
    openid: str


class WxAdCreate(WxAdBase):
    id: Optional[int]
    app_id: Optional[int]
    status: bool


class WxAdUpdate(WxAdBase):
    pass


class WxAdInDbBase(WxAdBase):
    id: Optional[int]
    app_id: Optional[int]
    status: bool
    created_at: Optional[datetime]

    class Config:
        orm_mode = True


class WxAd(WxAdInDbBase):
    pass
