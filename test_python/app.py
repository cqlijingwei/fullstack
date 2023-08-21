__all__ = ["app"]

from __init__ import create_app

from config import CONFIG

app = create_app()

if __name__ == "__main__":
    print(app.url_map)
    host, port = CONFIG.get("web_server", "host"), CONFIG.get("web_server", "port")
    app.run(host=host, port=port, threaded=False, debug=False)
