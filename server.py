import bottle
import os

from bottle import template, request, view, static_file
from beaker.middleware import SessionMiddleware

app = bottle.app()

@app.route('/')
@view('home')
def index():
    return dict(qs=request.query, req=request)


@app.route('/_sess')
def test():
    s = request.environ.get('beaker.session')
    s['test'] = s.get('test',0) + 1
    s.save()
    return dict(counter=s['test'])

@app.route('/static/<path:path>')
def server_static(path):
    return static_file(path, root='./static')


def plug_middle(chain):
    session_opts = {
        'session.type': 'file',
        'session.cookie_expires': 300,
        'session.data_dir': './sessions',
        'session.auto': True
        }
    chain = SessionMiddleware(chain, session_opts)
    return chain

def main():
    port = os.environ.get("PORT", 9030)
    debug = os.environ.get("DEBUG", False)
    bottle.run(
        app=plug_middle(app),
        reloader=debug,
        host='0.0.0.0',
        port=port)

main() if __name__ == '__main__' else ''
