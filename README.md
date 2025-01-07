# School Blog API

A simple RESTful API for managing blog posts, built with FastAPI and MongoDB. The API provides CRUD operations for creating, reading, updating, and deleting blog posts.

## Features

- Create a blog post
- Retrieve all blog posts
- Retrieve a single blog post by ID
- Update a blog post by ID
- Delete a blog post by ID

## Requirements

- Python 3.10+
- MongoDB instance
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/school-blog-api.git
   cd school-blog-api

2. Create a virtual environment and activate it:

3. Install the required dependencies:

4. Set up your MongoDB connection:
- Ensure MongoDB is running locally or accessible remotely.
- Create a `.env` file in the project root and add the following:
  ```
  MONGO_URL=mongodb://<username>:<password>@<host>:<port>/<database>
  ```

5. Start the FastAPI server:

6. Access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## API Endpoints

### Root Endpoint
- **GET `/`**
- Returns a welcome message.

### Blog Posts
- **POST `/posts/`**
- Create a new blog post.
- Request body:
 ```
 {
   "title": "Blog Title",
   "content": "Blog content...",
   "author": "Author Name"
 }
 ```
- Response:
 ```
 {
   "id": "post-id",
   "title": "Blog Title",
   "content": "Blog content...",
   "author": "Author Name"
 }
 ```

- **GET `/posts/`**
- Retrieve all blog posts.
- Response:
 ```
 [
   {
     "id": "post-id",
     "title": "Blog Title",
     "content": "Blog content...",
     "author": "Author Name"
   }
 ]
 ```

- **GET `/posts/{post_id}`**
- Retrieve a single blog post by its ID.
- Response:
 ```
 {
   "id": "post-id",
   "title": "Blog Title",
   "content": "Blog content...",
   "author": "Author Name"
 }
 ```

- **PUT `/posts/{post_id}`**
- Update a blog post by its ID.
- Request body:
 ```
 {
   "title": "Updated Title",
   "content": "Updated content...",
   "author": "Updated Author"
 }
 ```
- Response:
 ```
 {
   "id": "post-id",
   "title": "Updated Title",
   "content": "Updated content...",
   "author": "Updated Author"
 }
 ```

- **DELETE `/posts/{post_id}`**
- Delete a blog post by its ID.
- Response:
 ```
 {
   "message": "Post deleted successfully"
 }
 ```

## Project Structure

## Technologies Used

- **FastAPI**: High-performance web framework
- **MongoDB**: NoSQL database for storing blog posts
- **Motor**: Async MongoDB driver for Python
- **Pydantic**: Data validation and settings management
