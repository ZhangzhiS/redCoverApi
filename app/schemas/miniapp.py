#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseModel


class MiniAppConfigBase(BaseModel):
    appid: str
    app_secret: str


class MiniAppConfigCreate(MiniAppConfigBase):
    author: str


class MiniAppConfigUpdate(MiniAppConfigBase):
    app_secret: Optional[str] = None
    author: Optional[str] = None
    remarks: Optional[str] = None


class MiniAppConfigInDBBase(MiniAppConfigBase):
    id: int
    appid: str
    app_secret: str
    author: Optional[str] = None

    class Config:
        orm_mode = True


class MiniAppConfig(MiniAppConfigInDBBase):
    pass
