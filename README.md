# 🌐 Web APIs with Python — Study Notes

> **Topic:** Introduction to APIs  
> **Author:** Daniel Nzioki Musyoka  

---

## Table of Contents

- [🌐 Web APIs with Python — Study Notes](#-web-apis-with-python--study-notes)
  - [Table of Contents](#table-of-contents)
  - [1. What is an API?](#1-what-is-an-api)
  - [2. Web APIs, Clients \& Servers](#2-web-apis-clients--servers)
    - [How It Works](#how-it-works)
  - [3. Types of Web APIs](#3-types-of-web-apis)
  - [4. Working with APIs in Python](#4-working-with-apis-in-python)
    - [4.1 `urllib` (Built-in)](#41-urllib-built-in)
    - [4.2 `requests` (Third-party, Recommended)](#42-requests-third-party-recommended)
  - [5. urllib vs requests — Quick Comparison](#5-urllib-vs-requests--quick-comparison)
  - [6. Anatomy of an API Request](#6-anatomy-of-an-api-request)
  - [7. URL Structure](#7-url-structure)
  - [8. Query Parameters](#8-query-parameters)
    - [❌ Appending manually to the URL string (works but not ideal)](#-appending-manually-to-the-url-string-works-but-not-ideal)
    - [✅ Using the `params` argument (recommended)](#-using-the-params-argument-recommended)
  - [9. HTTP Verbs](#9-http-verbs)
  - [10. Sending Data — POST, PUT \& DELETE](#10-sending-data--post-put--delete)
  - [11. Key Takeaways](#11-key-takeaways)
  - [Resources](#resources)

---

## 1. What is an API?

**API** stands for **Application Programming Interface**.

An API defines a **set of rules and abilities** that allow two systems to communicate with each other. Through an API, systems can exchange or manipulate data without the end user needing to know the technical details.

> 💡 **Real-world analogy:** When you click "Send" in your email app, the application uses an API to instruct the email server to deliver your message to the recipient — all behind the scenes.

**Key points:**
- As users, we rarely interact with APIs directly — we use a **User Interface (UI)** instead.
- APIs power almost every piece of modern software.
- They are the "contracts" between software components for how to talk to each other.

---

## 2. Web APIs, Clients & Servers

**Web APIs** enable communication between two software applications **over a network or the internet**.

They use the **HTTP protocol** — the same protocol your browser uses to load web pages.

### How It Works

```
Client  ──── HTTP Request ────►  Server
Client  ◄─── HTTP Response ───  Server
```

- **Client** → sends a request message to the server
- **Server** → processes the request and sends a response back

---

## 3. Types of Web APIs

| Type | Description | Use Case |
|------|-------------|----------|
| **SOAP** | Formal, strict protocol using XML | Enterprise applications requiring robustness |
| **REST** | Simple, scalable, easy to integrate | Most common — used in this course |
| **GraphQL** | Flexible & precise data retrieval, minimises data transfer | Performance-optimised applications |

> ✅ **This course focuses on REST APIs** — the most widely used type in modern software development.

---

## 4. Working with APIs in Python

Python has two main libraries for working with Web APIs:

### 4.1 `urllib` (Built-in)

Comes bundled with Python. Powerful but verbose.

```python
from urllib.request import urlopen

api = "https://jsonplaceholder.typicode.com/posts/1"  # free public REST API, no auth required

with urlopen(api) as response:   # context manager ensures connection is closed after use
    data = response.read()        # Step 1: read raw bytes from response
    string = data.decode()        # Step 2: decode bytes → string (defaults to UTF-8)
    print(string)                 # Step 3: print the response body
```

**Drawback:** Requires multiple steps just to read a response.

---

### 4.2 `requests` (Third-party, Recommended)

Install with: `pip install requests`

```python
import requests

api = "https://jsonplaceholder.typicode.com/posts/1"  # free public REST API, no auth required

response = requests.get(api)   # sends GET request, reads & decodes automatically
print(response.text)           # .text gives you the already-decoded string
```

**Advantage:** Reading and decoding is handled automatically — much cleaner and more readable code.

---

## 5. urllib vs requests — Quick Comparison

| Feature | `urllib` | `requests` |
|---------|----------|------------|
| Bundled with Python | ✅ Yes | ❌ No (pip install) |
| Code simplicity | Verbose | Concise |
| Auto decoding | ❌ Manual | ✅ Automatic |
| Built-in features | Limited | Rich (auth, sessions, JSON, etc.) |
| Recommended for | Simple/internal use | General API work |

---

## 6. Anatomy of an API Request

Every API request is built from three things:

- **A URL** — where to send the request (what resource to target)
- **An HTTP verb** — what action to perform on that resource
- **Data (optional)** — the payload to send along (used in POST and PUT)

> 💡 **Analogy:** Think of a REST API as an office building. Each office unit is a unique resource. The URL is the full address of that unit. The HTTP verb is the instruction you give when you arrive — read the mailbox, drop a package, replace it, or empty it.

---

## 7. URL Structure

A URL is a **structured address** pointing to a specific resource on a server. It has five components:

```
https://api.example.com:443/users/123?sort=asc&limit=10
│       │               │   │         │
│       │               │   │         └── Query    → additional instructions/filters
│       │               │   └──────────── Path     → specific resource location
│       │               └──────────────── Port     → gateway into the server (default: 80/443)
│       └──────────────────────────────── Domain   → address of the API server
└──────────────────────────────────────── Protocol → how to travel (HTTP/HTTPS)
```

| Component | Office Building Analogy | Example |
|-----------|------------------------|---------|
| **Protocol** | Mode of transport (walk/drive) | `https://` |
| **Domain** | Street address of the building | `api.example.com` |
| **Port** | Entrance/gateway | `:443` |
| **Path** | Specific office unit | `/users/123` |
| **Query** | Extra instructions ("take the elevator") | `?sort=asc&limit=10` |

---

## 8. Query Parameters

Query parameters let you pass **additional instructions** to an API — like filters, sorting, or pagination.

### ❌ Appending manually to the URL string (works but not ideal)

```python
import requests

api = "https://jsonplaceholder.typicode.com/posts?userId=1&_limit=3"
response = requests.get(api)
print(response.text)
```

### ✅ Using the `params` argument (recommended)

```python
import requests

api = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1,    # filter posts by user
    "_limit": 3     # return only 3 results
}

response = requests.get(api, params=params)  # requests builds the query string automatically
print(response.text)
```

> The `params` dictionary is cleaner, easier to read, and `requests` handles URL encoding automatically.

---

## 9. HTTP Verbs

Every API request uses an **HTTP verb** to define what action to perform on a resource. There are 9 in total, but these 4 are the most important for REST APIs:

| Verb | Action | Mailbox Analogy |
|------|--------|-----------------|
| **GET** | Read a resource | Check the mailbox contents without removing anything |
| **POST** | Create a new resource | Drop a new package into the mailbox |
| **PUT** | Update/replace an existing resource | Replace the existing package with a new one |
| **DELETE** | Remove a resource | Empty the mailbox completely |

```python
import requests

base = "https://jsonplaceholder.typicode.com/posts"

# GET — read post with id=1
response = requests.get(f"{base}/1")

# POST — create a new post
response = requests.post(base, data={"title": "New Post", "body": "Content", "userId": 1})

# PUT — update post with id=1
response = requests.put(f"{base}/1", data={"title": "Updated Post", "body": "New content", "userId": 1})

# DELETE — remove post with id=1
response = requests.delete(f"{base}/1")
```

---

## 10. Sending Data — POST, PUT & DELETE

For **POST** and **PUT** requests, you need to send data along with the request using the `data` argument:

```python
import requests

api = "https://jsonplaceholder.typicode.com/posts"

# POST — create a new resource
new_post = {
    "title": "Learning APIs",
    "body": "APIs allow systems to communicate over HTTP.",
    "userId": 1
}

response = requests.post(api, data=new_post)
print(response.text)   # returns the newly created resource

# PUT — update an existing resource
updated_post = {
    "title": "Updated: Learning APIs",
    "body": "REST APIs are the most common type.",
    "userId": 1
}

response = requests.put(f"{api}/1", data=updated_post)
print(response.text)   # returns the updated resource

# DELETE — no data needed, just target the resource
response = requests.delete(f"{api}/1")
print(response.status_code)   # 200 means success
```

| Argument | Used With | Purpose |
|----------|-----------|---------|
| `params` | GET | Pass query parameters / filters |
| `data` | POST, PUT | Send payload to create or update a resource |

---

## 11. Key Takeaways

- An **API** is a contract between two systems defining how they can communicate.
- **Web APIs** use HTTP — the same protocol as the browser.
- The three main Web API types are **SOAP**, **REST**, and **GraphQL**; REST is the most common.
- In Python, use the **`requests`** library for clean, readable API calls.
- `urllib` is built-in but requires more boilerplate code for the same result.
- A **URL** has 5 components: protocol, domain, port, path, and query.
- Use the `params` argument in `requests` to pass query parameters cleanly.
- The 4 core **HTTP verbs** are GET (read), POST (create), PUT (update), DELETE (remove).
- Use the `data` argument in `requests.post()` and `requests.put()` to send payloads.

---

## Resources

- [DataCamp — Intermediate Importing Data in Python](https://www.datacamp.com)
- [Python `requests` Documentation](https://docs.python-requests.org/en/latest/)
- [Python `urllib` Documentation](https://docs.python.org/3/library/urllib.html)
- [REST API Overview — MDN](https://developer.mozilla.org/en-US/docs/Glossary/REST)
- [JSONPlaceholder — Free Fake REST API for testing](https://jsonplaceholder.typicode.com)

---

*Notes compiled from DataCamp lecture: "Introduction to APIs" by Chris Ramakers.*