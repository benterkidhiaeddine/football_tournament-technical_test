# Project Installation and Usage Guide

## Prerequisites

- Docker & Docker Compose installed
- (Optional) GNU Make installed for easier commands

## 1. Clone the Repository

```
git clone <repo-url>
cd football_tournament-technical_test
```

## 2. Environment Variables

Copy the example environment file and edit as needed:

```
cp .env.dev.example .env.dev
```

## 3. Build and Start the Services

```
make up
```

This will build and start the web, db containers.

## 4. Apply Database Migrations

```
make migrate
```

## 5. (Optional) Seed the Database

To populate the database with randome team and players

```
make seed
```

## 6. Run the Development Server

The server will be available at http://localhost:8000

## 7. Run Tests

```
make test
```

## 8. Stop the Services

```
make down
```

---

# Makefile Commands

See the `Makefile` in the project root for all available shortcuts.
