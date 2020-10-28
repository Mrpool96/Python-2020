import numpy as np
from datetime import date
from datetime import datetime

today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Today's date is:- " ,today)
print("Current time = " , current_time)

arr = np.array(["Sagar",2,"Aniket",3,"Abhi",4])

print(arr[1:5])

#We pass slice instead of index like this: [start:end].
#We can also define the step, like this: [start:end:step].
#If we don't pass start its considered 0
#If we don't pass end its considered length of array in that dimension
#If we don't pass step its considered 1 #

