class Reverse:
    def __init__(self,str):
        self.vowel_count=sum([1 if z.lower() in ['a','e','i','o','u'] else 0 for z in str])
        self.rev=list(reversed(str.split()))

a=Reverse(input("Enter the 1st string\n"))
b=Reverse(input("Enter the 2nd string\n"))
c=Reverse(input("Enter the 3rd string\n"))

p=sorted([(x.rev,x.vowel_count) for x in [a,b,c]],key=lambda s:s[1],reverse=True)
print("Output is :\n",p)
