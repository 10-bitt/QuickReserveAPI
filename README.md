# QuickReserveAPI

QuickReserveAPI is a web-based facility reservation system built using Django and Django REST Framework.

## Features
- User management
- Facility management
- Reservation system
- REST API with full CRUD operations
- Admin dashboard
- Simple frontend integration

## Technologies Used
- Python
- Django
- Django REST Framework
- SQLite
- HTML & JavaScript

## API Endpoints

### Users
- GET /api/users/
- POST /api/users/
- GET /api/users/{id}/
- PUT /api/users/{id}/
- DELETE /api/users/{id}/

### Facilities
- GET /api/facilities/
- POST /api/facilities/
- GET /api/facilities/{id}/
- PUT /api/facilities/{id}/
- DELETE /api/facilities/{id}/

### Reservations
- GET /api/reservations/
- POST /api/reservations/
- GET /api/reservations/{id}/
- PUT /api/reservations/{id}/
- DELETE /api/reservations/{id}/

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run migrations:
   py manage.py migrate

3. Start server:
   py manage.py runserver
