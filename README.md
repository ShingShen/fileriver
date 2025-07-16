# 📦 File Transfer Server MVP

This project is a Minimal Viable Product (MVP) for a unified file transfer server. It currently supports:

- ✅ HTTP file upload and download  
- ✅ FTP file transfer with authentication  
- 🔜 SFTP placeholder for future integration  

All files are stored locally in the `./uploads/` directory.

---

## 🚀 Features

### ✅ HTTP Upload

Endpoint:  
```http
POST /upload
```

Usage: send a `multipart/form-data` request with the key `file`.  
Example tools: `curl`, Postman, Python `requests`, web form.

---

### ✅ HTTP Download

Endpoint:  
```http
GET /download/<filename>
```

It will return the requested file from the `uploads` directory.

---

### ✅ FTP Server

- Host: `localhost`  
- Port: `2121`  
- Username: `admin`  
- Password: `admin`  

Supported by any FTP client (e.g. FileZilla, WinSCP, command-line tools).

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

Or manually:
```bash
pip install flask pyftpdlib paramiko
```

---

### 3. Run the Server

```bash
python file_transfer_server.py
```

You should see:

- HTTP server running at: `http://localhost:5000`  
- FTP server listening on: `ftp://localhost:2121`

---

## 📁 Upload Directory

All uploaded or transferred files are stored under:

```
./uploads/
```

Ensure the application has write access to this folder.

---

## 🔧 Future Plans

- [ ] Implement internal SFTP server (Paramiko ServerInterface)  
- [ ] Add web-based file manager interface  
- [ ] User account and permission system  
- [ ] Docker container support  
- [ ] Logging, monitoring, and audit trail  

---

## 👨‍💻 Developer Notes

This MVP is ideal for quick testing, demonstrations, or internal use cases where simple file transfer is required across different protocols. It provides a foundation for building a more advanced, multi-protocol file management platform.
