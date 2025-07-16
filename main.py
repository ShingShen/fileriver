import argparse
import os
import threading
from filetraffic import ftp, tftp
from flask import Flask, request, send_from_directory, jsonify

UPLOAD_FOLDER = './http_server_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app = Flask(__name__)

# --- HTTP Upload ---
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return jsonify({"status": "success", "filename": file.filename})

# --- HTTP Download ---
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

# --- Optional: List Uploaded Files ---
@app.route('/list', methods=['GET'])
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify({"files": files})

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="File Servers")
    parser.add_argument("--ip", required=True, help="file server ip")
    args = parser.parse_args()
    server_ip = args.ip

    ftp_thread = threading.Thread(target=ftp.start_ftp_server, args=(server_ip,))
    ftp_thread.daemon = True
    ftp_thread.start()

    tftp_thread = threading.Thread(target=tftp.start_tftp_server, args=(server_ip,))
    tftp_thread.daemon = True
    tftp_thread.start()

    # Start HTTP server (Flask app)
    print("Starting HTTP server on http://{}:5000".format(server_ip))
    app.run(host=server_ip, port=5000)

    print("Servers are running... Press Ctrl+C to stop.")
