
import pandas as pd

df = pd.DataFrame({
    "emp_name" :["vj","bj", "cj", "vij","bij", "cij"] 
    , "emp_no" : [1, 2, 3, 4, 5,6]})
df1 = pd.DataFrame({
    "emp_no": [1, 2, 3, 4, 5, 6],
    "salary": [20, 39, 34, 23 ,65, 48]
})

mer = pd.merge(df, df1, on="emp_no" )
right_join = pd.merge(df, df1, on="emp_no", how="right")
left_join  = pd.merge(df, df1, on="emp_no", how="left")
inner_join = pd.merge(df, df1, on="emp_no", how="inner")
outer_join = pd.merge(df, df1, on="emp_no", how="outer")

print(mer)
print()
print(right_join)
print()
print(left_join)
print()
print(inner_join)
print()
print(outer_join)
print()

print(f"mid value of the list = {mer["salary"].median()}")
print()
print(f"sum the all values = {mer["salary"].sum()}")
print()
print(f"find the mean value ={mer["salary"].mean()}")
print()
print(f"find the how many null values are there = {mer["salary"].count()}")  
print()
print(f"find the size of row {mer["salary"].size()}")

#secound heightest number
sorv= df1.sort_values("salary", ascending=False).iloc[2]
print(sorv)

# execute n numer of 

df.agg({'salary': 'mean', 'age': 'max'})