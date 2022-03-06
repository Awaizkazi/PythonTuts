mystr = 'Harry is A Good boy'
print(len(mystr)) # 19
# print(mystr[0:90])
# Python me Index jo hai wo 0 se start hoti hai
# String Slicing ka role hota hai wo ki agar hm 0 :4 likte hai toh wo 0 including hoga or 4 Excluding Hoga

# Advanced Slicing
# print(mystr[::9999])
# jab mai 3rd Colon me :2 last me Likunga tb wo 1 ,1 Char skip karke Print karega // Hry ye print karega wo
# or jab mai 3rd colon : me 1 Dalunga tb wo puri String ko Print kar dega bcwz wo by default 1 hi reta hai toh isliye Hmko Skip karna agar 1 ,1 Char toh hm 3rd Colon me 2 likenge hmm or agar hmko 2,2 Char skip karna hai toh hm 3 likhenge 3rd Wale Column me
# or agar mai glti se ya jaan buj ke 9 Likdu 3rd : me tb wo jaha tk ka Resolve kar payega utna karke Dedega agar Chars Khatam ho jae toh wha tk ka Skip karke dega Jitne Chars ho Usme  , OR Agar mai koi bada Number likdu tb bhi Wo jitna Resolve kar payega utna Return kar dega wo Ex= :5599 it prints H Bcwz by default wo :1st Colon jo Likhe wo Wo usko Print karega hi

# print(mystr[::-2])
#Tb wo Puri String ko reverse Kardega, Ulta kardega or fir wo 1 ,1 Char skip karega
print(type(mystr)) #<class 'str'>
print(mystr.isalpha()) #False
print(mystr.endswith('boy')) #True
print(mystr.count('o')) #3
print(mystr.capitalize()) # Harry
print(mystr.find('is')) #6 6 Q ki wo i 6th position se Start hua hai is ka i
print(mystr.lower()) #harry is a good boy
print(mystr.upper()) #HARRY IS A GOOD BOY
print(mystr.replace('is', 'are')) #Harry are A GOod boy
print(mystr,format('boy')) #Harry is A Good boy boy
print(mystr.rfind(12))