# full_duplex.py
import threading
import serial
import time

# ระบุพอร์ตที่เชื่อมกับ LR900F
serial_port = "/dev/tty.usbserial-4"  # หรือ "/dev/tty.SLAB_USBtoUART" สำหรับ macOS
baudrate = 57600

ser = serial.Serial(serial_port, baudrate, timeout=1)

def sender():
    while True:
        try:
            msg = input("🟢 You: ")
            ser.write((msg + "\n").encode())
        except Exception as e:
            print("Sender error:", e)
            break

def receiver():
    while True:
        try:
            line = ser.readline().decode().strip()
            if line:
                print(f"\n🔵 Friend: {line}\n🟢 You: ", end='', flush=True)
        except Exception as e:
            print("Receiver error:", e)
            break

# สร้าง thread แยกส่ง/รับ
threading.Thread(target=receiver, daemon=True).start()
sender()  # รัน sender ใน thread หลัก
