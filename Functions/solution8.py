
# create a function that accepts any number of keyword arguments and point them in the format key:value
def dicfun(**args):
   print("Name :",args["name"])
   print("marks :",args["marks"])
dicfun(name="virendra",marks=(10,20,30))