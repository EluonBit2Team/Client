import cv2
from pyzbar import pyzbar
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Qrcode:
    def __init__(self, main_window):
        self.main_window = main_window
        self.label = self.main_window.qrlogin_label_waiting
        self.socket = self.main_window.socket
        print("qtcode 클래스 이니셜라이즈")
    
    def decode_qr(self, frame):
        decoded_objects = pyzbar.decode(frame)
    
        # 첫 번째로 발견된 QR 코드의 데이터 추출
        if decoded_objects:
            qr_data = decoded_objects[0].data.decode("utf-8")
            return qr_data
    
        return None

    def wait_qrcode(self):
        try:
            # 웹캠 시작
            self.cap = cv2.VideoCapture(cv2.CAP_DSHOW)
            
            if not self.cap.isOpened():
                print("웹캠을 열 수 없습니다.")
                return
            
            print("웹캠시작됨")
            
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    print("프레임을 읽을 수 없습니다.")
                    break

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                qimg = QImage(frame.data, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format.Format_RGB888)
                pixmap = QPixmap.fromImage(qimg)
                self.label.setPixmap(pixmap)

                # QR 코드 디코딩 및 데이터 추출
                qr_data = self.decode_qr(frame)
                
                # 추출된 QR 코드 데이터 출력
                if qr_data:
                    print(f"QR 코드 데이터: {qr_data}")
                    self.main_window.packetSender.printSendClass()
                    self.main_window.packetSender.loginRequest(self.socket, qr_data)
                    break  # 데이터를 추출하면 반복문 종료
                
                # 'q' 키를 누르면 종료
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        
        except Exception as e:
            print(f"오류 발생: {e}")
        
        finally:
            # 리소스 해제
            if self.cap.isOpened():
                self.cap.release()
    
    def stop_qrcode(self):
        print("웹캠종료함수 호출")
        if self.cap and self.cap.isOpened():
            self.cap.release()