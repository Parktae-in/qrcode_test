import pyqrcodeng as qrcode
import os
from uuid import uuid4
import pyzbar.pyzbar as pyzbar
import cv2

#qrcode URL 생성
#q = qrcode.create("https://www.naver.com")
#qrcode url 이미지 생성
#q.png("test.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=8
#base64 인코딩된 문자열 데이터로 변환
#qr_str = q.png_data_uri(module_color=(34, 30, 63), background=(255, 255, 0), scale=8)



class QRCreater():
    def __init__(self):
        self.q = None
        self.module_color = (0, 0, 0, 0)
        self.back_color = (255, 255, 255, 255)
        self.scale = 8

    def get_base64(self):
        if self.q is not None:
            return self.q.png_data_uri(module_color=self.module_color, background=self.back_color, scale=self.scale)
        return None


    #qrcode namecard 생성하기
    #vCARD 포멧 형식으로 생성
    def qrcode_namecard(self, name, tel, email=None, url=None, org=None, title=None):
        vcard = f"BEGIN:VCARD\n"
        vcard += f"VSERSION:4.0\n"
        vcard += f"FN:{name}\n"
        vcard += f"TEL;TYPE=WORK;CELL:{tel}\n"

        if org is not None:
            vcard += f"ORG:{org}\n"
        if title is not None:
            vcard += f"TITLE:{title}\n"
        if email is not None:
            vcard += f"EMAIL;TYPE=WORK:{email}\n"
        if url is not None:
            vcard += f"URL:{url}\n"
        
        vcard += f"END:VCARD\n"

        #Class 생성으로 self 변경
        #q = qrcode.create(vcard, encoding="utf-8")
        #q.png("namecard.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=5)
        self.q = qrcode.create(vcard, encoding="utf-8")
        return self

    #공유기 와이파이 qr코드 생성
    def qrcode_wifi(self, ssid, encrypt, password):
        data = f"WIFI:S:{ssid};T:{encrypt};P:{password}"

        #q=qrcode.create(data, encoding="utf-8")
        #q.png("wificode.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=5)
        self.q=qrcode.create(data, encoding="utf-8")
        return self

    #sms 전송 qrcode
    def qrcode_sms(self, sendto, msg):
        data = f"SMSTO:{sendto}:{msg}"
        
        #q=qrcode.create(data, encoding="utf-8")
        #q.png("sms.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=5)
        self.q=qrcode.create(data, encoding="utf-8")
        return self

    #이메일 작성해주는 qrcode
    def qrcode_email(self, email, subject, body):
        data = f"MATMSG:TO:{email};SUB:{subject};BODY:{body};;"
        
        #q=qrcode.create(data, encoding="utf-8")
        #q.png("emailsend.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=5)
        self.q=qrcode.create(data, encoding="utf-8")
        return self

    #휴대폰 지도 실행후 위도 경도 표시
    def qrcode_geo(self, lon, lat):
        data = f"GEO:{lon},{lat}?z=10"
        
        #q=qrcode.create(data, encoding="utf-8")
        #q.png("geo.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=5)
        self.q=qrcode.create(data, encoding="utf-8")
        return self
    
    def make(self, data):
        self.q=qrcode.create(data, encoding="utf-8")
        return self
    
    def png(self):
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        filename = f"{cur_dir}\\{uuid4()}.png"
        self.q.png(filename, scale=8)
        return filename

#QR코드 파이썬을 통해 읽기
def read_qrcode_zbar(opencv_image):
    gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
    decoded = pyzbar.decode(gray)
    result = []
    for d in decoded:
        qr_data = d.data.decode("utf-8")
        qr_type = d.type

        result.append({
            "data": qr_data,
            "type": qr_type
        })
    return result



img = cv2.imread("wificode.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
a = pyzbar.decode(img)
print(a)


#qr_wifi = QRCreater().qrcode_wifi("IPTIME", "WPA", "123123123").get_base64()
#png_qr_wifi = QRCreater().qrcode_wifi("IPTIME", "WPA", "123123123").png()
#print(qr_wifi)

        

#qrcode_namecard("Name", "010-0000-0000")


#    qrcode_geo(37.11,26.11)

