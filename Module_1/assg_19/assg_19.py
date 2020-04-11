accepted_string=input("Enter a string")
print("accepted_string: ",accepted_string)
string=""

#removing whitepaces
for i in range(len(accepted_string)):
    if(accepted_string[i]==' '):
        continue

    string+=accepted_string[i]

resultant_string=""

for i in range(0,len(string),2):
    resultant_string+=string[i]


print("resultant_string: ",resultant_string)

exp = ""

for i in range(len(resultant_string)-1,-1,-1):
    exp+=resultant_string[i]

print("expected_outout: ",exp)



'''
output::

PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$ python3 sample.py
Enter a stringaaa
accepted_string:  aaa
resultant_string:  aa
expected_outout:  aa
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$ python3 sample.py
Enter a stringabcd
accepted_string:  abcd
resultant_string:  ac
expected_outout:  ca
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/Infosys$


'''