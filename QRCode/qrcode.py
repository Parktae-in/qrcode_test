import pyqrcodeng as qrcode

#qrcode URL 생성
q = qrcode.create("https://www.naver.com")
#qrcode url 이미지 생성
#q.png("test.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=8
#base64 인코딩된 문자열 데이터로 변환
qr_str = q.png_data_uri(module_color=(34, 30, 63), background=(255, 255, 0), scale=8)

#qrcode namecard 생성하기
#vCARD 포멧 형식으로 생성
def qrcode_namecard(name, tel, email=None, url=None, org=None, title=None):
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

    q = qrcode.create(vcard, encoding="utf-8")
    q.png("namecard.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=5)

#공유기 와이파이 qr코드 생성
def qrcode_wifi(ssid, encrypt, password):
    data = f"WIFI:S:{ssid};T:{encrypt};P:{password}"
    q=qrcode.create(data, encoding="utf-8")
    q.png("wificode.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=5)

#sms 전송 qrcode
def qrcode_sms(sendto, msg):
    data = f"SMSTO:{sendto}:{msg}"
    q=qrcode.create(data, encoding="utf-8")
    q.png("sms.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=5)

#이메일 작성해주는 qrcode
def qrcode_email(email, subject, body):
    data = f"MATMSG:TO:{email};SUB:{subject};BODY:{body};;"
    q=qrcode.create(data, encoding="utf-8")
    q.png("emailsend.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=5)

#휴대폰 지도 실행후 위도 경도 표시
def qrcode_geo(lon, lat):
    data = f"GEO:{lon},{lat}?z=10"
    q=qrcode.create(data, encoding="utf-8")
    q.png("geo.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=5)

    

qrcode_namecard("Name", "010-0000-0000")
qrcode_wifi("IPTIME", "WPA", "123123123")

qrcode_geo(37.11,26.11)