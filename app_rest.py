# Web app entry point

import bottle
import app_rest_modules

if __name__ == "__main__":
    app_rest_modules.init()
    bottle.run(port=int(os.environ.get("PORT", 5000)))
