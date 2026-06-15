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
  - [6. Key Takeaways](#6-key-takeaways)
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

## 6. Key Takeaways

- An **API** is a contract between two systems defining how they can communicate.
- **Web APIs** use HTTP — the same protocol as the browser.
- The three main Web API types are **SOAP**, **REST**, and **GraphQL**; REST is the most common.
- In Python, use the **`requests`** library for clean, readable API calls.
- `urllib` is built-in but requires more boilerplate code for the same result.

---

## Resources

- [DataCamp — Intermediate Importing Data in Python](https://www.datacamp.com)
- [Python `requests` Documentation](https://docs.python-requests.org/en/latest/)
- [Python `urllib` Documentation](https://docs.python.org/3/library/urllib.html)
- [REST API Overview — MDN](https://developer.mozilla.org/en-US/docs/Glossary/REST)

---

*Notes compiled from DataCamp lecture: "Introduction to APIs" by Chris Ramakers.*