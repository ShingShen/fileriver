import functools
import subprocess
import time
from log_tools import log

# Retry decorator for unstable operations
def retry(times=3, delay=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == times:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry()
def ping_device(log_file, ip) -> bool:
    log(log_file, f"Pinging {ip}...")
    response = subprocess.call(["ping", ip, "-n", "4"], stdout=subprocess.DEVNULL)
    if response != 0:
        log(log_file, f"{ip} ping Fail.")
        # sys.exit(1)
        return False
    else:
        log(log_file, f"{ip} ping Pass.") 
        return True