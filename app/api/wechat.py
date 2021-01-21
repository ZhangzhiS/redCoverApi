#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

from fastapi import APIRouter
from app.core.config import settings

wechat_route = APIRouter()


@wechat_route.get("/wx")
def check_token(
        signature: str,
        timestamp: str,
        nonce: str,
        echostr: str
):
    """
    校验微信服务
    :return:
    """
    args_list = [settings.WECHAT_TOKEN, timestamp, nonce]
    args_list.sort()
    s = "".join(args_list)
    sha1 = hashlib.sha1()
    sha1.update(s.encode(encoding="utf-8"))
    hashcode = sha1.hexdigest()
    if hashcode == signature:
        return int(echostr)
    return ""
