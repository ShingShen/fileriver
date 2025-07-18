import os
from flask import Flask, request, send_from_directory, jsonify

UPLOAD_FOLDER = './http_server_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app = Flask(__name__)

# --- HTTP Upload ---
@app.route('', methods=['POST'])
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
@app.route('/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

# --- Optional: List Uploaded Files ---
# @app.route('/list', methods=['GET'])
# def list_files():
#     files = os.listdir(UPLOAD_FOLDER)
#     return jsonify({"files": files})

def start_http_server(ip, port=5001):
    print(f"Starting HTTP server on http://{ip}:{port}")
    app.run(host=ip, port=port, debug=False)