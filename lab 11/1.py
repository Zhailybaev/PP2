import psycopg2

con = psycopg2.connect(
  host="localhost",
  database="Phonebook",
  user="dia",
  password="passw0rd"
)
cur = con.cursor()
#d=input()
#if d=="1":
#  i=input()
#  s=input()
#  n=input()
#  cur.execute(f"INSERT INTO PHONE (ID,NAME,NUMBER) VALUES ({i}, '{s}' , {n})")
#if d=="2":
#  f = open('ex2.csv', 'r')
#  cur.copy_from(f, 'phone', sep=',')
#  f.close()

#con.commit()  
#print("Record inserted successfully")  

#1.Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)
cur.callproc('filter',['st',])
p=cur.fetchall()
print(p)

#2.Create procedure to insert new user by name and phone, update phone if user already exists
cur.execute('CALL insert_user(%s,%s,%s)', (18,'lop', 356))

#3.Create procedure to insert many new users by list of name and phone. Use loop and if statement in stored procedure. Check correctness of phone in procedure and return all incorrect data.
cur.callproc('list')

#4.Create function to querying data from the tables with pagination (by limit and offset)
cur.callproc('qwe')
g=cur.fetchall()
print(g)

#5.Implement procedure to deleting data from tables by username or phone
cur.execute('CALL delete_user(%s)', ('abc',))


#cur.execute('select * from phone where id >5')
#stud = cur.fetchall()
#print(stud)

#cur.execute('select * from phone where number/1000>1')
#st = cur.fetchall()
#print(st)

#cur.execute("DELETE FROM phone WHERE id = 2")
con.commit()

con.close()