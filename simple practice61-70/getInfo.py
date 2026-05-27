# Write A Python Program To Get Different Information Of Students From User And Display All The Student Information In This Order.
# Name			---------
# Father name 		---------
# CNIC			---------
# Age 			---------
# Contact 		---------

l=["Name","Father name","CNIC","Age","Contact"]
dic={}
for i in range(len(l)):
    dic[l[i]]=input(f"Enter your {l[i]} :")

for key,value in dic.items():
    print(key,":",value)