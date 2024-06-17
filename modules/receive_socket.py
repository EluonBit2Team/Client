import json
import struct
import select
from PySide6.QtWidgets import QMessageBox
from modules.util import *


class ReceivePacket():
    def __init__(self, main_window):
        self.main_window = main_window
        self.receivedPacket = 0
        self.running = True

    
    def receiveMessage(self, socket):
        self.sock = socket
        buffer = b""
        while self.running:
            try:
                if self.sock:
                    readable, _, _ = select.select([self.sock], [], [], 0.5)
                    if readable:
                        data = self.sock.recv(4096)
                        if data:
                            buffer += data
                            print("received message: ")
                            print(data)
                            print("end")
                            while len(buffer) >= 4:
                                msg_length = struct.unpack('<I', buffer[:4])[0]
                                if len(buffer) >= msg_length - 4:
                                    json_msg = buffer[4:4 + msg_length]
                                    buffer = buffer[4 + msg_length:]
                                    self.message = json.loads(json_msg.decode('utf-8')).get("text")
                                    self.main_window.updateMsgDisplay(self.message, "received")
                                
                                else:
                                    break
            except BlockingIOError:
                continue
            except Exception as e:
                print(f"An error occurred: {e}")
                self.running = False