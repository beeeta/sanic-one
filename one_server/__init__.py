from .core import app

from .bps.bp_static import bp as bps
from .bps.bp_home import bp as bph

app.blueprint(bps)
app.blueprint(bph)