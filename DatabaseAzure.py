#!/usr/bin/env python
# coding: utf-8

# In[5]:


import mysql.connector


# In[6]:


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Inidara",
  database="test"
)


# In[7]:


mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


# In[8]:


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM centable ")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# In[10]:


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM centable WHERE STATES='Imo'")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# In[7]:


import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
  'host':'cen2021.mysql.database.azure.com',
  'user':'Toiletsanitaton@cen2021',
  'password':'jo*el!eg1',
  'database':'INI'
}

# Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()
  # Cleanup
  conn.commit()
#   cursor.close()
#   conn.close()
#   print("Done.")


# In[8]:


# Read data
#conn.open()
cursor = conn.cursor()
cursor.execute("SELECT * FROM centable1;")
rows = cursor.fetchall()
print("Read",cursor.rowcount,"row(s) of data.")

  # Print all rows
for row in rows:
    print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))


# In[10]:


# Update a data row in the table
cursor = conn.cursor()
cursor.execute("UPDATE centable1 SET STATES = %s WHERE ID = %s;", (12, "EDO"))
print("Updated",cursor.rowcount,"row(s) of data.")


# In[11]:


import pandas as pd
import ipywidgets as widgets
from IPython.display import display
df_london = pd.read_csv(r'C:\Users\inida\OneDrive\Documents\400 lvl notes\Alpha\CEN 414\SQL\centable.csv')
#print(df_london)
ALL ='ALL'
def unique_ALL(array):
    unique = array.tolist()
    unique.sort()
    unique.insert(0,ALL)
    return unique
dropdown_state = widgets.Dropdown(options=unique_ALL(df_london.STATES))
output_year = widgets.Output()
def dropdown_year_eventhandler(change):
    output_year.clear_output()
    with output_year:
        if(change.new == ALL):
            display(df_london)
        else:
            display(df_london[df_london.STATES == change.new])
dropdown_state.observe(dropdown_year_eventhandler,names='value')
display(dropdown_state)


# In[13]:


dropdown = widgets.Dropdown(options=(1,2,3))
display(dropdown)


# In[ ]:




