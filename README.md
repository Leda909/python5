# python5

```
"""  This is how you can comment out multyple lines.
try:
  with open("file.txt", "r") as file:
    data = file.readlines()
    for line in data:
      print(line.strip())
except FileNotFoundError:
  print("The file with that name do not exist.")  
"""
```
```
"""
with open("file.txt", "a") as file:
  file.write("Hello, this is a second sentence!\n")
"""
```
```
import datetime

date = datetime.date.today().strftime("%d-%m-%y")
print(date)
```
