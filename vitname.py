import requests
from bs4 import BeautifulSoup
from captchaparser import CaptchaParser
from io import BytesIO
from PIL import Image

mainurl = 'https://vtop.vit.ac.in/student/stud_login_submit.asp'
captchurl = 'https://vtop.vit.ac.in/student/captcha.asp'
s = requests.session()
r1 = s.get(captchurl, verify=False)
# print(r1.status_code)
if(r1.status_code == 200):
        image = Image.open(BytesIO(r1.content))
        image.save('./captcha.bmp')
        # image.show()
        img = Image.open("captcha.bmp")
        parser = CaptchaParser()
        captcha = parser.getCaptcha(img)
        # print(captcha)
        regno=raw_input("/nEnter Registration Number:")
        password=raw_input("/nEnter Password:")
        data = {'regno': regno, 'passwd': password,
            'vrfcd': captcha, 'message': ''}
        r = s.post(mainurl, data)
        # print(r.content)
        soup = BeautifulSoup(r.content, 'html.parser');
        s = soup.find_all('table')[1].find_all('td')[0];
        names =s.text
        n=''
        names=names.split()
        # print(names)
        for name in names:
            if(name == "Welcome"):
                continue;
            if(name == "-"):
                break;
            n =n+" "+name
            
myname=n
print("\n########################## Scraped Name is: "+myname+" ###########################")


