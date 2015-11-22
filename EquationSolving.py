# Krzysztof Kuziel www.krzykustudio.pl
#  Solver linear equations using determinants
#    Ax+By=C 
#    Dx+Ey=F 

def message():
     print ("Wrong number")

print("To solve equation:")
print("Ax + By = C")
print("Dx + Ey = C")
print("Enter the coefficients: ")

setCoefficients = ['A','B','C','D','E','F']
coefficients = {}

for wsp in setCoefficients:
    while True:
        try:
            x = float(input("Enter " + wsp + ": "))
            coefficients[wsp]=x
            break
        except Exception:
            message()

print(coefficients)

# Cramers Rule
# determinant of the coefficient matrix
determinantW = coefficients['A'] * coefficients['E'] - coefficients['D'] * coefficients['B'] 
determinantWx = coefficients['B'] * coefficients['F'] - coefficients['E'] * coefficients['C']
determinantWy = coefficients['A'] * coefficients['F'] - coefficients['D'] * coefficients['C']

if(determinantW !=0):
    #to find the solution (x,y), we simply use our determinants:
    x = determinantWx/ determinantW
    y = determinantWy/ determinantW

    print("Our solution:")
    print("x: " + str(x) )
    print("y: " + str(y) )

elif(determinantWx == 0 and determinantWy ==0):
    #If determinantW = 0, and determinantWx = determinantWy = 0, then the system has infinitely many solutions
	print("System has infinitely many solutions.")
   
else:
	#If determinantW = 0, and at least one of determinantWx, determinantWy is non-zero, then the system has no solution. 
    print("System has no solution.")

	
try:
	input("Press Enter key to continue...")
except:
	pass