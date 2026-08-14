# Lab 8: ClinicGuard Healthcare & Appointment API

## Overview
ClinicGuard is a FastAPI-based backend service designed for managing clinic operations, patient records, and appointment scheduling with security and role-based authorization.

## Features
* **Authentication & RBAC**: JWT-based authentication supporting `Patient`, `Doctor`, and `Admin` roles.
* **Appointment Management**: Endpoints for booking, updating, and cancelling medical appointments.
* **Data Validation**: Strict input validation and custom exception handling powered by Pydantic.
* **Database Management**: Relational data modeling using SQLModel and PostgreSQL/SQLite.

## Project Structure
```text
clinicguard-api/
├── database/
│   └── session.py
├── models/
│   ├── appointment.py
│   └── user.py
├── auth.py
├── main.py
├── requirements.txt
└── .env
