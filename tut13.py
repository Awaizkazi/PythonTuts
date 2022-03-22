# var1 = 6
# var2 = 56
# print('Enter a Number :')
# var3 = int(input())  # var3 bhi 1 integer ban gya
#
# if var3 >=var2:
#     print('Greater') # print ke pehle jo bhi hai usko hmm indentation bolte wo 1 tara se automatically tab jitna Space leleta hai
# else:
#     print('Lesser')


print('Enter your Age :')
userInput = int(input())
if userInput >18:
    print('Your are Eligible for Drive')
    print('Congratulations !!')
elif userInput ==18:
    print('Not Decided yet , Come Physically')
else :
    print('You are not Eligible for Driving')
