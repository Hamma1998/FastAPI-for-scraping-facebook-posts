# FastAPI-for-scraping-facebook-posts
This is a Facebook scraping service that extracts and stores data in a NoSql database.

FastAPI instructions are used to create this service. It contains two functions that are accessible via get requests. The second is for collecting and storing information from Facebook posts.

Please keep in mind that this service is dockerized. You must first execute this command before you can run it. in your CLI:
```
docker build -t my-app .
````
Then, you run this second command:

```
docker run --network="host" my-app
```

To properly connect the database to the container, you must additionally install and run mongodb.

Go directly to the following URL to access the service through your browser:
```
http://0.0.0.0:8000/
```
Please add /docs to the above URL to get the Swagger default interface where you can find all of the functions included in the service:
```
http://0.0.0.0:8000/docs
```
You can access the function that scraps and stores data through the following URL (replace {post_main_topic} with the desired topic you want to include):
```
http://0.0.0.0:8000/scraping/{post_main_topic}
```
The repository includes as well a testing file that you can execute while running the container. 





