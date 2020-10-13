from tkinter import *
import tkinter
import tkinter as tk
from tkinter import messagebox
import socket 
from datetime import datetime 
import webbrowser

root=tk.Tk()
root.title("Port Scanner | Manjunathan C")
root.geometry("1000x500")
root.iconphoto(True,tk.PhotoImage(file="icon.png"))
root.config(bg="#22a7cc")


label=Label(root,text="Enter Your Website Or IP Addres ",bg="#22a7cc",fg="black",font=("courier",15,"bold italic"))
label.place(x=50,y=20)

urlEntry=Entry(root,fg="#22a7cc",bg="black",font=("courier",15,"bold italic"),width=30,borderwidth=6)
urlEntry.place(x=50,y=50)

labelPort=Label(root,text="Range of the ports You want to Scan \n(Max and Default is 65,535) ",bg="#22a7cc",fg="black",font=("courier",15,"bold italic"))
labelPort.place(x=30,y=100)

labelMinPort=Label(root,text="Min :",bg="#22a7cc",fg="black",font=("courier",15,"bold italic"))
labelMinPort.place(x=50,y=150)

urlMinPort=Entry(root,fg="#22a7cc",bg="black",font=("courier",15,"bold italic"),width=10,borderwidth=6)
urlMinPort.place(x=70,y=180)

labelMaxPort=Label(root,text="Max :",bg="#22a7cc",fg="black",font=("courier",15,"bold italic"))
labelMaxPort.place(x=250,y=150)

urlMaxPort=Entry(root,fg="#22a7cc",bg="black",font=("courier",15,"bold italic"),width=10,borderwidth=6)
urlMaxPort.place(x=270,y=180)

def find():
	def process():
		try:
			target = socket.gethostbyname(urlEntry.get())  
			ipAddr="IP Address : "+target
			textShow.insert(END,ipAddr)
			try:
				if urlMaxPort.get()=="":
					maxPortNum=65535
				else:
					maxPortNum=int(urlMaxPort.get())
			
				if urlMinPort.get()=="":
					minPortNum=1
				else:
					minPortNum=int(urlMinPort.get())
				try: 
					# will scan ports between 1 to 65,535 
					for port in range(minPortNum,maxPortNum): 
						s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
						socket.setdefaulttimeout(1) 
		          
        				# returns an error indicator 
						result = s.connect_ex((target,port)) 
						if result ==0: 
							if(port==20) or(port==21):
								portName="FTP"
							elif(port==22):
								portName="SSH"
							elif(port==23):
								portName="Telnet"
							elif(port==25):
								portName="SMTP"
							elif(port==50) or (port==51):
								portName="IPSec"
							elif(port==53):
								portName="DNS"
							elif(port==67) or (port==68):
								portName="DHCP"
							elif(port==69):
								portName="TFTP"
							elif(port==80):
								portName="HTTP"
							elif(port==110):
								portName="POP3"
							elif(port==119):
								portName="NNTP"
							elif(port==123):
								portName="NTP"
							elif(port==135) or (port==136) or (port==137) or(port==138) or(port==139):
								portName="NetBIOS"
							elif(port==143):
								portName="IMAP4"
							elif(port==161) or (port==162):
								portName="SNMP"
							elif(port==389):
								portName="LDAP"
							elif(port==443):
								portName="SSL"
							elif(port==989) or (port==990):
								portName="FTP over SSL/TLS (implicit mode)"
							elif(port==3389):
								portName="RDP"
							aText=f"\nPort {port} Is Open - {portName}"
							textShow.insert(END,aText)
							s.close()
				except:
					messagebox.showerror("Error","Network Error or Unknown Error Occured")
			except:
				messagebox.showerror("Error","Enter only Numbers in Port ")

		except:
			messagebox.showerror("Error","Invalid URL Or Network Error or Unknown Error Occured")	
	if(urlEntry.get()==""):
		messagebox.showwarning("Empty","Enter the URL")
	else:
		process()
		

buttonFind=Button(root,text="Find",fg="#22a7cc",bg="black",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=find)
buttonFind.place(x=180,y=250)

buttonClear=Button(root,text="Clear",fg="#22a7cc",bg="black",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=lambda: urlEntry.delete(0,END))
buttonClear.place(x=180,y=300)

buttonExit=Button(root,text="Exit",fg="#22a7cc",bg="black",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=root.destroy)
buttonExit.place(x=180,y=350)

buttonContact=Button(root,text="Contact",fg="#22a7cc",bg="black",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=lambda: webbrowser.open("https://github.com/cmanjunathan45/"))
buttonContact.place(x=180,y=400)

textShow=Text(root,fg="#22a7cc",bg="black",font=("courier",15,"bold italic"),width=35,height=16,borderwidth=6)
textShow.place(x=500,y=47)

root.mainloop()
