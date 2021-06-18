def simple_math(x, y, z):
    """This function will output the numbers passed into the function, their average, their sum, and their product"""
    print("The numbers passed to the function are:", str(x) + ",", str(y) + ",", "and", str(z) + ".")
    #this calculates the sum of the three numbers passed into the function
    sum = x + y + z
    #this prints the sum of the numbers
    print("The sum of the numbers:", sum)
    #this calculates the average of the three numbers passed into the function
    average = sum / 3
    #this prints the average of the numbers
    print("The average of the numbers:", average) 
    #this calculates the product
    product = x * y * z
    #this prints the product
    print("The product of the numbers:", product)


