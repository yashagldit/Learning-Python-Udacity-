import webbrowser
import time
total=300
break_count=0
print("Started on "+time.ctime())
while(break_count<total):
    time.sleep(2*60*60)
    webbrowser.open("http://youtu.be/w0EF3AxJwLU")
    break_count=break_count+1
