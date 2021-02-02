#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
route = APIRouter()


@route.get('/rec/cover', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "received_cover.html",
        {"request": request}
    )
