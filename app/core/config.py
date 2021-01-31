#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
import os
from typing import Optional, Dict, Any

from environs import Env
from pydantic import BaseSettings, BaseModel, validator, PostgresDsn


class WeChatConfig(BaseModel):

    appid: str
    app_secret: str


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str
    # WECHAT_TOKEN: str = "azhizhizhia"

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )


# try:
env = Env()
env_path = "/etc/make-money/.env"
if os.path.exists(env_path):
    env.read_env(env_path)
else:
    env.read_env()
settings = Settings(
    PROJECT_NAME=env.str("PROJECT_NAME"),
)
