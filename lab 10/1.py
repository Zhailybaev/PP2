import psycopg2

con = psycopg2.connect(
  host="localhost",
  database="Phonebook",
  user="dia",
  password="passw0rd"
)
cur = con.cursor()
d=input()
if d=="1":
  i=input()
  s=input()
  n=input()
  cur.execute(f"INSERT INTO PHONE (ID,NAME,NUMBER) VALUES ({i}, '{s}' , {n})")
if d=="2":
  f = open('ex2.csv', 'r')
  cur.copy_from(f, 'phone', sep=',')
  f.close()

con.commit()  
print("Record inserted successfully")  

cur.execute('select * from phone where id >5')
stud = cur.fetchall()
print(stud)

cur.execute('select * from phone where number/1000>1')
st = cur.fetchall()
print(st)

cur.execute("DELETE FROM phone WHERE id = 2")
con.commit()

con.close()