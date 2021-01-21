#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
import secrets
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str
    WECHAT_TOKEN: str = "azhizhizhia"


settings = Settings(PROJECT_NAME="wallet")
