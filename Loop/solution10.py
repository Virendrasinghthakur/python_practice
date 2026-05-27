
import time
tries=5
wait=1
while tries:
    print("wait time is ",wait,"attempts left :",tries)
    time.sleep(wait)
    tries-=1
    wait*=2
    
