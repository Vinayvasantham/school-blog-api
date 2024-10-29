from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field
from bson import ObjectId
import os

# Initialize FastAPI app
app = FastAPI()

# MongoDB Connection
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["school_blog"]

# Pydantic Models for Validation
class BlogPost(BaseModel):
    title: str = Field(..., max_length=100)
    content: str = Field(..., min_length=5)
    author: str = Field(..., max_length=50)

class BlogPostDB(BlogPost):
    id: str

# Helper function to format MongoDB document
def format_doc(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

# Create a blog post

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/posts/", response_model=BlogPostDB)
async def create_post(post: BlogPost):
    result = await db.posts.insert_one(post.dict())
    new_post = await db.posts.find_one({"_id": result.inserted_id})
    return format_doc(new_post)

# Read all blog posts
@app.get("/posts/", response_model=list[BlogPostDB])
async def get_posts():
    posts = await db.posts.find().to_list(100)
    return [format_doc(post) for post in posts]

# Read a single blog post by ID
@app.get("/posts/{post_id}", response_model=BlogPostDB)
async def get_post(post_id: str):
    post = await db.posts.find_one({"_id": ObjectId(post_id)})
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return format_doc(post)

# Update a blog post by ID
@app.put("/posts/{post_id}", response_model=BlogPostDB)
async def update_post(post_id: str, post: BlogPost):
    result = await db.posts.update_one({"_id": ObjectId(post_id)}, {"$set": post.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    updated_post = await db.posts.find_one({"_id": ObjectId(post_id)})
    return format_doc(updated_post)

# Delete a blog post by ID
@app.delete("/posts/{post_id}", response_model=dict)
async def delete_post(post_id: str):
    result = await db.posts.delete_one({"_id": ObjectId(post_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}
