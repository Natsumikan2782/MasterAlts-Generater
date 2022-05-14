import os,requests,json,re,time

apikey = os.environ['key']
url = f"https://2captcha.com/res.php?key={apikey}&action=getbalance"

def getMoney():
  solver = requests.get(url).text
  print("残高:",solver,"$")

def getUrl():
  data = {'gen': '',}
  
  response = requests.post('https://masteralts.com/',data=data)
  match = re.search(r"http(s)?://beta\.shortearn\.eu/[a-zA-Z0-9]+",response.text)
  
  if match != None:
    print(match.group())
  else:
    print("Can not gen url")  

  ourl=f"http://2captcha.com/in.php?key={apikey}&method=userrecaptcha&version=v3&action=verify&min_score=0.3&googlekey=6Lde6mYUAAAAAADDO372WogUwpZb17QmZbAMRTRr&pageurl={match.group()}"

  verify = requests.post(ourl)
  suuji = re.sub(r"\D", "",verify.text)
  
  zurl=f"http://2captcha.com/res.php?key={apikey}&action=get&json=1&id={suuji}"
  
  print("Captcha開始")
  
  for i in range(1,10):
    time.sleep(5)
    verify2 = requests.get(zurl)
    if verify2.text[0:2] == "OK":
        break
      
  print("Captcha完了")