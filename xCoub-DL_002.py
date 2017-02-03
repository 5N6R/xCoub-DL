#(c) 2017, coded 5n6r
#!/usr/bin/env  python3
from tkinter import *
import requests,urllib.request,sys,json,re,os
def mous(event):
	try:
		cb=app.clipboard_get()
		ii.set(cb)
	except:
		cl()
def runner():
	i=ii.get()
	if i!="":
		if len(sys.argv)>1:
			os.environ["http_proxy"]=sys.argv[1]
		opener=urllib.request.build_opener()
		opener.addheaders=[("User-agent","Mozilla/5.0")]
		st=re.findall(r"/\w+$",i)
		url="http://coub.com//api/v2/coubs"+str("".join(st))
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
		txt2.set("Название ролика: "+s["title"][:30]+";\n")
		txt2.set(txt2.get()+"Автор coub'a: "+z+";")
		txt3.set("Размер файла: "+str(n)+" байт; \n")
		client=opener.open(htm5)
		f=open("video_"+str(x)+".mp4","wb")
		f.write(client.read())
		f.close()
def cl()	:
	app.clipboard_clear()
	txt2.set("\n"+"")
	txt3.set("\n"+"")
	txt4.set("\n"+"")
	ii.set("")
app=Tk()
app.title(chr(10029)*3+" xCoub-DL версия 0.0.2 бета "+chr(169)+" 2017, программирование 5n6r "+chr(10029)*3)
app.geometry("590x180")
app.resizable(0,0)
fr0=Frame(app,bd=0,height=12)
fr0.pack(padx=10,pady=10)
fr1=Frame(fr0,bd=2,relief="groove")
fr1.grid(row=0, column=0,pady=5,padx=5)
fr2=Frame(fr0,bd=0)
fr2.grid(row=1, column=0,pady=5,padx=5)
fr3=Frame(fr0,bd=2,relief="groove")
fr3.grid(row=2, column=0,pady=5,padx=5)
ii=StringVar()
ii.set("")
txt2=StringVar()
txt2.set("\n"+"")
txt3=StringVar()
txt3.set("\n"+"")
txt4=StringVar()
txt4.set("\n"+"")
l=Label(fr1,text=">>> Ссылка на видео >>>",height=2)
l.grid(row=0,column=0,pady=5,padx=5)
e=Entry(fr1,textvariable=ii,bd=3,cursor="cross",width=40)
e.focus()
e.grid(row=0,column=1,pady=5,padx=5)
l2=Label(fr2,textvariable=txt2)
l2.grid(row=0,column=0,padx=1,pady=1)
l3=Label(fr2,textvariable=txt3)
l3.grid(row=0,column=1,padx=1,pady=1)
l4=Label(fr2,textvariable=txt4)
l4.grid(row=0,column=2,padx=1,pady=1)
b1=Button(fr3,text="Скачать",command=runner,cursor="hand2")
b1.grid(row=0,column=0,padx=3,pady=3)
b2=Button(fr3,text="Новая ссылка",command=cl,cursor="hand2")
b2.grid(row=0,column=1,padx=3,pady=3)
b3=Button(fr3,text="Выход из программы",command=app.destroy,cursor="hand2")
b3.grid(row=0,column=2,padx=3,pady=3)
e.bind("<Button-3>",mous)
app.mainloop()
