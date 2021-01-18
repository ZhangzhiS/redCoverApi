#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

from fastapi import APIRouter

from app.api.api_v1.endpoints import index

api_router = APIRouter()
api_router.include_router(index.route)