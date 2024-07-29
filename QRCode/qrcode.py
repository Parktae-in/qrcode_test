import pyqrcodeng as qrcode

#qrcode URL 생성
q = qrcode.create("https://www.naver.com")
#qrcode url 이미지 생성
#q.png("test.png", module_color=(34, 30, 63), background=(255, 255, 0), scale=8
#base64 인코딩된 문자열 데이터로 변환
qr_str = q.png_data_uri(module_color=(34, 30, 63), background=(255, 255, 0), scale=8)

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


qrcode_namecard("Name", "010-0000-0000")