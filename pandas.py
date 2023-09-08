import pandas as pd

# Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
# Accessing elements by index
print(series[2])  # Output: 30

s=pd.Series([15,"ravi",3.14,"rohit"])
print(s)

#adding indexing to the s   like a b c d instead of o 1 2 3  ,,and to remove index write index=false
s1=pd.Series([15,"ravi",3.14,"rohit"], index=["a","b","c","d"])
print(s1)
print(s1["a"])



data1={

"Studentname":["ravi","yash","rohit"],
"Mathmark":[90,50,60],
"Sciencemark":[69,60,60],
"Sport":["kabbadi","cricket","swimming"]
}

st=pd.DataFrame(data1,columns=["Studentname","Mathmark","Sciencemark","Sport"])
#no need to add the colomns name
print(st)
print(st.drop([0]))#use to drop the zero no. row
print(st.drop(['Studentname','Sciencemark'],axis=1,inplace=True))#drop the specific colomn
#or u also use
#print(st["Mathmark","Sport"].head()) #sovle the error

#exporting the file into the csv
#print(st.to_csv('data2friend.csv'))

#reading the csv file using pandas
print(pd.read_csv('BOOK1.csv'))

#now changing the colomn name 
print(pd.read_csv('Book1.csv',names=['naav','kimmat','available'],header=0))

#--------------------------------------------------------------

users=pd.read_csv('ml-100k/u.user',sep='|',names=["user_id","age","gender","occupation","zipcode"])

#print(users.head())
#head print the first five line of data

#print(users.tail())  #last five line

#.............

#colomns_i_want=["age","gender"]#["user_id","zipcode"]
#print(users[colomns_i_want].head())

#........

#now we adding some condition in this 

#print(users[(users.age<40) & (users.gender=='M')].head())
#print(users[(users.age>18) & (users.occupation== 'writer')].tail())

#...........

#now we defines the dtypes and describe it in details
#print(users.dtypes)# users colomns data types
#print(users.describe())# describe(is the method) all the things in details  like count,mean,std,min,.....

#................

#now set the index as the user_id
#print(users.set_index(user_id).head())# sovle the error

#...........................

frame1=pd.DataFrame({'key':range(5)})
frame1=pd.DataFrame({'key':range(5),'f1':["a","b","c","d","e"]})
frame2=pd.DataFrame({'key':range(2,7),'f2':["t","u","v","w","x"]})
#print(frame2)#print(frame1)
#print(pd.merge(frame1,frame2,on='key'))#combine common element from both frames # 
# but when there is no common in frame1 and frame2 then they print empty dataframe with key f2 

print(pd.merge(frame1,frame2,on='key' ,how='right'))#in this they show all element in right/left and 
# some common element in left and non common with NAN


print(pd.merge(frame1,frame2,on='key',how="inner"))#comman element

print(pd.merge(frame1,frame2,on='key',how="outer"))

print(pd.concat([frame1,frame2]))#this will add both frame1 and frame2 but one and other bleow
print(pd.concat([frame1,frame2],axis=1))#this also add both but in the same colomn wise 







