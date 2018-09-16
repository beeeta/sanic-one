from sanic import Blueprint
from sanic.response import json, redirect

bp = Blueprint(__name__)

@bp.route('/')
async def hello(request):
    return json({'msg':'hello'})

@bp.route('/go/<name>')
async def go(request,name):
    return redirect('http://www.{}.com'.format(name))