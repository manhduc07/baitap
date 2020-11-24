import smtplib
import getpass

email=input("Email: ")
password = input("password: ")
Address = input ("send to: ")
mess = input("content : ")
time=int(input("số lần muốn gửi: "))

client=smtplib.SMTP("smtp.gmail.com",587)
client.starttls()
client.login(email,password)

for i in range(1,time+1):
    content=mess + "- lan thu "+str (i)
    client.sendmail(email,Address,content)
    print("/\n tin nhắn đã được gửi đến {} \n/n\n".format(email,i))

client.quit()
end=input("enter để end")