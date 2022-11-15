# Declare & Assign Variable in python
int_var = 10
float_var = 18.25
string_var ="RAVEESH J" # or another way 'RAVEESH J'
bool_var = True # if we want to assin false it's False

# Function in python for output
# Function Dose What ? They might or might not Accept som parameter
print("Hello World")

# Print Variable Values
print("value of int_var =",int_var)
#OR
print("value of int_var =",int_var,"-Result Done !!")


print("value of float_var =",float_var)
#OR
print("value of float_var =",float_var,"-Result Done !!")


print("value of string_var =",string_var)
#OR
print("value of string_var =",string_var,"-Result Done !!")


print("value of bool_var =",bool_var)
#OR
print("value of bool_var =",bool_var,"-Result Done !!")

# How to Check data type of any variable in python
# We can use type() Function
print("type of int_var ?",type(int_var))
print("type of float_var ?",type(float_var))
print("type of string_var ?",type(string_var))
print("type of bool_var ?",type(bool_var))

# How to do the type casting in Python
# int(), float(), str(), bool()
int_var = int_var + 10 # int_var = 10 + 10 in next step int_var = 20

casted_int_var = float(int_var)
print("int to float typecasting for int_var =", casted_int_var)

casted_float_var = int(float_var)
print("Float to Int typecasting for float_var =", casted_float_var)

Numeric_str = "123"
#Numeric_str = Numeric_str + 50 # its NOt Vallied..!!
Numeric_str = int(Numeric_str) + 50
print("value of Numeric_str =", Numeric_str)
