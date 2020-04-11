#to calculate ‘x’ to the power of ‘n’ using a while loop.•Assume both ‘x’ and ‘n’ are positive whole numbers
START
DISPLAY "Enter the values of x and n"
READ X Y 

IF Y equals 0
 RETURN 1
ELSE IF Y%2 equals 0
 RETURN POWER(X,Y/2)*POWER(X,Y/2)
ELSE 
 RETURN X*POWER(X,Y/2)*POWER(X,Y/2)
END IF

DISPLAY POWER(X,Y)
