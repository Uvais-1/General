import sqlite3 #importing sqlite3 library

#create database
con=sqlite3.connect("Movies.db") #create database
c=con.cursor()

#create table Movies
c.execute('''create table Movies(Movie_Name varchar(100) primary key,Lead_Actor varchar(100),Lead_Actress varchar(100),Year_of_Release integer,Director varchar(100))''')

#Insertion of values
c.execute('''insert into Movies values('KGF 2','Yash','Srinidhi Shetty',2022,'Prashanth Neel')''')
c.execute('''insert into Movies values('Spider-Man:No Way Home','Tom Holland','Zendaya',2021,'Jon Watts')''')
c.execute('''insert into Movies values('Spider-Man:Far From Home','Tom Holland','Zendaya',2019,'Jon Watts')''')
c.execute('''insert into Movies values('PK','Amir Khan','Anushka Sharma',2014,'Rajkumar Hirani')''')
c.execute('''insert into Movies values('Dangal','Amir Khan','Fathima Sana Shaikh',2016,'Nitesh Tiwari')''')
c.execute('''insert into Movies values('Secret Superstar','Amir Khan','Zaira Wasim',2017,'Advait Chandan')''')
c.execute('''insert into Movies values('Drishyam','Mohan Lal','Meena',2013,'Jeethu Joseph')''')
c.execute('''insert into Movies values('M.S.Dhoni:The Untold Story','Sushanth Singh Rajpoot','Kiara Advani',2016,'Neeraj Pandey')''')
c.execute('''insert into Movies values('83','Ranveer Singh','Deepika Padukone',2022,'Kabir Khan')''')
c.execute('''insert into Movies values('Zero','Shah Rukh Khan','Anushka Sharma',2018,'Anand L Rai')''')
c.execute('''insert into Movies values('Beast','Vijay','Pooja Hegde',2022,'Nelson')''')
c.execute('''insert into Movies values('Tiger Zinda Hai','Salman Khan','Katrina Kaif',2017,'Ali Abbas Zafar')''')
c.execute('''insert into Movies values('Kabir Singh','Shahid Kapoor','Kiara Advani',2019,'Sandeep Reddy Vanga')''')
c.execute('''insert into Movies values('RRR','Ram Charan','Alia Bhat',2022,'S.S.Rajamouli')''')
c.execute('''insert into Movies values('Moonfall','Patrick Wilson','Hally Berry',2022,'Roland Emmerich')''')
con.commit() #commit the data inserted

#fetch data from Database
data=c.execute('''select * from Movies''').fetchall() #fetch all data
actor_data=c.execute('''select * from Movies where Lead_Actor='Amir Khan' ''').fetchall() #fetch movies acted by Amir Khan

#print the results
print(data)
print(actor_data)