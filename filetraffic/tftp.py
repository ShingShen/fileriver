import argparse
import os
from tftpy import TftpServer

def start_tftp_server(tftp_ip, tftp_root='tftp_files', port=6969):
    os.makedirs(tftp_root, exist_ok=True)

    # give the folder read-write permission
    os.chmod(tftp_root, 0o777)
    server = TftpServer(tftp_root)
    print(f"✅ TFTP Server running on {tftp_ip}:{port}, root: {tftp_root}")
    print("🔧 Press Ctrl+C to stop.")
    try:
        server.listen(tftp_ip, port)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user (Ctrl+C)")
