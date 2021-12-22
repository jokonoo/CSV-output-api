## This is another task I did as part of the recruitment process.

###It is a simple app that scrape data from api, and generate CSV format file with all results.

### Methods:

## There is only one endpoint that do both scraping data and passing response with generated file

#### GET/app/user_task

This method is calling function that scrapes data, write data to SQLite database,
and it's writing results to file. File is downloading automatically.
