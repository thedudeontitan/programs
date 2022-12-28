data=[]
x=int(input("Enter number of elements"))
for i in range (0,x):
    data.append(input("enter data elements"))
    
print("unsorted list = ",data)

def bubblesort(data):
    for i in range (x-1,0,-1):
        for j in range (i):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]


def incersionsort(data):
    for i in range(1,x):
        j=i
        while data[j-1]>data[j] and j>0 :
            data[j-1],data[j]=data[j],data[j-1]
            j=j-1


def selectionsort(data):
    for i in range (0,x-1):
        min=i
        for j in range(i+1,x):
            if data[j]<data[min]:
                min=j
        data[i], data[min]=data[min] , data[i]


print("\nchoose 1 for bubble sort\nchoose 2 for incersion sort\nchoose 3 for selection sort")
p=int(input("choose"))
if (p==1):
    bubblesort(data)
    print("sorted : ",data)
elif (p==2):
    incersionsort(data)
    print("sorted : ",data)
elif (p==3):
    selectionsort(data)
    print("sorted : ",data)
