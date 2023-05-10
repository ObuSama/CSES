import os
folder = os.getcwd()
with open(os.path.join(folder,"input\increasing_array.txt")) as f:
    data = f.readlines()
    f.close()
n = int(data[0])
array = [ int(x) for x in data[1].strip().split()]
moves = 0
for i in range(1,n):
    while array[i]<array[i-1]:
        array[i]+=1
        moves+=1
    i+=1
print(moves)
