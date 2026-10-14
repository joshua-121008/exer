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
df=pd.read_csv("customers-100.csv")
print(df.to_string())








d
f
g








