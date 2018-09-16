from sanic import Blueprint
import os

cur_dir = os.path.dirname(__file__)
static_dir = os.path.join(cur_dir,'..','static')

bp = Blueprint('static', url_prefix='/resource')

bp.static('/static', static_dir)

