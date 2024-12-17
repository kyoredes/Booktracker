# BookTracker

BookTracker is a RESTful API project built with Django REST Framework (DRF). It allows users to organize their book collections into categorized reading lists. The application is designed to track books you plan to read, are currently reading, or have already finished.

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![image](https://img.shields.io/badge/Elastic_Search-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)
![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)


## Features

- **User Authentication**: User registration and login.
- **Book Management**:
  - Add books with details like title, author(s), and description.
  - Manage your book lists.
  - search for books using Elasticsearch
- **Categorized Lists**:
  - Create your book lists
- **API Endpoints**:
  - Create, update, and delete books.
  - Add books to categorized lists.
  - View and manage your reading lists.
## Installation

### Prerequisites
- Python 3
- pip
- PostgreSQL
- Poetry

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/kyoredes/Booktracker/
   cd booktracker
   ```

2. Create a virtual environment and activate it:
   ```bash
   poetry init
   poetry check
   ```

3. Install dependencies:
   ```bash
   poetry install
   ```

4. Configure the database in the `.env` file:
   ```env
   DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DBNAME
   ```

5. Apply migrations:
   ```bash
    make migrate
   ```

6. Run the development server:
   ```bash
   make dev
   ```

The API will be available at `http://127.0.0.1:8000/`.

## Testing

Run tests to ensure the project is functioning correctly:
```bash
make test
```

Show all urls:
```bash
make urls
```
