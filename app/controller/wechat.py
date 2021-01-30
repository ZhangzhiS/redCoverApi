#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
微信相关的服务
"""
from app.core.config import settings


class WeChatApiException(Exception):
    """
    接口异常
    """
    pass


class WeChatClient(object):
    """
    微信api的操作
    """

    def __init__(self):
        self._token = None
        self.token_expires_at = None

    @property
    def appid(self):
        return settings.WECHAT_CONF.appid

    @property
    def app_secret(self):
        return settings.WECHAT_CONF.app_secret
