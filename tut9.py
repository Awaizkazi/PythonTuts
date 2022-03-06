# Index      0           1         2        3        4        5
grocery = ["Harpic","Vim bar","deodrant","Bhindi","Lollypop",56]
# Indexing 0 se Start hoti hai 0,1,2,3,4,.....
# print(grocery[5])
numbers = [20,90,10,7,4,69]
# numbers.sort() #[4, 7, 10, 20, 69, 90]
# numbers.reverse() # [90, 69, 20, 10, 7, 4]
# jab hm Length Ginte hai toh wo 1 se Start karte hai 1,2,3,4,......
# print(numbers[2])
# Slicing me Jab 0 likho ya na likho apne aap wo lelega 1st : se pehele (Ex: 0:4) , Or agr mai 1st : ke baad koi number na likhu toh wo automatically Full Length Consider kar dega
# print(numbers[::2]) # [20, 10, 4] ye Print kardega wo 1 ko Skip kardega or gar mai 3 likhu toh  wo 2 ko Skip marega [20, 7] ye print karega
# print(numbers[::3]) # [20, 7] ye itna hi Print krega Q ke Usko uske aage numbers nhi mile hai
# print(min(numbers))

# numbers = []
# numbers.append(71)
# numbers.append(72) # append Jo hai wo end me add kardega wo
# numbers.append(73) # append means Last me ADD karna hai
# numbers.append(74) # [71, 72, 73, 74] new list me aaega wo bcwz usko Line wise me Wo mila hai New list blank wali
# print(min(numbers))
# print(numbers) #[20, 90, 10, 7, 4, 69, 71, 72, 73, 74]
# # To INSERT anywhere in the List
# numbers.insert(1, 34)
# numbers.remove(4) # [20, 34, 90, 10, 7, 69] # 1st is (Index , value)
# # to delete at last Index element
# numbers.pop() # [20, 34, 90, 10, 7]
# print(numbers) #[20, 90, 10, 7, 4, 69]
# if i insert with using Index
numbers[1] = 87
print(numbers)  #[20, 87, 10, 7, 4, 69] # it inserts a new Number at the index 1
# Mutable - Can Change Lsit are Mutable
# Immutable - Cannot Change , Tuples are Immutable

# Tuples it is Represented by () Parenthesis braces
tp = (1,2,3,4)
print(tp)
a = 1
b = 8
print(a,b)
a ,b = b , a
# temp = a
# a = b
# b = temp
print(a,b)
# or jab hmm 1 element ka Tuple Banate hai toh hmko (2,) Aisa likenge tb wo usko tuple smjega

