from fastapi  import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_post = [{"title": "titel of post 01", "content" : "content of post 1", "id":1},
           {"title": "titel of post 02", "content" : "content of post 2", "id":2}]


def find_post(id):
    for p in my_post:
        if p['id'] == id:
            return p


@app.get("/")
def root():
    return{"message": "Hello World!"}


@app.get("/posts")
def get_posts():
    return {"data": my_post}


@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 100000)
    my_post.append(post_dict)
    return {"data": post}


@app.get("/posts/latest")
def get_latest_post():
    post = my_post[len(my_post)-1]
    return{"Latest" : post}


@app.get("/posts/{id}")
def get_post(id: int):

    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f"post with id:{id} was not found")
    return{"post_details" : post}