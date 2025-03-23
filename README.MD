### deployment
-various env. in development
1.Development env.
2.Staging env.
3.Production env.

-Build process: compile the code into an executeble format
-Testing : verifying the required qualities
-Release : Deploy the softwarae to the designed env. (live env.)
-Monitoring : Enquiring the software operates as expected and resolving any issues

### Considerations when selecting a deployment services
1.Infrastructure requirements : scalability and performance
2. Supported technologies: ensure compatibility with tech stack
3. Deployment model : a. cloud based: b. on-premise: c. hybrid
4. Automation : continuous intergration / continuous deployment
5. Monitoring analytics : logs
6. costs and ease of use



### Steps to deploy this project
1. prepare the django application
2. setup static files for production : python manage.py collectstatic
3. create a requirements.txt file : pip freeze > requirements.txt : lists all dependencies used
4. create runtime.txt files : specify the type of python uses
5. install gunicorn : pip install gunicorn 
6. df
7. push code to github



### on render 
1. create a new web service
2. connect it to github acc
3. add build commmands
4. add start commands
5. ensure the env is set to the python