import test
import smtplib, ssl
import sqlite3
import re
import time 
from credits import cemsaylam, yagiz, buko, emre, berdo,gunes,db_location,omer,sender_password,sender



def get_time():
    seconds = 1545925769.9618232
    local_time = time.ctime(seconds)
    date_scrap = time.asctime( time.localtime(time.time()) ) # parameter 1
    return date_scrap

def get_dollar_value():
    x = test.dolar()
    extracted_number_list = re.findall("\d+.\d+",x)
    extracted_number = extracted_number_list[0]
    extracted_number = extracted_number.replace(",",".")
    result = float(extracted_number)

    return result

def connection_db(database_name,entites):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    ex = "create table if not exists dollar (date text, val_tl integer);"
    cursor.execute(ex)
    cursor.execute("insert into dollar (date,val_tl) values (?,?)",entites)
    #db_message = "databese is connected."
    connection.commit()
    
    cursor.execute("SELECT * FROM dollar order by rowid desc;")
    rows = cursor.fetchall()
    result = "     DATE                           VALUE\n"
    rows_length = len(rows)
    for x in range(rows_length):
        result = result + (rows[x][0])+"           "+ str(rows[x][1])+"\n"
    
    
    return result


dol_tl = get_dollar_value()
date_n = get_time()
entites = (date_n,dol_tl)
def check_difference(db_name, new_val):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("select * from dollar;")
    rows = cursor.fetchall()

    vals = []
    for x in rows:
        vals.append(x[1])

    diff = vals[len(vals) - 1] - new_val
    diff = abs(diff)  
    return diff
     




message = test.dolar() # get the message from website



difference = check_difference(db_location, dol_tl)

if difference > 0.100:
    a =  connection_db(db_location,entites)


    


    message = message + "\n===\n\nMERHABA dolar dusuyor mu ?\n===\n" +a
    
    port = 465 #for SSL
    smtp_server = "smtp.gmail.com"
    sender_email = sender # Enter your address
    receiver_email = omer  # Enter receiver address
    password = sender_password

    subject = "Subject: Notificiation\n"
    subject = subject + message
    message = subject
    message = message.encode('ascii','ignore').decode('ascii')
    context = ssl.create_default_context()






    while 1 == 1:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            server.sendmail(sender_email,yagiz,message)
            server.sendmail(sender_email,berdo,message)
            server.sendmail(sender_email,buko,message)    
            server.sendmail(sender_email,emre,message)
            server.sendmail(sender_email,cemsaylam,message)
            server.sendmail(sender_email,gunes,message)


else:
    print("nothing added to database")