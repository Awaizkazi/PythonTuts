# Dictionary is nothing but a key value pairs
d1 = {}
# print(type(d1))
d2 = {"Harry": "Burger","Rohan": 'Fish','SkillF':'Roti',"Shubham":{"B":"maggie","L":"roti","D":"Chicken"}}
# print(d2['Harry']) #Burger ,harry kya khata hai usne wo print kara hai Harry Burger khata hai H Capital hai agar Dict me toh usko hame wesa hi dena hoga Q ki wo Case Sensitive hai
# print(d2["Shubham"]["B"]) #{'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}
# d2["Ankit"] = "Junk Food"
# d2[420] = "Kebabs"
# # For delete the value  By using Key
# print(d2)#{'Harry': 'Burger', 'Rohan': 'Fish', 'SkillF': 'Roti', 'Shubham': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Ankit': 'Junk Food', 420: 'Kebabs'}
# del d2[420] #{'Harry': 'Burger', 'Rohan': 'Fish', 'SkillF': 'Roti', 'Shubham': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Ankit': 'Junk Food'}
# print(d2) #{'Harry': 'Burger', 'Rohan': 'Fish', 'SkillF': 'Roti', 'Shubham': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Ankit': 'Junk Food', 'Aurangzeb': 'Kebabs'}
# d3 = d2.copy() # toh yha pe d3 1 new Dictionary nhi banri hai wo d2 ka hi reference krti hai agar mai d3 ka name use krke Insert,Delete krta hu toh Wo d2 me bhi changes ho jaate hai
# del d3["Harry"] #{'Harry': 'Burger', 'Rohan': 'Fish', 'SkillF': 'Roti', 'Shubham': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}}
# print(d2)    # Or agar aisa naa ho ho toh hmm .copy Function use karte hai
# d2.update({'Leena':'Toffee'})
# print(d2.get('Harry')) #Burger
# print(d2) #{'Harry': 'Burger', 'Rohan': 'Fish', 'SkillF': 'Roti', 'Shubham': {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}, 'Leena': 'Toffee'}
print(d2.keys()) #dict_keys(['Harry', 'Rohan', 'SkillF', 'Shubham'])
print(d2.items()) # ye return karta hai Key:vakue pairs ko , #dict_items([('Harry', 'Burger'), ('Rohan', 'Fish'), ('SkillF', 'Roti'), ('Shubham', {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'})])
print(d2.fromkeys('Rohan'))
