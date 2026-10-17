import pandas as pd
"""
students={
    "name":["joshua","john","leon"],
    "age":[20,21,22],
    "cgpa":[3.5,3.6,3.7]
}
#df=pd.DataFrame(students)
#print(df)
df=pd.DataFrame(students)
df["medium"]=["english","english","english"]
d=pd.DataFrame({"name":"alton","age":23,"cgpa":3.8,"medium":"english"
                ,"name":"alton","age":23,"cgpa":3.8,"medium":"english"},index=[3,4])
df=pd.concat([df,d], ignore_index=True)
print(df)


marks={"name":["english","maths","computer","physics","chemistry"],
       "marks":[81,46,87,53,54]
       }
df=pd.DataFrame(marks)
df["grade"]=["a","b","a","c","c"]
d=pd.DataFrame({"name":"biology","marks":67,"grade":"b"},index=[5])
df=pd.concat([df,d], ignore_index=True)
print(df)
"""
"""
df=pd.read_csv("customers-100.csv", index_col="Phone 2")
print(df)
##print(df.loc[2])

"""
students={"name":["joshua","leon","john","nishitha"],
          "age":[18,18,51,18],
          "cgpa":[3.5,3.6,3.7,3.8]
          }
a=pd.DataFrame(students,index=['a','b','c','d'])
a["medium"]=["english","english","english","english"]
a=pd.concat([a,pd.DataFrame({"name":["samuel","joshua"],"age":[20,21],"cgpa":[3.5,3.6],"medium":["english","english"]},index=['f','g'])])
print(a)
filter=a[a["age"]!=20]   
print(filter)







