# 📦 fileriver

This project is a unified file transfer server. It currently supports:

- ✅ HTTP file upload and download  
- ✅ FTP file transfer with authentication  
- ✅ TFTP file transfer 

---

## 🚀 Features

### ✅ HTTP Upload

Endpoint:  
```http
POST http://<HTTP SERVER IP>:5001/
```

Usage: send a `multipart/form-data` request with the key `file`.  
Example tools: `curl`, Postman, Python `requests`.

---

### ✅ HTTP Download

Endpoint:  
```http
GET http://<HTTP SERVER IP>:5001/<filename>
```

It will return the requested file from the `http_server_files` directory.

---

### ✅ FTP Server

- Host: `Network Adaptor IP`  
- Port: `2121`  
- Username: `admin`  
- Password: `admin`  

Supported by any FTP client (e.g. FileZilla, command-line tools).

---

### ✅ TFTP Server

- Host: `Network Adaptor IP`  
- Port: `6969`  

Supported by any TFTP client (e.g. Tftpd64, command-line tools).

---

## ⚙️ Installation & Setup

### 1. Create Python Virtual Environment

#### On Linux / macOS:
```bash
python3 -m venv <folder path>
source <folder path>/bin/activate
```

#### On Windows (cmd):
```cmd
python -m venv <folder path>
<folder path>\Scripts\activate
```

---

### 2. Install Dependencies

If using `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

### 3. Run the Server

```bash
python main.py --ip <Network Adaptor IP>
```

---

## 👨‍💻 Developer Notes

This tool is ideal for quick testing, demonstrations, or internal use cases where simple file transfer is required across different protocols. It provides a foundation for building a more advanced, multi-protocol file management platform.
