def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return
    except ValueError:
        return


print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))
