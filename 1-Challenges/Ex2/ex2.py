# Richiedi all'utente di inserire un numero in virgola mobile (double)
input1 = input("first integer number: ")
n1 = int(input1)

input2 = input("second integer number: ")
n2 = int(input2)

print("\n0: addizione\n1: sottrazione\n2: moltiplicazione\n3: divisione\n")
operation_type = input("number associated to the operation: ")
operation = int(operation_type)

if operation == 0:
    print("solution = ", n1 + n2)
elif operation == 1:
    print("solution = ", n1 - n2)
elif operation == 2:
    print("solution = ", n1 * n2)
if operation == 3:
    print("solution = ", n1 / n2)