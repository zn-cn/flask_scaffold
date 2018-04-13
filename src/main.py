from app import app
import os

if __name__ == "__main__":
    debug = True
    if os.environ.get("WEB_ENV", "dev") == "prod":
        debug = False
    port = int(os.environ.get("WEB_ENV", 3031))
    host = os.environ.get("HOST", "0.0.0.0")

    app.run(host=host, port=port, debug=debug)