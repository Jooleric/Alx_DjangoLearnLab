# 🧑‍🤝‍🧑 Social Media API

This is a Django REST Framework-based **Social Media API** project that provides user authentication and basic profile management functionality.  
It is part of the `Alx_DjangoLearnLab` repository.

---

# Social Media API - Posts and Comments

## 🚀 Features

✅ **Custom User Model** — Extended from Django’s `AbstractUser`  
✅ **Token Authentication** — Secure access using DRF’s `TokenAuthentication`  
✅ **User Registration & Login** — JSON-based API endpoints  
✅ **Profile Management** — View and update user profiles  
✅ **Media Uploads** — Profile pictures stored in `/media/`  
✅ **RESTful API Design** — Built using Django REST Framework
✅ CRUD operations for posts and comments
✅ Permissions for post/comment owners

---
## Endpoints

### Posts
- `GET /api/posts/` – List all posts
- `POST /api/posts/` – Create new post
- `GET /api/posts/{id}/` – View post detail
- `PUT/PATCH /api/posts/{id}/` – Update your post
- `DELETE /api/posts/{id}/` – Delete your post

### Comments
- `GET /api/comments/` – List all comments
- `POST /api/comments/` – Create comment
- `DELETE /api/comments/{id}/` – Delete your comment

## 🏗️ Project Structure


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<Jooleric>/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
