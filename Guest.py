from tkinter import*
from datetime import datetime
import smtplib
import config
import requests
import json
URL = "https://www.way2sms.com/api/v1/sendCampaign"
class Guests:
    guest_name=""
    guest_email=""
    guest_phone=""
    def sendPostRequest(self,reqUrl,apiKey,secretKey,useType,phoneNo,senderId,textMessage):
        req_params = {'apikey':apiKey,'secret':secretKey,'usetype':useType,'phone': phoneNo,'message':textMessage,'senderid':senderId}
        print("Message Successfullt Sent")
        return requests.post(reqUrl, req_params)
    
    def send_email(self,a,message):
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(config.EMAIL_ADDRESS,config.PASSWORD)
            from Host import Hosts
            server.sendmail(config.EMAIL_ADDRESS,a,message)
            server.quit()
            print("Email Sent Successfully")
        except:
            print('Email Failed To Send')
            
    def register_guest(self):
        screen.destroy()
        Guests.guest_name = username.get()
        Guests.guest_email = email.get()
        Guests.guest_phone = phone.get()
        now = datetime.now()
        guest_check_in = now.strftime("%H:%M")
        from Host import Hosts
        message1=""
        message1+=Guests.guest_name+" "+Guests.guest_email+" "+Guests.guest_phone
        self.send_email(Hosts.hostmail,message1)
        response = self.sendPostRequest(URL,'EF7NRZHZSX7DWYKDTN8M1PL2DBYJ02YU','J10G6WE6D5HZZW70','stage',Hosts.hostphone,'mohsinquantum@gmail.com',message1)
        guest_check_out = input("Enter check out time: ")
        message2=""
        message2+= Guests.guest_name+" "+Guests.guest_phone+" "+guest_check_in+" "+guest_check_out+" "+Hosts.hostname
        self.send_email(Guests.guest_email,message2)
        
    def guest_screen(self):
        global screen
        screen = Tk()
        screen.geometry("300x350")
        global username,email,phone
        username = StringVar()
        email = StringVar()
        phone = StringVar()
        screen.title("Guest Info")
    
        Label(text="Guest Registration",bg="red",width="15",height="1",font=("Calibri",13)).pack()
        Label(text="").pack()
        Label(text="Please enter details below").pack()
        Label(text="").pack()
        Label(text="Username ").pack()
        Entry(textvariable=username).pack()
        Label(text="Email ").pack()
        Entry(textvariable=email).pack()
        Label(text="phone ").pack()
        Entry(textvariable=phone).pack()
        Label(text="").pack()
        button = Button(screen,text="Check In",width=10,height=1,command=self.register_guest)
        button.pack()
        screen.mainloop()
    
