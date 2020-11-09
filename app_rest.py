# Web app entry point
import os

import bottle
import app_rest_modules

if __name__ == "__main__":
    app_rest_modules.init()
    bottle.run()
