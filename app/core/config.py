#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
from environs import Env
from pydantic import BaseSettings, BaseModel


class WeChatConfig(BaseModel):

    appid: str
    app_secret: str


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str
    WECHAT_TOKEN: str = "azhizhizhia"

    WECHAT_CONF: WeChatConfig


env = Env()
env.read_env()
settings = Settings(
    PROJECT_NAME=env.str("PROJECT_NAME"),
    WECHAT_CONF=WeChatConfig(
        appid=env.str("WECHAT_APPID"),
        app_secret=env.str("WECHAT_APP_SECRET")
    )
)
