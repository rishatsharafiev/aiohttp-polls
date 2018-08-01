import sys
from aiohttp import web
from routes import setup_routes
from settings import get_config


async def init_app(argv=None):

    app = web.Application()

    app['config'] = get_config(argv)

    # setup views and routes
    setup_routes(app)

    return app

def main(argv):

    app = init_app(argv)

    config = get_config(argv)
    web.run_app(app,
                host=config['host'],
                port=config['port'])


if __name__ == '__main__':
    main(sys.argv[1:])