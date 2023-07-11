from psycopg2 import Binary 
import psycopg2 
from os import listdir
 
def Database(q,send=False): 
    conn=None 
    cur=None 
    try: 
        conn=psycopg2.connect( 
            database="demo", 
            user='postgres', 
            password="Naresh@123", 
            host="localhost", 
            port=5432 
        ) 
        cur=conn.cursor() 
        # fetch data---------------- 
        cur.execute(q) 
        if send: 
            conn.commit() 
            return True 
        else:  
            data=cur.fetchall() 
            return data 
 
    except Exception as e: 
        print(e) 
    finally: 
        if cur is not None: 
            cur.close() 
        if conn is not None: 
            conn.close() 
 
 
 
id=list(range(101,115)) 
name=['Digital Electronics','Computer Problem Solving','Communiocation Skills','Basic Math','Fundamentals of Computer','Inoerganic Chemistry','General Math','General Physics','Engineering Biology','Relational Database Managemnet System','Object Oriented Programming','Fundamnetals of Python','Computer Structural Architecture','Statistics'] 
for index,i in enumerate(id): 
    with open(f"img/{i}.png",'rb')as f: 
        Database(f"UPDATE subject SET title='{name[index]}',image={Binary(f.read())} WHERE subject_id={i}",send=True)