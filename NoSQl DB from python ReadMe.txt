NoSQl DB from python 

I have developed the assignment as been instructed

I have added specific commands

1- For creating database
create_db #dbname


2- For Selecting Database
change #dbname

3- For Show All database 
show db

4- for making table you need to select a database first from command number 2 and then ,
make #table_name #col1,col2,col3

5- For showing all the table 
show * table

6- for adding a new row, values in column can be less or equal to assigned column in a table, each time it will create a unique id and add the row with it
add #table_name #val1,val2

7- for printing whole table 
get #table_name *

8- for printing only one data with unique id
get #table_name #unique_id

9- for deleting data from table use unique id 
del #table_name #unique_id


It will save all the db dictionary to keyfile.txt

And it will load it every time


---------Improvements that can be Done -------------

I had to attend office so I created this a shorter version 

We could create class for most of the operation and global variabls which will increase
code readability and also will reduce repeatation 

There can be extra operations like when I am taking value as comma seperated value, I can 
actually take JSON object and assign values to columns exactly

In such way it will be actual no SQL cause then it wont have to specify a different entity that is no longer required

Right now when we are making any changes to db it saves all the data at once everytime, what we can improve is to make only some changes in file 
that is necessary, in that way this will be faster 

I have used dictionary for json view, we can use numpy also to make processing faster and then save it as json. 