import pandas as pd
#firstly we see about the series data ****
#in this u also add the index,names,....

data2=['ravi',23,9.33]
sd=pd.Series(data2)
print(sd)


#now we see the Dataframes by using set and dictionary... ****
data3={
 "studentname":['ravi','rohit','yash','mohit','ravi'],
 "rollno":[10,12,33,44,10],
 "mark":[23,33,44,55,23]
}

st=pd.DataFrame(data3)
print(st)


#now we see the reading csv ,changing colomn name ,/index and exporting csv and many operation ****
print(pd.read_csv('Book1.csv'))
#print(pd.read_csv('Book1.csv',names=['col1','col2','col3']))
#now exporting the data2_1 into the csv

#print(st.to_csv('data3friend.csv'))#must be define st name #export

#now print the colomn that u want to print
#tail ,head,describe,....  dtype#is not a function
#condition print(users[(users.1st condition) & (users.2nd condition)])


#..........colomn_i_want=['ravi','rohit']
#...........print(st[colomn_i_want])


users=pd.read_csv('ml-100k/u.user',sep='|',names=["user_id","age","gender","occupation","zipcode"])

colomns_i_want=["age","gender"]#["user_id","zipcode"]
print(users[colomns_i_want].head())
#print(st.drop([0]).head())...........................


#the names must be in double quate "" not in single ' '  ............
#users=pd.read_csv('ml-100k/u.user',sep='|',names=["user_id","age","gender","occupation","zipcode"])





#now learn about the merge funtion to merging the dataframes ****
#right ,left ,inner ,outer
#frame1=pd.DataFrame({'key':range(5),'f1':["a","b","c","d","e"]})
#frame2=pd.DataFrame({'key':range(2,7),'f2':["t","u","v","w","x"]})
#print(pd.merge(frame1,frame2,on='key' ,how='inner'))




#sorting the data according to colomn
print(users.sort_values(by='user_id')) 
#not define True as like 'true' this
#and remove the,inplace=True to sovle the error

#drop the dublicate rows 
print(st.drop_duplicates())


#group by use to add a group a one or more colomns and perform some operation on this
#print(st.groupby('mark').mean()).........
#print(st.groupby(['mark', 'name']).size().reset_index(name='Count'))......


#count the values
#print(st['mark'].value_counts())

#print(st.loc[1,3])
#loc is use to print the selected rows and coloms
#print(users.loc[0:6 ,["user_id","age"]])
#print(users.iloc[0:6])# only for rows and not include the last element


