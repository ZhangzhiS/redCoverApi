#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseModel


class MiniAppTipBase(BaseModel):
    id: Optional[int]
    app_id: int
    tip: str
    page: Optional[str]
    item_id: Optional[int]
    

class MiniAppTipCreate(MiniAppTipBase):
    pass


class MiniAppTipUpdate(MiniAppTipBase):
    pass


class MiniAppTipInDBBase(MiniAppTipBase):
    pass

    class Config:
        orm_mode = True


class MiniAppTip(MiniAppTipInDBBase):
    pass
