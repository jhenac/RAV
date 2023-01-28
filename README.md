# RAV
Replicated the rav website and tried to incoporate sql database in the data storage.

This project was created for the technical exam for RAV. The problem was broken down to two parts: 1) to replicate the website 2) to use crud api in querying data
from a database.

I used flask to replicate the website and everything seems to be working fine. Below is the screenshot of the website on the flask development server:
![image](https://user-images.githubusercontent.com/98466796/215246137-b7858c87-0fda-4557-88b7-279e1656574d.png)


My next problem was to change the static data into dynamic values to be stored in a database. I had no prior experience with database management so I watched and read up on sql, installed sql server, installed xampp, made the necessary imports to my flask app using sqlalchemy. Everything was going smoothly until I tried to create tables from the app and encountered ERROR 1045. I spent an ungodly amount of time trying to get rid of the error. After maybe four hours of deepdiving into stackoverflow alternating keywords between flask, flask shell, sql and sql alchemy, I got rid of the error and was able to create the table columns as can be seen below:

![image](https://user-images.githubusercontent.com/98466796/215243235-5afa934e-6c73-4e40-bb31-9b2909ba4b94.png)


Sadly, I don't have much time to proceed with the next steps as the deadline for submission was nearing. The goal was to be able to create, read and update data using
resident ID. From my initial analysis, the base pay is based on the current cost of the services of certain facility/hospital and the diagnosis. Total(4-20) is the sum
of of the cost of PT, OT, SLP, and Nursing. Additional cost incurred will depend on a lot of other factors such as days staying in the hospital and other extra 
services required. 

I will need additional time to analyze the data and figure out how they are connected to each other. This was a very big task but overall I had a lot of fun trying
to solve this as best as I can. 
