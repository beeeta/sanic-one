from sanic import Sanic,Blueprint
from sanic.response import json,redirect,text
from sanic.exceptions import NotFound

from logger import get_logger

log = get_logger(__name__)

app = Sanic()

bp = Blueprint('static', url_prefix='resource')
bp.static('/static','./static')

app.blueprint(bp)

@app.route('/')
async def hello(request):
    return json({'msg':'hello'})

@app.route('/go/<name>')
async def go(request,name):
    return redirect('http://www.{}.com'.format(name))


@app.exception(NotFound)
async def exception_handler(request, exception):
    return text('url not found!')

app.run(host='0.0.0.0', port=8899, debug=True)
