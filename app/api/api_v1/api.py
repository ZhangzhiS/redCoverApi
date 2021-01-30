#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

from fastapi import APIRouter

from app.api.api_v1.endpoints import index
from app.api.api_v1.endpoints import red_cover_miniapp

api_router = APIRouter()
api_router.include_router(index.route)
api_router.include_router(red_cover_miniapp.route, prefix="/wx/app", tags=["wechat"])
