#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RedCoverSerialBase(BaseModel):
    """红包封面序列号"""
    id: Optional[int]
    app_id: Optional[int]
    cover_id: Optional[int]
    red_cover_serial: Optional[str]
    status: Optional[bool]
    created_at: Optional[datetime]


class RedCoverSerialCreate(RedCoverSerialBase):
    pass


class RedCoverSerialUpdate(RedCoverSerialBase):
    status: bool = True
