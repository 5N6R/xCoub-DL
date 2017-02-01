#(c) 2017, coded 5n6r
#!/usr/bin/env  python3
import requests,urllib.request,sys,json,re
print("\033[1;32m"+chr(10029)*55)
print("xCoub-DL версия 0.01 бета "+chr(169)+" 2017, программирование 5n6r\033[0;0m")
print("\033[1;32m"+chr(10029)*55+"\033[0;0m")
i=input("\033[1;32mВведите ссылку: \033[0;0m\033[1;35m")
opener=urllib.request.build_opener()
opener.addheaders=[("User-agent","Mozilla/5.0")]
st=re.findall(r"\w{5}$",i)
url="http://coub.com//api/v2/coubs/"+str("".join(st))
r = requests.get(url)
s=r.json()
try:
 htm5=s["file_versions"]["html5"]["video"]["high"]["url"]
 n=s["file_versions"]["html5"]["video"]["high"]["size"]
except:
 htm5=s["file_versions"]["html5"]["video"]["med"]["url"]
 n=s["file_versions"]["html5"]["video"]["med"]["size"]
z=s["channel"]["title"]
x=s["permalink"]
print("\033[1;32mНазвание ролика: \033[0;0m"+"\033[1;35m"+s["title"]+"\033[0;0m")
print("\033[0;0m\033[1;32mАвтор coub'a: \033[0;0m"+"\033[1;35m"+z+"\033[0;0m")
print("\033[1;32mРазмер файла: \033[0;0m"+"\033[1;35m"+str(n)+" байт\033[0;0m")
print("\033[1;32mСкачиваю видео, ждите... \033[0;0m")
client=opener.open(htm5)
f=open("video_"+str(x)+".mp4","wb")
f.write(client.read())
f.close()
print("\033[1;32mГотово! "+chr(9786)+"\033[0;0m")
exit(0)



