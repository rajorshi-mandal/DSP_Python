def func_name(var1 = 100,var2 = 200):
    if var1 > var2:
        print("var1 is greater than var2")
        return "first condition was executed"
    elif var1 < var2:
        print("var1 is lesser than var2")
        return "second condition was executed"
    else:
        print("Both are equal !!")
        return "last condition was executed"