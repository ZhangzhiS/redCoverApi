#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from pydantic import BaseModel


class RedCoverBase(BaseModel):
    id: Optional[int]
    app_id: int
    receive_desc: str
    invite_limit: str
    is_free: str
    ad_limit: str
    pic: str
    is_task_together: str
    is_in_stock: str
    notice_show: str


class RedCoverCreate(RedCoverBase):
    pass


class RedCoverUpdate(RedCoverBase):
    pass


class RedCoverInDBBase(RedCoverBase):
    pass

    class Config:
        orm_mode = True


class RedCover(RedCoverInDBBase):
    pass

