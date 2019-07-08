try : 
    x = int(input("Enter a number : "))
    y = int(input("Enter another number : "))
    result = x / y
except BaseException as arg : 
    print("Error!! Something Went Wrong\n",arg)
else : 
    print(f"Done!!! result is {result:.2f}")
finally : 
    print("To free up your resources")

