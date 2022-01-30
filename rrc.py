  
 ​#!/usr/bin/python 
 ​# -*- coding: UTF-8 -*- 
  
 ​from​ ​os​ ​import​ ​system​, ​name 
 ​import​ ​itertools 
 ​import​ ​threading 
 ​import​ ​time 
 ​import​ ​sys 
 ​import​ ​datetime 
 ​from​ ​base64​ ​import​ ​b64decode​,​b64encode 
 ​from​ ​datetime​ ​import​ ​date 
  
 ​expirydate​ ​=​ ​datetime​.​date​(​2021​, ​10​, ​4​) 
 ​playday​ ​=​ ​datetime​.​date​(​2021​, ​10​,​3​) 
 ​#expirydate = datetime.date(2021, 8, 30) 
 ​today​=​date​.​today​() 
 ​def​ ​hero​(): 
  
 ​    ​def​ ​chalo​(): 
 ​        ​done​ ​=​ ​False 
 ​        ​#here is the animation 
 ​        ​def​ ​animate​(): 
 ​            ​for​ ​c​ ​in​ ​itertools​.​cycle​([​'|'​, ​'/'​, ​'-'​, ​'​\\​'​]) : 
 ​                ​if​ ​done​: 
 ​                    ​break 
 ​                ​sys​.​stdout​.​write​(​'​\r​hacking in the parity/bcone server for next colour--------- '​ ​+​ ​c​) 
 ​                ​sys​.​stdout​.​flush​() 
 ​                ​time​.​sleep​(​0.1​) 
 ​            ​sys​.​stdout​.​write​(​'​\r​Done!     '​) 
  
 ​        ​t​ ​=​ ​threading​.​Thread​(​target​=​animate​) 
 ​        ​t​.​start​() 
  
 ​        ​#long process here 
 ​        ​time​.​sleep​(​20​) 
 ​        ​done​ ​=​ ​True 
  
 ​    ​def​ ​chalo1​(): 
 ​        ​done​ ​=​ ​False 
 ​        ​#here is the animation 
 ​        ​def​ ​animate​(): 
 ​            ​for​ ​c​ ​in​ ​itertools​.​cycle​([​'|'​, ​'/'​, ​'-'​, ​'​\\​'​]): 
 ​                ​if​ ​done​: 
 ​                    ​break 
 ​                ​sys​.​stdout​.​write​(​'​\r​getting the colour wait --------- '​ ​+​ ​c​) 
 ​                ​sys​.​stdout​.​flush​() 
 ​                ​time​.​sleep​(​0.1​) 
 ​            ​sys​.​stdout​.​write​(​'​\r​Done!     '​) 
  
 ​        ​t​ ​=​ ​threading​.​Thread​(​target​=​animate​) 
 ​        ​t​.​start​() 
  
 ​        ​#long process here 
 ​        ​time​.​sleep​(​20​) 
 ​        ​done​ ​=​ ​True 
  
 ​    ​def​ ​clear​(): 
 ​        ​# for windows 
 ​        ​if​ ​name​ ​==​ ​'nt'​: 
 ​            ​_​ ​=​ ​system​(​'cls'​) 
 ​        ​# for mac and linux(here, os.name is 'posix') 
 ​        ​else​: 
 ​            ​_​ ​=​ ​system​(​'clear'​) 
 ​     
  
 ​    ​def​ ​checkg​(​n​): 
 ​        ​check​=​0 
 ​        ​for​ ​digit​ ​in​ (​n​): 
 ​            ​if​(​int​(​digit​)​==​0​): 
 ​                ​check​=​check​+​1 
 ​        ​return​ ​check 
 ​    ​def​ ​getSum​(​n​): 
 ​        ​sum​=​0 
 ​        ​for​ ​digit​ ​in​ ​str​(​n​): 
 ​            ​sum​+=​ ​int​(​digit​) 
 ​        ​return​ ​sum 
 ​    ​clear​() 
 ​    ​y​=​1 
 ​    ​newperiod​=​period 
 ​    ​banner​=​'figlet RXCE' 
 ​    ​numbers​=​[] 
 ​    ​while​(​y​): 
 ​        ​clear​() 
 ​        ​system​(​banner​) 
 ​        ​print​(​"Weekly members play PARITY all other play BCONE"​) 
 ​        ​print​(​"Contact me on telegram @smsn_knt"​) 
 ​        ​print​(​"Enter "​,​newperiod​,​" BCONE Price :"​) 
 ​        ​current​=​input​() 
 ​        ​current​=​int​(​current​) 
 ​        ​chalo​() 
 ​        ​print​(​"​\n​---------Successfully hacked the server-----------"​) 
 ​        ​chalo1​() 
 ​        ​print​(​"​\n​---------Successfully got the colour -------------"​) 
 ​        ​print​(​'​\n​'​) 
 ​        ​last2​=​str​(​current​)[​-​2​:] 
 ​        ​check​=​checkg​(​last2​) 
 ​        ​if​(​newperiod​%​2​==​0​): 
 ​            ​sum​=​getSum​(​current​)​+​check 
 ​            ​if​(​sum​%​2​==​0​): 
 ​                ​print​(​newperiod​+​1​,​" : 🔴"​) 
 ​            ​else​: 
 ​                ​print​(​newperiod​+​1​,​"  : 🟢"​) 
 ​        ​else​: 
 ​            ​sum​=​getSum​(​current​)​+​check​+​1 
 ​            ​if​(​sum​%​2​==​0​): 
 ​                ​print​(​newperiod​+​1​,​"   : 🔴"​) 
 ​            ​else​: 
 ​                ​print​(​newperiod​+​1​,​"   : 🟢"​) 
 ​        ​newperiod​+=​1 
 ​        ​numbers​.​append​(​current​) 
 ​        ​y​=​input​(​"Do you want to play : Press 1 and 0 to exit ​\n​"​) 
 ​        ​if​(​y​==​0​): 
 ​            ​y​=​False 
 ​        ​if​ (​len​(​numbers​)​>​11​): 
 ​            ​clear​() 
 ​            ​system​(​'figlet Thank you!!'​) 
 ​            ​print​(​"Play on next specified time!!"​) 
 ​            ​print​(​"-----------Current Time UP----------"​) 
 ​            ​sys​.​exit​(​" ​\n​ ​\n​ ​\n​ Contact on Telegram @smsn_knt"​) 
 ​            ​#print(numbers) 
  
 ​if​(​expirydate​>​today​ ​and​ ​playday​==​today​): 
 ​    ​now​ ​=​ ​datetime​.​datetime​.​now​() 
 ​    ​First​ ​=​ ​now​.​replace​(​hour​=​10​, ​minute​=​55​, ​second​=​0​, ​microsecond​=​0​) 
 ​    ​Firstend​ ​=​ ​now​.​replace​(​hour​=​11​, ​minute​=​35​, ​second​=​0​, ​microsecond​=​0​) 
 ​    ​Second​ ​=​ ​now​.​replace​(​hour​=​14​, ​minute​=​25​, ​second​=​0​, ​microsecond​=​0​) 
 ​    ​Secondend​ ​=​ ​now​.​replace​(​hour​=​15​, ​minute​=​5​, ​second​=​0​, ​microsecond​=​0​) 
 ​    ​Third​ ​=​ ​now​.​replace​(​hour​=​19​, ​minute​=​25​, ​second​=​0​, ​microsecond​=​0​) 
 ​    ​Thirdend​ ​=​ ​now​.​replace​(​hour​=​20​, ​minute​=​5​, ​second​=​0​, ​microsecond​=​0​) 
 ​    ​Final​ ​=​ ​now​.​replace​(​hour​=​20​, ​minute​=​25​, ​second​=​0​, ​microsecond​=​0​) 
 ​    ​Finalend​ ​=​ ​now​.​replace​(​hour​=​21​, ​minute​=​5​, ​second​=​0​, ​microsecond​=​0​) 
  
 ​    ​#if (now>First and now<Firstend): 
 ​    ​#        period=220 
 ​    ​#        #hero() 
 ​    ​if​(​now​>​Second​ ​and​ ​now​<​Secondend​): 
 ​            ​period​=​290 
 ​            ​#banner='figlet RXCE' 
 ​            ​#system(banner) 
 ​            ​#print("Server Overloading.....") 
 ​            ​#time.sleep(3) 
 ​            ​#print("Please try again later") 
 ​            ​#exit() 
 ​            ​hero​() 
 ​    ​elif​(​now​>​Third​ ​and​ ​now​<​Thirdend​): 
 ​            ​period​=​390 
 ​            ​hero​() 
 ​    ​elif​(​now​>​Final​ ​and​ ​now​<​Finalend​): 
 ​            ​period​=​410 
 ​            ​hero​() 
 ​    ​else​: 
 ​        ​banner​=​'figlet RXCE' 
 ​        ​print​(​"Hi!! Thanks for buying the hack"​) 
 ​        ​print​(​"----------Your play time-----------"​) 
 ​        ​#print(playday," 11:00 AM- 11:30 AM") 
 ​        ​print​(​playday​,​" 02:30 PM- 03:00 PM"​) 
 ​        ​print​(​playday​,​" 07:30 PM- 08:00 PM"​) 
 ​        ​print​(​playday​,​" 08:30 PM- 09:00 PM"​) 
 ​        ​print​(​"Please play on the given time, and "​) 
 ​        ​print​(​"If you think it is an error contact"​) 
 ​        ​print​(​" admin on telegram @smsn_knt "​) 
 ​elif​(​expirydate​>​today​): 
 ​    ​banner​=​'figlet RXCE' 
 ​    ​system​(​banner​) 
 ​    ​print​(​"Hi!! Thanks for buying the hack"​) 
 ​    ​print​(​"We got error today as Somebody is"​) 
 ​    ​print​(​"using our hack in bulk without our permission"​) 
 ​    ​print​(​"that's why we have updated your play time to tomorrow"​) 
 ​    ​print​(​"Thank you!! for ur understanding"​) 
 ​    ​print​(​"----------Your play time-----------"​) 
 ​    ​#print(playday," 11:00 AM- 11:30 AM") 
 ​    ​#print(playday," 02:30 PM- 03:00 PM") 
 ​    ​print​(​playday​,​" 07:30 PM- 08:00 PM"​) 
 ​    ​print​(​playday​,​" 08:30 PM- 09:00 PM"​) 
 ​    ​print​(​"Please play on the given time, and "​) 
 ​    ​print​(​"If you think it is an error contact"​) 
 ​    ​print​(​" admin on telegram @smsn_knt "​) 
  
  
 ​else​: 
 ​    ​banner​=​'figlet RXCE' 
 ​    ​system​(​banner​) 
 ​    ​print​(​"Your hack has expired--- Please contact"​) 
 ​    ​print​(​" on telegram -----------@smsn_knt"​)

 
 


