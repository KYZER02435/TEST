import os
import re
import requests
import json
from datetime import datetime

#__________________[ COLOUR ]__________________#
A = '\x1b[1;97m'  # White
B = '\x1b[38;5;11m'  # Yellow
G1 = '\x1b[38;5;46m'  # Light Green
G2 = '\x1b[38;5;47m'  # Light Yellow Green
G3 = '\x1b[38;5;48m'  # Dark Green
G4 = '\x1b[38;5;49m'  # Olive
G5 = '\x1b[38;5;50m'  # Very Light Green

#__________________[ LOGO ]__________________#
logo = f"""{A}
{B}  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$  /$$$$$$$$
{B} /$$__  $$| $$  | $$ /$$__  $$| $$__  $$| $$_____/
{B}| $$  \\__/| $$  | $$| $$  \\ $$| $$  \\ $$| $$      
{B}|  $$$$$$ | $$$$$$$$| $$$$$$$$| $$$$$$$/| $$$$$   
{B} \\____  $$| $$__  $$| $$__  $$| $$__  $$| $$__/   
{B} /$$  \\ $$| $$  | $$| $$  | $$| $$  \\ $$| $$      
{B}|  $$$$$$/| $$  | $$| $$  | $$| $$  | $$| $$$$$$$$
{B} \\______/ |__/  |__/|__/  |__/|__/  |__/|________/
{A}──────────────────────────────────────────────────────────
{G1}[{A}•{G1}]{G1} OWNER      {A}:{G1} KYZER
{G1}[{A}•{G2}]{G2} FACEBOOK   {A}:{G2} KYZER
{G1}[{A}•{G3}]{G3} TOOL TYPE  {A}:{G3} AUTO SHARE POST
{G1}[{A}•{G4}]{G4} STATUS     {A}:{G4} PAID
{A}──────────────────────────────────────────────────────────"""

def clear():
    os.system('clear')
    print(logo)

def linex():
    print(f'{A}──────────────────────────────────────────────────────────')

def approval():
    import os, time, requests
    uuid = str(os.geteuid()) + "DS" + str(os.geteuid())
    id = "KYZER-SHARE-TOOL-" + "".join(uuid)
    clear()
    print(f"\033[1;37m{B}[{B}\u001b[36m•{B}] \033[0;32mYou Need Approval To Use This Tool\033[1;37m")
    print(f"\033[1;37m{B}[{B}\u001b[36m•{B}] \033[0;32mYour Key :\033[0;31m {id}")
    time.sleep(0.1)
    print("""\033[0;37m──────────────────────────────────────────────────────────""")
    try:
        httpCaht = requests.get("https://github.com/KYZER02435/TEST/blob/main/key.txt").text
        if id in httpCaht:
            print("\033[0;32m >> Your Key Has Been Approved !!!")
            msg = str(os.geteuid())
            time.sleep(1)
        else: 
            print("\x1b\033[0;32m >> Send Key on Facebook")
            time.sleep(0.1)
            input(' >> Click Enter To Send Your Key ')
            tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:' + id)
            os.system('am start https://www.facebook.com/100051353153084=' + tks)
            approval()      
            time.sleep(1)
            exit()
    except: 
        print(" >> Unable To Fetch Data From Server ")
        time.sleep(2)
        exit()

def logo_menu():
    clear()
    print(f"{G1}LOGIN COOKIES FIRST BRO")
    print(f"{G1}TAKE COOKIES FROM KIWI BROWSER")
    
    cookie = input(f"{G1}Enter your Facebook cookies: ")
    
    try:
        response = requests.get(
            "https://business.facebook.com/business_locations",
            headers={
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
                "referer": "https://www.facebook.com/",
                "host": "business.facebook.com",
                "origin": "https://business.facebook.com",
                "upgrade-insecure-requests": "1",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "max-age=0",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type": "text/html; charset=utf-8"
            },
            cookies={"cookie": cookie}
        )
        
        print(f"Response status code: {response.status_code}")
        
        find_token = re.search("(EAAG\w+)", response.text)
        if find_token:
            token = find_token.group(1)
            with open(".token.xx.txt", "w") as token_file:
                token_file.write(token)
            with open(".cookie.xx.txt", "w") as cookie_file:
                cookie_file.write(cookie)
            print("SUCCESSFUL LOGIN")
            bot_share(token, cookie)
        else:
            raise ValueError("Token not found in response")
    
    except Exception as e:
        print(f"Error during login: {e}")
        if os.path.exists(".token.xx.txt"):
            os.remove(".token.xx.txt")
        if os.path.exists(".cookie.xx.txt"):
            os.remove(".cookie.xx.txt")
        print("COOKIE INVALID")
        login()

def bot_share(token, cookie):
    clear()
    
    try:
        cookie_dict = {"cookie": cookie}
        ip = requests.get("https://api.ipify.org").text
        
        user_info = requests.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies=cookie_dict).json()
        nama = user_info.get("name", "Unknown")
        id = user_info.get("id", "Unknown")
    
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return
    
    clear()
    print(f"{G1}USER ACTIVE     : {nama}")
    print(f"{G1}YOUR ID         : {id}")
    print(f"{G1}YOUR IP         : {ip}")
    print(f"{G1}CURRENT DATE    : {datetime.now().strftime('%A, %d %B %Y')}")
    
    link = input(f"{G1}\nEnter the post link: ")
    jumlah = int(input(f"{G1}Initial amount of shares: "))
    
    print(f"{G1}\nAUTO SHARE IS RUNNING")
    
    n = 0
    header = {
        "authority": "graph.facebook.com",
        "cache-control": "max-age=0",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"
    }
    
    while jumlah > 0:
        n += 1
        try:
            post = requests.post(
                f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&privacy={{'value':'SELF'}}&access_token={token}", 
                headers=header, 
                cookies=cookie_dict
            ).json()
            
            if "COOKIE LIMIT" in json.dumps(post):
                print("\nAUTO SHARES STOPPED! YOUR COOKIE IS LIMITED")
                print("\x1b[31m" + "COOKIE LIMIT REACHED. PLEASE GET ANOTHER ONE." + "\x1b[0m")
                break
            
            if "id" in post:
                print(f"{G1}Successful sharing {n} post(s). Remaining shares: {jumlah - 1}")
                jumlah -= 1  # Decrement the number of shares left to do
            else:
                print(f"{G1}Failed to share the post.")
        
        except requests.exceptions.RequestException as e:
            print(f"{G1}Error occurred: {e}")
    
    print(f"{G1}All shares completed.")

# Main execution
approval()
logo_menu()