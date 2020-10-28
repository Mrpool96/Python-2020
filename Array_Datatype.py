import numpy as np
from datetime import date
from datetime import datetime

today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Today's date is:- " ,today)
print("Current time = " , current_time)

arr = np.array([1,"BMW",2,"AUDI",3,"MERCEDES",4,"PORSCHE"])
print(arr.dtype)
#The NumPy array object has a property called dtype that returns the data