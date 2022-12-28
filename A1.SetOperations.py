A = []
x = int(input("enter no of students who play cricket : "))
for i in range(0, x):
    A.append(input("Name of students who play cricket : "))
print(A)

B = []
y = int(input("enter no of students who play badminton : "))
for j in range(0, y):
    B.append(input("Name of students who play badminton  : "))
print(B)

C = []
z = int(input("enter no of students who play football : "))
for k in range(0, z):
    C.append(input("Name of students who play football : "))
print(C)


def AandB():
    AandB = []
    if (len(A) > len(B)):
        for i in range(x):
            for j in range(y):
                if (A[i] == B[j]):
                    AandB.append(A[i])
        print("Students who play both cricket and badminton : ", AandB)
    else:
        for j in range(y):
            for i in range(x):
                if B[j] == A[i]:
                    AandB.append(B[j])
        print("Students who play both cricket and badminton : ", AandB)
    return AandB

def AorB():
    AorB=[]
    for i in A:
        if i not in B:
            AorB.append(i)
    for j in B:
        if j not in A:
            AorB.append(j)
    print("Students who play either cricket or badminton but not both", AorB)

def onlyFB():
    onlyC=[]
    for k in C:
        if (k not in A) and (k not in B):
            onlyC.append(k)
    if len(onlyC)>0:
        print(len(onlyC), "students play neither cricket nor football")
        print("list: ", onlyC)
    elif len(onlyC) == 0:
        print("No student plays only Football, i.e. neither cricket, nor badminton")

def AandCnotB():
    AandCnotB =[]
    AandCnotB=A+C
    AandCnotB=list(dict.fromkeys(AandCnotB))
    for j in B:
        if j in AandCnotB:
            AandCnotB.remove(j)
    print(len(AandCnotB), "students play cricket and football but not badminton")
    print("list: ", AandCnotB)


AandB()
AorB()
onlyFB()
AandCnotB()