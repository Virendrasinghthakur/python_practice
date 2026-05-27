# Write a Python program to create a class of student having two data member (name and id) having a two methods, one is used to get name and id and other is to display name and id to user.
class student:
    def get(self):
        self.name=input("enter your name:")
        self.id=int(input("enter your id:"))

    def show(self):
        print(self.name)
        print(self.id)


s=student()
s.get()
s.show()