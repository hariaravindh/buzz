# A Python and MySQL based Bus Ticket Booking System

## Overview

BUZZ is a command line Bus Ticket Booking System that allows users to browse available buses, view routes and manage ticket reservations using a MySQL database backend.

Developed as an educational project, BUZZ demonstrates the fundamentals of:

- Python application development
- MySQL database integration
- SQL query execution
- CRUD operations
- Reservation management workflows
- Data persistence

---

## Features

- Bus Management
- Booking Workflow
- Route Management
- Database Integration

---

## Technology Stack

### Backend

- Python 3

### Database

- MySQL

### Database Operations

- SQL

### Execution Mode

- Command Line Interface (CLI)


---

## System Architecture

```text
+------------------+
|  User Interface  |
|      (CLI)       |
+--------+---------+
         |
         v
+------------------+
| Business Logic   |
|  Python Modules  |
+--------+---------+
         |
         v
+------------------+
|   MySQL Layer    |
|  SQL Queries     |
+--------+---------+
         |
         v
+------------------+
|    Database      |
| Booking Records  |
+------------------+
```

## Learning Outcomes

This project was built to explore and understand:

- Relational database design
- SQL schema creation
- Python-MySQL connectivity
- Data storage and retrieval
- Reservation system workflows
- Modular application development

---

## Future Roadmap

Planned improvements include:

- Functional Enhancements
- Improved Modularization
- Web based Front End

---

## Repository Structure

```text
buzz/
│
├── src/
│   └── buzz/
│       ├── main.py
│       ├── booking.py
│       ├── buses.py
│       ├── locations.py
│       └── database.py
│
├── sql/
│   └── schema.sql
│
├── tests/
│   ├── test_booking.py
│   └── test_database.py
│
├── docs/
│   ├── architecture.md
│   └── screenshots/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Project Background

BUZZ originated as a learning project aimed at understanding how booking systems interact with databases and how transactional workflows can be implemented using Python and MySQL.

The project focuses on core software engineering concepts such as database integration, structured data management, and user interaction through a command-line interface.

## Tools Used

<p align="left">

<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=fff" />

</p>

---

![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)

---

⭐ If you found this project interesting, consider giving it a star.
