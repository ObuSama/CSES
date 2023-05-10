import os
folder = os.getcwd()
with open(os.path.join(folder,"input\missing_number.txt")) as f:
    data = f.readlines()
    f.close()

n = int(data[0].strip())

nums = [ int(x) for x in data[1].strip().split()]

def find_missing_number(n,nums):
    total = int(n*(n+1)/2)
    return total-sum(nums)
print(find_missing_number(n,nums))