
#### note  

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

#### deploy  
* test  
  > pytest  

* run  
  > export FLASK_APP=blog
  > export FLASK_ENV=development  
  > flask run  


#### reference
* [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/writing/structure/)
* [Create a Static Blog Using Python Flask](https://dev.to/arrantate/create-a-static-blog-using-python-flask-1oab) 
* [pythonanywhere](https://www.pythonanywhere.com/user/muyun/)
* [Blask](https://getblask.com/)