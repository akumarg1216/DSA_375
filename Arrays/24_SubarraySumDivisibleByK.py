#def subarraysDivByK(self, nums):
A = [4,5,0,-2,-3,1]
K = 5
count=0
res = 0
prefix = 0
count = [1] + [0] * K
print("Count: ",count)
for a in A:
    print("A= ",a)
    print(prefix)
    prefix = (prefix + a) % K
    print("Prefix = ",prefix)
    res += count[prefix]
    print("Result = ",res)
    count[prefix] += 1
    print(f"Count[{prefix}] = {count[prefix]}")
    print("*************************************")
print(res)




#subarraysDivByK(nums=nums)