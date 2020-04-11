str = input("Enter a string\n")

str=str.lower();

def isrepeat(x):
    flag=0
    for j in range(x):
        if(str[x]==str[j]):
            flag+=1

    if(flag!=0):
        return  True
    else:
        return  False





for i in range(len(str)):
    if(isrepeat(i)==True):
        continue
    count=0;


    for j in range(i,len(str)):
        if(str[i]==str[j]):
            count+=1

    print(count,str[i].upper(),sep='')


'''
output::

PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$ python3 sample.py
Enter a string
aa
2A
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$ python3 sample.py
Enter a string
a
1A
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$ python3 sample.py
Enter a string
aaaa
4A
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$ python3 sample.py
Enter a string
aabbdd
2A
2B
2D
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$
    
'''