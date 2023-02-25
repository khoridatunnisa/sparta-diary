from datetime import datetime

now = datetime.now()
print(now)

date_time = now.strftime("%Y-%m-%d-%H-%M-%S")
print(date_time)