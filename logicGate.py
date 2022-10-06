gate = input("Enter logic gate: ")
fir = int(input("Enter first input: "))
sec = int(input("Enter second input: "))

def OR(A, B):
	return A | B
def AND(A, B):
	return A & B
def NOT(A):
	return ~A+2
def NAND(A, B):
	return NOT(AND(A, B))
def NOR(A, B):
	return NOT(OR(A, B))
def XOR(A, B):
	return A ^ B

match gate.upper():
    case "OR":
        print(OR(fir, sec))
    case "AND":
        print(AND(fir, sec))
    case "XOR":
        print(XOR(fir, sec))
    case "NAND":
        print(NAND(fir, sec))
