from random import Random
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_post = [{"title": "Title Post Pertama", "content": "Content dari Perttama",
            "id": 1}, {"title": "Fav of Food", "content": "She Like Chicken", "id": 2}]


def find_post(id):
    for p in my_post:
        if p["id"] == id:
            return p


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/post")
def get_posts():
    return {"data": my_post}


@app.post("/post")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    my_post.append(post_dict)
    return{"data": post_dict}


@app.get("/post/{id}")
def get_post(id: int):

    post = find_post(id)
    print(post)
    return{"post_detail": post}
