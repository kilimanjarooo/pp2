import datetime
import datetime as DT

day1 = datetime.datetime.today()
day2 = datetime.datetime(2005, 7, 3)
diff = day1 - day2
print(f"Difference in seconds: {diff.total_seconds()}")