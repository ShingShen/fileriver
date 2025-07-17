# building...
import os
import socket
import threading
import paramiko
from paramiko import SFTPServerInterface, SFTPAttributes, SFTPHandle

HOST_KEY = paramiko.RSAKey.generate(2048)

class SimpleSFTPServer(SFTPServerInterface):
    def list_folder(self, path):
        files = os.listdir(path)
        return [SFTPAttributes.from_stat(os.stat(os.path.join(path, f)), filename=f) for f in files]

    def open(self, path, flags, attr):
        return SFTPHandle(os.open(path, flags))

def start_sftp_server(bind_ip, port=2222, root_dir="."):
    class SFTPServerHandler(paramiko.ServerInterface):
        def check_auth_password(self, username, password):
            return paramiko.AUTH_SUCCESSFUL if username == "test" and password == "test123" else paramiko.AUTH_FAILED

        def get_allowed_auths(self, username):
            return "password"

    def run():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((bind_ip, port))
        sock.listen(100)
        print(f"[SFTP] Listening on {bind_ip}:{port}")

        while True:
            client, addr = sock.accept()
            transport = paramiko.Transport(client)
            transport.add_server_key(HOST_KEY)
            server = SFTPServerHandler()
            transport.start_server(server=server)
            channel = transport.accept()
            transport.set_subsystem_handler("sftp", paramiko.SFTPServer, SimpleSFTPServer)

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
