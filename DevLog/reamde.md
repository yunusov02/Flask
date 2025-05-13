# DevLog

**DevLog it is blog application**

## DataBase Structure
    CATEGORY
        id
        name unique
    
    POST
        id
        user_id
        title
        body
        image
        published
        created_at
    USER
        id
        username
        password
        emails
        job_title
            - author
            - admin
    LIKES
        id
        post_id
        user_id
        like 1 or -1 not required
        comment not required

## App Strucutre

run.py
app/
    | post/
    | users/
    | likes/
    | api/
    | templates/
    | static/
tests
    | test_post.py
    | test_users.py
    | test_likes.py
    | test_api.py
    | test_db.py
    

- post detail view
- like / unlike a post
- comments
- tags Clicking a tag shows all the post with that tag
- A search box with title
- Paged display. Only show 5 postss per page
- upload an image to go along with a post
- formating posts using Markdown
- an RSS feed of ned posts
- user authentication & authorization
- post categories
- Bookmarking posts (allow user to bookmark their favorite posts, which they can later access through their profile)
- Social sharing Integration
- Comment Moderation and Spam Protection
- Email notification
- Post scheduling
- Trending posts (daily, weekly, monthly)
- user profiles
- allow users to filter search results by categories date range
- related posts
- Markdown preview (provide a real-time preview of posts being written in Markdown)
- Dark / Light Mode
- Analytics Dashboard (Admin Feature)

Implementation
* Database models SQLAlchemy
* Form handling use Flask-WTF
* Flask-Login
* Flask-Mail
* Flask-Admin

First use what you learned yesterday
and use above Implementation


Models
    Users
    Followers
    Categories
    Posts
    Media_Files
    Comments
    Likes
    Schedule_post
    Post_views
    


Flask API
    - Blogify API
    - e Commerce API
    - RealTimeCHat API
PostgreSQL
    - 1-4
    - 5-8
    - 9-12
    - 12-16
    - 16-20
HTML/CSS/Bootstrap
    - Main Course
    - YouTube
    - Facebook
    - Linkedn
    - Asaxiy
    - Twitter
    
DevOps
    - Nginx
    - Docker
    - CI/CD Gitlab
    - CI/CD Github
Flask
    - Blogify
    - e Commerce
    - RealTimeChat
    - s21_decimal



Django
    - Blog Application
    - RealEstate
    - e Commerce
    - POS
    - Social App
    - Online Job Portal
    - HR MS
    - Acc & Fin MS
    - School Management System
Django API
    - Blog Application API
    - RealEstate API
    - e Commerce API
    - POS API
    - Social App API
    - Online Job Portal API
    - HR MS API
    - Acc & Fin MS API
    - School Management System API
JS/React
    - Main Course
    - JS30
    - React
    -23FullStackBootcamp




FastAPI
    - Manufacturing ERP
    - Yandex Go
    - Yandex Eats
    - Uzum
MongoDB
    - Getting Start
    - CRUD
    - Aggregation
    - Indexes
    - Tools
    - Python
    











