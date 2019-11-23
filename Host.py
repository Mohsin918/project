#This file registeres the Host who has to attend a Client
from tkinter import*

class Hosts:
    #Host Details
    hostname=""
    hostmail=""
    hostphone=""
    
    #Registration of the host
    def register_host(self):
        Hosts.hostname=username.get()
        Hosts.hostmail=email.get()
        Hosts.hostphone=phone.get()
        print("Registered Successfully")
        screen.destroy()
        from Guest import Guests
        guest = Guests()
        guest.guest_screen()
        
    #GUI screen for the host registration
    def main_screen(self):
        global screen
        screen = Tk();
        screen.geometry("300x290")
        global username,email,phone
        username = StringVar()
        email = StringVar()
        phone = StringVar()
        screen.title("Host Info")
    
        Label(text="Host Registration",bg="Yellow",width="15",height="1",font=("Calibri",13)).pack()
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
        button = Button(text="Register",width=10,height=1,command=self.register_host)
        button.pack()
        screen.mainloop()

