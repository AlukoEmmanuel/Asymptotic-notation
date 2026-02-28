# Program to show Constant time complexity
def printnumber(n):
    iteration=0
    print("The number entered by user is ",n)
    iteration+=1
    print("Total iterations done by the code: ", iteration)

printnumber(10)
printnumber(20)
print("\n with any 'n' the time taken by our code won't change")