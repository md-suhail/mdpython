#!/usr/bin/python3
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("guess it", "pwd")
msg = "iam fine buddy!"
server.sendmail("guess it","guess it", msg)
server.quit()