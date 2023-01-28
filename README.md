# RAV
Replicated the rav website and tried to incoporate sql database in the data storage.

This project was created for the technical exam for RAV. The problem was broken down to two parts: 1) to replicate the website 2) to use crud api in querying data
from a database.

I used flask to replicate the website and everything seems to be working fine. Below is the screenshot of the website on the flask development server:
![image](https://user-images.githubusercontent.com/98466796/215243005-2866dfde-2914-4084-8c72-6e23b98d0422.png)

My next problem was to change the static data into dynamic values to be stored in a database. I had no prior experience with database management so I watched and read up on sql, installed sql server, installed xampp, made the necessary imports to my flask app using sqlalchemy. Everything was going smoothly until I tried to create tables from the app and encountered ERROR 1045. I spent an ungodly amount of time trying to get rid of the error. After maybe four hours of deepdiving into stackoverflow alternating keywords between flask, flask shell, sql and sql alchemy, I got rid of the error and was able to create the table columns as can be seen below:
![image](https://user-images.githubusercontent.com/98466796/215243235-5afa934e-6c73-4e40-bb31-9b2909ba4b94.png)

Sadly, I don't have much time to proceed with the next steps as the deadline for submission was nearing. Looking through the table 
