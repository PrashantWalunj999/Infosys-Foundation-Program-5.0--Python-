item=input("Enter name of furniture\n")

quan= int(input("Enter quantity of furniture\n"))

furniture=["Sofa set","Dining table","T.V Stand","Cupboard"]

cost=[20000,8500,4599,13920]

if(item in furniture and quan>0):
    index=furniture.index(item)
    bill=quan*cost[index]
    print("Total bill of",quan,item,"is",cost[index],"*",quan,"=",bill)

else:
    bill=0
    print("Error\nbill is",0)



'''
output::

PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$ python3 sample.py
Enter name of furniture
Cupboard
Enter quantity of furniture
3
Total bill of 3 Cupboard is 13920 * 3 = 41760
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$ python3 sample.py
Enter name of furniture
Sofa set
Enter quantity of furniture
5
Total bill of 5 Sofa set is 20000 * 5 = 100000
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$

'''