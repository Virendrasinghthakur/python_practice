# Write a Python OOP program to get a number from user to display its table.


class table:
    def print_table(n):
        for i in range(1,11):
            print(f"{n}X{i}={n*i}")


t=table
t.print_table(5)