# MetaMOOC
MetaMOOC is an online course recommendation system based on users entering preferences.

## Installation
1. Download the source code.
2. Setup the database. Currently only MySQL is tested, but any DB compatible with sqlalchemy should work.
(If you use another DB, you may need to edit db.py.) You will need to create users metamooc_ro and metamooc_rw.
Create a database metamooc with character set utf8 (using latin-1 is likely to cause problems with non-English
course titles). metamooc_rw needs all permissions the database; metamooc_ro just needs SELECT.
Create a file password.py containing the database password (e.g. the file should contain 

        password = '12345'
    
3. Now you should run the scripts scrape_coursera.py and scrape_coursetalk.py. 
