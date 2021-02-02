#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RedCoverReceivedBase(BaseModel):
    """红包封面领取记录"""
    id: Optional[int]
    app_id: Optional[int]
    openid: Optional[str]
    cover_id: Optional[int]
    red_cover_serial: Optional[str]
    created_at: Optional[datetime]


class RedCoverReceivedCreate(RedCoverReceivedBase):
    pass


class RedCoverReceivedUpdate(RedCoverReceivedBase):
    pass
