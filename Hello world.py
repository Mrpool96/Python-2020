#This is My first Python Helow World Program With Showing Current Date and Time

from datetime import date
from datetime import datetime
name = input("Enter Your Name:-")
age = input("Your age is:-")
today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print("Hello " +name+ "  Welcome to Python World You are " +age+ " years Old")
print("Today's date is:- " ,today)
print("Current time=" , current_time)

