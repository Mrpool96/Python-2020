import numpy as np
from datetime import date
from datetime import datetime

today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Today's date is:- " ,today)
print("Current time = " , current_time)

