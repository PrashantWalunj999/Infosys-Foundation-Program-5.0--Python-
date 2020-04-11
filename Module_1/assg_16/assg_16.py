str = input("Enter a string for a palindrome check\n")
flag=0;
for i in range(len(str)):
    if(str[i] == str[-(i+1)]):
        flag+=0;
    else:
        flag+=1;


if(flag!=0):
    print("String is not a palindrome")
else:
    print("string is a palindrome")

'''
output::

PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$ python3 sample.py
Enter a string for a palindrome check
1
string is a palindrome
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$ python3 sample.py
Enter a string for a palindrome check
234
String is not a palindrome
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$ python3 sample.py
Enter a string for a palindrome check
e
string is a palindrome
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$ python3 sample.py
Enter a string for a palindrome check
ffdds
String is not a palindrome
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$


'''