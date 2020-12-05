import requests
import random
import json
import time
import subprocess as sp
from termcolor import colored

user_agent_list = [
    #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)']
crypto_list = [
    ['[0] BTC','[1] BCH','[2] BSV','[3] ETH','[4] ETC','[5] LTC','[6] ZRX',
     '[7] USDC','[8] BAT','[9] MANA'],['[10] KNC','[11] LINK','[12] DNT',
     '[13] MKR','[14] CVC','[15] OMG','[16] DAI','[17] ZEC','[18] XRP',
     '[19] REP'],['[20] XLM','[21] EOS','[22] XTZ','[23] ALGO','[24] DASH',
     '[25] ATOM','[26] OXT','[27] COMP','[28] BAND','[29] NMR'],['[30] CGLD',
     '[31] UMA','[32] LRC','[33] YFI','[34] UNI','[35] BAL','[36] REN','[37] WBTC','[38] NU']]


col_width = max(len(word) for row in crypto_list for word in row) + 2  # padding
for row in crypto_list:
    print("".join(word.ljust(col_width) for word in row))

#user preferences
crypto_choice = int(input("\nCrypto to monitor: "))
crypto_amount = float(input("Enter your current amount of cryptos: "))
delay = int(input("Enter the delay in seconds: "))
currency = input("Currency (EUR/USD/GBP): ")

previous_price = 0.0
previous_change = 0.0
tmp = sp.call('clear', shell=True) #clear terminal

while True:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    timer = colored("["+current_time+"]",'white')
    user_agent = random.choice(user_agent_list)
    headers={'User-Agent' : user_agent, 
             'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
             'Accept-Encoding' : 'gzip, deflate, br', 
             'Accept-Language' : 'en-GB,en-US;q=0.9,en;q=0.8'}
    session1 = requests.Session()
    r1 = session1.get("https://www.coinbase.com/api/v2/assets/prices?base="+currency+"&filter=listed&resolution=latest", headers=headers)
    json_data = json.loads(r1.text)


    crypto_name = json_data['data'][crypto_choice]['base']
    currency = json_data['data'][crypto_choice]['currency']
    price = json_data['data'][crypto_choice]['prices']['latest']
    change = json_data['data'][crypto_choice]['prices']['latest_price']['percent_change']['hour']
    current_balance = round(((float(price) * crypto_amount)/1),5) #calculate current balance
        
    #check market status
    if float(change) >= 0.0:
        new_change = colored("Market is up by "+str(round(change,10))+"%",'green')
    else:
        new_change = colored("Market down by "+str(round(change,10))+"%",'red')

    #check price status
    if previous_price == float(price):
        # print("[*] Same price", price)
        pass
    elif previous_price < float(price):
        up = colored("[+] "+crypto_name+" price is: "+str(price)+" "+currency,'green')
        print(timer, up, new_change, colored("since the last hour.",'green'),colored("Balance: "+str(current_balance)+currency,'yellow'))
        previous_price = float(price)
        previous_change = float(change)

    elif previous_price > float(price):
        down = colored("[-] "+crypto_name+" price is: "+str(price)+" "+currency,'red')
        print(timer, down, new_change, colored("since the last hour.",'red'),colored("Balance: £"+str(current_balance),'yellow'))
        previous_price = float(price)
        previous_change = float(change)
    else:
        pass

    time.sleep(delay)



    
