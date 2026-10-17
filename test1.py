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


students={"name":["joshua","leon","john","nishitha"],
          "age":[18,18,51,18],
          "cgpa":[3.5,3.6,3.7,3.8]
          }
a=pd.DataFrame(students,index=['a','b','c','d'])
a["medium"]=["english","english","english","english"]
a=pd.concat([a,pd.DataFrame({"name":["samuel","joshua"],"age":[20,21],"cgpa":[3.5,3.6],"medium":["english","english"]},index=['f','g'])])
##print(a)
##filter=a[a["age"]!=20]   



##print(a.mean(numeric_only=True ))

##print(a.max(numeric_only=True ))


##print(a.min(numeric_only=True ))
"""
"""
a["city"]=["hyderabad","bangalore","chennai","delhi","delhi","delhi"]
print(a)
c=a.groupby("city")
print(c)
print(c.mean(numeric_only=True))
"""
a={"name":["joshua","leon","john","nishitha","joshua","alton","inick","nivintham","samuvel raja","jolice","samuvel asirvatham","selvan","sam","john","john wesley","jeba","jason","simon","anush"],
   "age":[18,18,52,18,20,21,22,23,24,25,26,27,28,29,30,31,32,30,30],
   "rollnumer":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
   "city":["hyderabad","bangalore","chennai","delhi","delhi","delhi","delhi","delhi","delhi","delhi","delhi","delhi","delhi","delhi","delhi","delhi","delhi","delhi","delhi"],
   "role":["data analyst","data scientist","data engineer","data analyst","data scientist","data engineer","data analyst","data scientist","data engineer","data analyst","data scientist","data engineer","data analyst","data scientist","data engineer","data analyst","data scientist","data engineer","data analyst"]

   }
b=pd.DataFrame(a)
print(b)



