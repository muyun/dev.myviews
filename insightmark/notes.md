### notes

#### deploy  
* local  
  - use sqlite3 to develop  

* [onsite](https://insightmarks.herokuapp.com/)  
* db migration  
  > python manage.py db init  
  > python manage.py db migrate  
* commands:  
  > git commit -m "update" .  
  > git push heroku master  
  > heroku ps:scale web=1  
  > heroku open  
