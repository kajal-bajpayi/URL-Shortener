# 🚀 URL Shortener

A fully serverless URL shortener built using AWS services.

Users can:
- 🔗 Create short links
- ↪ Redirect using short URLs
- 📊 Track click counts
- 📈 View analytics dashboard

Deployed using a fully managed, scalable AWS architecture.

---

# 🏗 Architecture

## AWS Services Used

- Amazon API Gateway (REST API)
- AWS Lambda
- Amazon DynamoDB
- Amazon S3 (Static Website Hosting)
- Amazon CloudFront (CDN + HTTPS)

---

# 🧠 How It Works

1. User enters a long URL in frontend.
2. Frontend calls API Gateway.
3. Lambda generates short ID.
4. URL mapping is stored in DynamoDB.
5. Short URL is returned.
6. When short URL is accessed:
   - Lambda fetches original URL
   - Increments click counter
   - Redirects user
7. Analytics endpoint returns all records.

---

# 🏛 Architecture Diagram (Logical Flow)

```
User
  ↓
CloudFront (HTTPS CDN)
  ↓
S3 (Static Frontend)
  ↓
API Gateway
  ↓
Lambda Functions
  ↓
DynamoDB
```

---

# 🔧 Backend Implementation

## 1️⃣ DynamoDB Table

Table Name: `url-shortener`

Primary Key:
```
shortId (String)
```

Attributes:
- originalUrl (String)
- clicks (Number)

---

## 2️⃣ Lambda Functions

### A. Shorten Function

**Route:**  
`POST /shorten`

**Purpose:**
- Generate unique shortId
- Store mapping in DynamoDB
- Return shortId

---

### B. Redirect Function

**Route:**  
`GET /{shortId}`

**Purpose:**
- Fetch original URL
- Increment clicks
- Redirect (302)

---

### C. Analytics Function

**Route:**  
`GET /analytics`

**Purpose:**
- Scan DynamoDB
- Return all records with click counts

---

# 🌐 Frontend

Hosted on:
- Amazon S3 (static website)
- Delivered via CloudFront

Features:
- URL input field
- Short URL generator
- Clickable short link
- Analytics table with refresh button

---

# 🔥 API Endpoints

Base URL:

```
https://<api-id>.execute-api.<region>.amazonaws.com/prod
```

| Method | Endpoint | Description |
|--------|----------|------------|
| POST | /shorten | Create short URL |
| GET | /{shortId} | Redirect |
| GET | /analytics | Get click stats |

---

# ⭐ If you found this helpful

Give this repo a star ⭐
