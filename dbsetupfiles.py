#________________________________________________________________________________________________________________________________

'''                                                    INPORTING MODULES/DATABASE CONNECTION                                                   '''
#________________________________________________________________________________________________________________________________         


                        
import sqlite3 as sq
conn = sq.connect("Shinechem.db")
cursor = conn.cursor()


#________________________________________________________________________________________________________________________________

'''                                                       TABLES                                                              '''
#________________________________________________________________________________________________________________________________         
                        

cursor.execute("""CREATE TABLE if not exists Product_purchase(
               S_no integer AUTOINCREMENT,
               product_code INTEGER PRIMARY KEY,
               prod_name text,
               hsn integer,
               pack integer,
               manf_date date,
               exp_date date,
               qty integer,
               price real,
               );""")
conn.commit()
cursor.execute("SELECT * Product_purchase;")
print(cursor.fetchall())

# """CREATE TABLE if not exists Clients(
#                 INTEGER PRIMARY KEY,
#                name text,
#                manf_date date,
#                exp_date date,
#                qty integer,
#                price real);"""



#________________________________________________________________________________________________________________________________

'''                                                          Functions                                                        '''
#________________________________________________________________________________________________________________________________         
 
def add_product():
    name = str(input("Enter Your Name:-"))
    age= int(input("Enter Your age:-"))
    aim= str(input("Enter Your aim:-"))
    cursor.execute("INSERT INTO filedata values(NULL,?,?,?);",(name,age,aim))
    conn.commit()
    print("inserted successfully...")
    conn.close()
     
#________________________________________________________________________________________________________________________________

'''                                                          GUI                                                        '''
#________________________________________________________________________________________________________________________________         


tkinter.messagebox.showinfo('Window Title',"DO Need a break have KITKAT LOL!")
answer = tkinter.messagebox.askquestion('Question 1',"DO you Like ML?")

if answer =='NO':
    tkinter.messagebox.showinfo('LOL',"HAHA")
else:
    tkinter.messagebox.showinfo('LOL',"BHAG yaha se")          