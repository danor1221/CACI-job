# CACI-job
Solution to the data engineer challenge

## Contents
There are various python files contained above. generateTables.py and sanitiser.py contain functions that build and clean the tables in the database. SQLDatabase.db is a database that has been 
created and sanitised. fraudData.py, transaction001Data.py, and transaction002Data.py are data files that contain the raw data used to build the sql databse. testFile.py contains the unittest
framework.

## Usage
Opening and running the file marked getReports.py will connect to the database and extract the desired fradulent data. Running the function in reportPlot.py will plot these fradulent transactions by
state and by vendor.
There is no need to run the function within generateTables.py as this creates a database and the three tables contained within and has already been run. Similarly the function within sanitiser.py
does not need to be run as it already has and has removed desired transactions from transaction-001 and transaction-002. Sanitiser.py also adds a fourth column marked 'vendor' to make later
stages easier. If you would like to experiment with these functions, you can change the database name from SQLDatabase.db to something else (eg. SQLDatabase01.db) and run them making sure
to run them in the correct order (generateTables.py->sanitiser.py->getReports.py->reportPlot.py).