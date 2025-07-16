# 📦 fileriver

This project is a Minimal Viable Product (MVP) for a unified file transfer server. It currently supports:

- ✅ HTTP file upload and download  
- ✅ FTP file transfer with authentication  
- ✅ TFTP file transfer 
- 🔜 SFTP placeholder for future integration  

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

Or manually:
```bash
pip install flask pyftpdlib tftpy
```

---

### 3. Run the Server

```bash
python main.py --ip <Network Adaptor IP>
```

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
