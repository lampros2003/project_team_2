import requests

url = "http://google.com"
timeout = 4

try:
    request = requests.get(url, timeout = timeout)
    internet = True
except ConnectionRefusedError:
    print('conrefused')
except:
    internet = False








#Πηγες
#1)https://cppsecrets.com/users/505510911110410511611497106105105105116107971081219711010564103109971051084699111109/How-to-Check-the-Internet-Connection-in-Python.php
#2)https://www.codespeedy.com/how-to-check-the-internet-connection-in-python/
#3)https://www.youtube.com/watch?v=NieQn_xc9AE
#4)https://www.youtube.com/watch?v=kvh8DQ7QRGY
