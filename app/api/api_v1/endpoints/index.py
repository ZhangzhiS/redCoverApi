#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
from fastapi import APIRouter

route = APIRouter()


@route.get('/')
def index():
    return {"data": "hello world"}
