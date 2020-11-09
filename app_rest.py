# Web app entry point
import os

import bottle
import app_rest_modules

if __name__ == "__main__":
    run(host='localhost', port=8080)

app = bottle.default_app()
