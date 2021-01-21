#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
import secrets
import os
from pydantic import BaseSettings, BaseModel


class WeChatConfig(BaseModel):

    appid: str
    app_secret: str


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str
    WECHAT_TOKEN: str = "azhizhizhia"

    WECHAT_CONF: WeChatConfig


settings = Settings(
    PROJECT_NAME=os.getenv("PROJECT_NAME"),
    WECHAT_CONF=WeChatConfig(
        appid=os.getenv("WECHAT_APPID"),
        app_secret=os.getenv("WECHAT_APP_SECRET")
    )
)
