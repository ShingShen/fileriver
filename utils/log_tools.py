import datetime

def log(log_file, msg):
    with open(log_file, "a", encoding="utf-8") as f:
        now = datetime.datetime.now()
        print(f"[{now}] {msg}\n", flush=True)
        f.write(f"[{now}] {msg}\n")

def log_print(msg):
    now = datetime.datetime.now()
    print(f"[{now}] {msg}\n", flush=True)

def serial_log(console_port, log_file, msg):
    with open(log_file, "a", encoding="utf-8") as f:
        now = datetime.datetime.now()
        print(f"[{now}][{console_port}] {msg}\n", flush=True)
        f.write(f"[{now}][{console_port}] {msg}\n")

def serial_log_print(console_port, msg):
    now = datetime.datetime.now()
    print(f"[{now}][{console_port}] {msg}\n", flush=True)
