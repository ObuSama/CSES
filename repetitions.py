import os
folder = os.getcwd()
with open(os.path.join(folder,"input/repetitions.txt")) as f:
    data = f.readlines()
    f.close()
string= data[0].strip()
def main(string):
    best, count = 0,1
    i,j = 0,1
    s = set()
    s.add(string[0])
    for each in string[1:]:
        if each == string[i]:
            count+=1
            j+=1
            best = max(best,count)
        else:
            i=j
            count = 1
            j+=1
    return best 

if __name__ == "__main__":
    print(main(string))

    

