n=int(input("Enter how many fibonacci you want\n"))

l=[0,1]


for i in range(2,n):
    l.insert(i,l[i-1]+l[i-2])

print(l)


'''
output:::

PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$ python3 sample.py
Enter how many fibonacci you want
5
[0, 1, 1, 2, 3]
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$ python3 sample.py
Enter how many fibonacci you want
10
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$

'''