from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import sys
import threading
import webbrowser

root = Path(__file__).resolve().parent / 'out'
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
handler = partial(SimpleHTTPRequestHandler, directory=str(root))
try:
    server = ThreadingHTTPServer(('127.0.0.1', port), handler)
except OSError as error:
    raise SystemExit(f'Cannot start server on port {port}: {error}\nTry: python3 serve.py 8766')
url = f'http://localhost:{port}/ar/'
print(f'Friction AR: {url}\nPress Control-C to stop.')
threading.Timer(0.5, lambda: webbrowser.open(url)).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
