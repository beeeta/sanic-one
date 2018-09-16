from sanic import Sanic,Blueprint
from sanic.response import json,redirect,text
from sanic.exceptions import NotFound

from .logger import get_logger

log = get_logger(__name__)

app = Sanic(__name__)


@app.exception(NotFound)
async def exception_handler(request, exception):
    return text('url not found!')


