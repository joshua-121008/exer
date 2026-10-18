import pandas as pd
##series
"""
p=pd.Series({
    1:'john',
    2:'joshua',
    3:'jeba'
})
print(p.iloc[1])

p=pd.DataFrame({
    'name':["john","joshua","jeba"],
    "age":[52,18,42],
    "work":["late","college","teacher"]
}, index=["head","son","mother"])

p["native"]=["tvl","tvl","tuty"]
print(p)

d1=pd.DataFrame({
    "name":["nishitha"],
    "age":[18],
    "work":["college"],
    "native":["tuty"]
})
d=pd.concat([p,d1], ignore_index=True)

sales=pd.DataFrame({"fruit":["apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange","apple","banana","orange",],
                    "price":[100,50,80,20,45,100,50,80,20,45,100,50,80,20,45,100,50,80,20,45,100,50,80,20,45,100,50,80,20,45,100,50,80,20,45,100,50,80,20,45,100,50,80,20,45,100,50,80,20,45,100,50,80,20,45,100,50,80,20,45,54,65,66]

})
print(sales.fillna())
"""
a=pd.read_csv("insurance.csv")
print(a.query("age > 18 and age < 30"))
    