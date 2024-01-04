num1 = 2+3j

num2 = complex(2,3)

print(num2.real, num2.imag)

print(type(num1) == type(num2)) # True

if type(num2) == complex:
    print('Num 2 is a complex number of which ' + str(num2.real) + ' is the real part and ' + str(num2.imag) + ' is the imaginary part' )