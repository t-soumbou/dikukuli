# Web app entry point
import os

import bottle
import app_rest_modules

if __name__ == "__main__":
    app_rest_modules.init()
    port = int(os.environ.get('PORT', 33507))
    bottle.run(port=port)
