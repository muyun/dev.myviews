
#### note  

#### 2020-03-17  
* fix the issue to display books.md 
  - Only get book page in pages 

* improve the frontend  
  - React ?  

* improve flask app 
  - organize Flask server  
  - bp? 

* reference
  - [react-flask](http://allynh.com/blog/adding-a-react-frontend-to-your-flask-project/)

#### 2020-03-14  
* TODO  
  - transfer books.md to html 
  - improve the layout  
  - pytest 

##### 2020-03-13  
* TODO 
  - design the layout  - fixed, need to improve  
  - pytest functions 

* Fixed 
  - add config_public.py for public setting

##### 2020-03-10  
* TODO  
  - flatpages in Flask  ?  
    + Done 
    + pages Works in jinjia templates, not in Flask 
     
  - pytest functions  
 

* use static not database to manage files
  - flatpages module  
  - sometimes flatpages dones't work in flask  - fix

* React ? 

#### deploy  
* test  
  > pytest  

* run  
  > export FLASK_APP=app.py
  > export FLASK_ENV=development  
  > flask run  


##### structure is the key  
* Modules 
  - modular programming - separating code into parts holding related data and function   
  - each module has its **own private symbol table**; 
  thus a module creates a **separate namespace**     
  - import <module_name>  -> only place <module_name> in the caller's symbole table  
  - dir() can find out which names a module defines  

* Packages  

* Test 
  - **what** was done - look at **the result** of a particular behavior   
  - a full **testing suite**  
  - each test unit must be fully **independent**  
  - **write a broken unit test about** what you want to develop next  

* Doc   

#### reference
* [Dead easy yet powerful static website generator with Flask](https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/)
* [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/writing/structure/)
* [Create a Static Blog Using Python Flask](https://dev.to/arrantate/create-a-static-blog-using-python-flask-1oab) 
* [pythonanywhere](https://www.pythonanywhere.com/user/muyun/)
* [Blask](https://getblask.com/)