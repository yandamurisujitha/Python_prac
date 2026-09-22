import random
import datetime
import os
numb = random.randint(12,89) # randint predefined function
print(numb)

partcicipants = ["Anie","jessica","goldie","Geven"]
pickOne=random.choice(partcicipants) # randint predefined function
print(pickOne)

current_time = datetime.datetime.now()
expire_date = current_time+datetime.timedelta(days=7)
print(current_time)

print(f"datetime registered at : {current_time.strftime('%y-%m-%d %H:%M:%S')}")
print(f"expire_date registered at: {expire_date.strftime('%y-%m-%d %H:%M:%S')}")

current_dir = os.getcwd()
print(current_dir)

data_filename="session_data.json"
print(data_filename)