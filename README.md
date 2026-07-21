# BUZZ 🚌

> A Python and MySQL based Bus Ticket Booking System built to demonstrate database driven application design, ticket reservation workflows and command-line application development.

https://img.shields.io/badge/Python-3.x-blue
![MySQL](httpsields.io/badge/MySQL-Database-orange
![License](https://img.shields.io/badge/License-MIT-
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

---

## License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

⭐ If you found this project interesting, consider giving it a star.
