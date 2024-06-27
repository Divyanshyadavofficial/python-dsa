def rec(num):
    if(num==0):
        return 1
    elif(num==1):
        return 1
    else:
        return rec(num-1)*num
print(rec(5))

# # recursion approach
# define the function as it is ie rec(num)
# then define the function for one less iteration ie if the function 
# has n iterations then define it for n-1 iterations combine it with
# the last iteration to define the recursive case
# then define the base cases according to the logic of recursive case
# eg
# to define a function for factorial of a number these steps are folowed
# defining the as it is--->fact(n)
# definig the function for one less iteration--->fact(n-1) now
# combining this function with the nth number on the basis of logic--> fact(n-1)*n
# defining the base cases ---> in this cases are 0 and 1 if they occur 
# the rsult will be 1
