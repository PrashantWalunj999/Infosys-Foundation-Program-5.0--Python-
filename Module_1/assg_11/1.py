#Consider two variables 'a' and 'b' in Python such that a = 4 and b = 5. Swap the values of 'a' and 'b' without using a temporary variable. Print the values of 'a' and 'b' before and after swapping.

a = 4
b = 5
print("before Swapping: a =",a ," b =", b);

# Code to swap 'a' and 'b' 
# a now becomes 9 
a = a + b   
# b becomes 4
b = a - b  
# a becomes 5 
a = a - b   
print("After Swapping: a =",a ," b =", b); 

'''
output::
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/infosys/fp5.0_prashantwalunj/module_1/assg_11$ python3 1.py
before Swapping: a = 4  b = 5
After Swapping: a = 5  b = 4
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/infosys/fp5.0_prashantwalunj/module_1/assg_11$

'''