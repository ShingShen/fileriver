import argparse
import os
import threading
import time
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def start_ftp_server_thread(server):
    server.serve_forever()

def start_ftp_server(ftp_ip, ftp_root='ftp_files', user='admin', password='admin', port=2121):
    os.makedirs(ftp_root, exist_ok=True)

    authorizer = DummyAuthorizer()
    authorizer.add_user(user, password, ftp_root, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer((ftp_ip, port), handler)

    print(f"✅ FTP Server started at {ftp_ip}:{port}, root: {ftp_root}")
    print("🔧 Press Ctrl+C to stop the server.")

    server_thread = threading.Thread(target=start_ftp_server_thread, args=(server,))
    server_thread.daemon = True
    server_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user (Ctrl+C)")
        server.close_all()
