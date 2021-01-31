#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseModel


class CpsBase(BaseModel):
    id: Optional[int]
    app_id: int
    border: str
    desc: str
    icon: str
    appid: str
    path: str
    name: str
    platform: str
    sort: int
    tip: str


class CpsCreate(CpsBase):
    pass


class CpsUpdate(CpsBase):
    pass


class CpsInDBBase(CpsBase):
    pass

    class Config:
        orm_mode = True


class Cps(CpsInDBBase):
    pass
