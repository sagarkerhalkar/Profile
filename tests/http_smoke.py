from __future__ import annotations

import contextlib
import functools
import http.server
import socketserver
import threading
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATHS = [
    '/',
    '/cv/',
    '/admin/',
    '/projects/systemhealthmonitor/',
    '/assets/profile.json',
    '/assets/site.css',
    '/assets/site.js',
    '/assets/Sagar_Kerhalkar_IT_Infrastructure_DevOps_Leader_CV.pdf',
]

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass

handler = functools.partial(QuietHandler, directory=str(ROOT))
with socketserver.TCPServer(('127.0.0.1', 0), handler) as server:
    port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    time.sleep(0.2)
    try:
        for path in PATHS:
            with contextlib.closing(urllib.request.urlopen(f'http://127.0.0.1:{port}{path}', timeout=10)) as response:
                assert response.status == 200, (path, response.status)
                response.read()
                print(f'PASS {response.status} {path}')
    finally:
        server.shutdown()
        thread.join(timeout=5)

print('PASS local HTTP delivery for homepage, CV, admin, case study, assets and direct A4 PDF download.')
