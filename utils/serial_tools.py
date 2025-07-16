import serial
import sys
import time
from utils.log_tools import serial_log_print
from datetime import datetime

def serial_conn(console_port, speed=115200) -> serial.Serial:
    ser = serial.Serial(
        port=console_port,
        baudrate=speed,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=2
    )
    if not ser.is_open:
        serial_log_print(console_port, f"Failed to connect to {console_port}")
        sys.exit(1)
    serial_log_print(console_port, f"Successfully connected to {console_port}")
    return ser

def send_command_and_record_log(ser, console_port, command, test_report, delay=0.1, response_wait=3) -> str:
    ser.reset_input_buffer()
    ser.reset_output_buffer()

    for char in command:
        ser.write(char.encode('utf-8'))
        time.sleep(delay)

    ser.write(b'\r\n')
    time.sleep(response_wait) 

    response = ser.read(ser.in_waiting).decode("utf-8").strip()
    with open(test_report, "a", encoding="utf-8") as test_report:
        now = datetime.now()
        print(f"[{now}][{console_port}] Response for '{command}':\n{response}")
        test_report.write(f"[{now}][{console_port}] Response for '{command}':\n{response}\n")

    return response

def send_command(ser, command, delay=0.1, response_wait=3):
    ser.reset_input_buffer()
    ser.reset_output_buffer()

    for char in command:
        ser.write(char.encode('utf-8'))
        time.sleep(delay)

    ser.write(b'\r\n')
    time.sleep(response_wait) 

    response = ser.read(ser.in_waiting).decode("utf-8").strip()
    now = datetime.now()
    print(f"[{now}] Response for '{command}':\n{response}\n")

    return response

def read_output(ser, console_port, test_report):
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    with open(test_report, "a", encoding="utf-8") as test_report:
        start_time = time.time()
        while True:
            if ser.in_waiting:
                line = ser.readline().decode(errors='ignore').strip()
                if line:
                    now = datetime.now()
                    print(f"[{now}][{console_port}] {line}")
                    test_report.write(f"[{now}][{console_port}] {line}")
            if time.time() - start_time > 20:
                break