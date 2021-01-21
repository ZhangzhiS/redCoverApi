#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
from fastapi import FastAPI

from app.core.config import settings
from app.api.api_v1.api import api_router
from app.api.wechat import wechat_route

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
app.include_router(wechat_route)
app.include_router(api_router, prefix=settings.API_V1_STR)
