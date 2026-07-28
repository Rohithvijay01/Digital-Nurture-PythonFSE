# Module 3: Database Integration & Management

> Comprehensive practical guide and technical implementations covering Relational Database Design (MySQL), Advanced SQL Querying, Performance Optimization, NoSQL Integration (MongoDB), Python ORM (SQLAlchemy), and Schema Migrations (Alembic).

---

## 📌 Overview

**Module 3: Database Integration** provides a complete end-to-end hands-on exploration of relational and non-relational database management, data modeling, query optimization, Object-Relational Mapping (ORM), and database migration workflows in modern software engineering.

All exercises are organized under `Rohith.V/` and structured into distinct Hands-On modules detailing database concepts from foundational DDL schemas to enterprise migration pipelines.

---

## 📁 Module Directory Structure

```
Module3_DatabaseIntegration/
└── Rohith.V/
    ├── HANDS-ON 1/        # Database Creation & Schema Design (MySQL DDL)
    ├── HANDS-ON  2/       # Data Manipulation (DML), Joins & Aggregations
    ├── HANDS-ON 3/        # Subqueries, Views & Indexing
    ├── HANDS-ON 4/        # Query Execution Optimization & Transactions
    ├── HANDS-ON 5/        # NoSQL Document Database Integration (MongoDB)
    ├── HANDS-ON 6/        # Python ORM Development (SQLAlchemy)
    └── HANDS-ON 7/        # Database Migrations & Version Control (Alembic)
```

---

## 🚀 Learning Modules & Hands-On Breakdowns

### 🛠️ Hands-On 1: Relational Schema Design & DDL
- **Focus**: Setting up MySQL databases (`college_db`) and designing relational schemas.
- **Key Concepts**:
  - `CREATE DATABASE` and `USE` statements.
  - Table creation with explicit constraints: Primary Keys, Foreign Keys, Auto-increment IDs, `NOT NULL`, and `DECIMAL` precision.
  - Entities created: `departments`, `students`, `courses`, and `enrollments`.

---

### 📊 Hands-On 2: Data Manipulation (DML) & Basic Querying
- **Focus**: Inserting, updating, deleting, and querying relational data.
- **Key Concepts**:
  - `INSERT INTO` batch operations for seeding sample records.
  - Filtering records with `WHERE`, `LIKE`, and `ORDER BY`.
  - Table relationships using `INNER JOIN` and `LEFT JOIN`.
  - Data aggregation using `COUNT()`, `SUM()`, `AVG()`, and `GROUP BY`.

---

### 🔍 Hands-On 3: Advanced SQL Queries & Database Views
- **Focus**: Writing complex analytical SQL queries, views, and index structures.
- **Key Concepts**:
  - Subqueries and nested filtering logic.
  - Post-aggregation filtering with the `HAVING` clause.
  - Creating abstraction layers using Database Views (`CREATE VIEW`).
  - Index creation (`CREATE INDEX`) to improve search performance.

---

### ⚡ Hands-On 4: Query Optimization & Transaction Management
- **Focus**: Analyzing query execution paths and managing transaction boundaries.
- **Key Concepts**:
  - Inspecting query execution plans using `EXPLAIN FORMAT=JSON`.
  - Identifying table scans vs. index lookup operations.
  - Index optimization to reduce examined rows across joined tables.
  - ACID transaction management using `COMMIT` and `ROLLBACK`.

---

### 🍃 Hands-On 5: NoSQL Database Integration (MongoDB)
- **Focus**: Managing unstructured/semi-structured data with MongoDB collections (`college_nosql`).
- **Key Concepts**:
  - Document initialization (`createCollection("feedback")`).
  - Inserting nested JSON documents with arrays and attachments (`insertMany`).
  - Complex document querying with `$elemMatch`, array matching, and ISODate operations.
  - Aggregation framework pipelines (`$match`, `$group`, `$avg`, `$unwind`).

---

### 🐍 Hands-On 6: Python ORM Integration (SQLAlchemy)
- **Focus**: Interacting with relational databases programmatically using Python ORMs.
- **Key Concepts**:
  - Declarative Base models (`models.py`) mapping Python classes to database tables.
  - Defining relationship mappings (`ForeignKey`, `relationship`).
  - Session lifecycle management (`sessionmaker`) for executing type-safe CRUD operations (`crud.py`).

---

### 🔄 Hands-On 7: Database Migrations & Version Control (Alembic)
- **Focus**: Versioning database schemas and applying incremental database migrations.
- **Key Concepts**:
  - Configuring Alembic with SQLAlchemy engines (`alembic.ini`, `env.py`).
  - Baseline migration generation (`revision --autogenerate`).
  - Applying incremental schema updates (`upgrade head`) and rolling back changes (`downgrade`).
  - Schema evolutions (e.g., adding `is_active` status flag, creating `CourseSchedule` table).

---

## 🛠️ Tech Stack & Requirements

| Layer | Technology |
| :--- | :--- |
| **Relational Database** | MySQL 8.0+ |
| **NoSQL Database** | MongoDB 6.0+ |
| **Programming Language** | Python 3.10+ |
| **ORM Library** | SQLAlchemy 2.0+ |
| **Migration Tool** | Alembic |
| **Driver / Connector** | PyMySQL |

---

## ⚙️ How to Run & Verify

1. **MySQL Scripts (Hands-On 1 to 4)**:
   ```bash
   mysql -u root -p < "Rohith.V/HANDS-ON 1/task1"
   ```

2. **MongoDB Scripts (Hands-On 5)**:
   ```bash
   mongosh college_nosql "Rohith.V/HANDS-ON 5/task1"
   ```

3. **SQLAlchemy ORM (Hands-On 6)**:
   ```bash
   python "Rohith.V/HANDS-ON 6/crud.py"
   ```

4. **Alembic Migrations (Hands-On 7)**:
   ```bash
   cd "Rohith.V/HANDS-ON 7"
   python -m alembic upgrade head
   ```
