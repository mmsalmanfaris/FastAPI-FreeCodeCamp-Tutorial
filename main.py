from fastapi  import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def root():
    return{"message": "Hello World!"}


@app.get("/post")
def get_posts():
    return {"data": "This is your posts"}


@app.post("/createpost")
def create_post(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}