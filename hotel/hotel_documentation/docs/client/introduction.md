
# Client Implementation Introduction
### Backend API interfaces implemented:
- Auth:
	- Sign In -> `POST /auth/token/login`
	- Sign Out -> `POST /auth/token/logout`
	- Registration -> `POST /api/visitors/create`
	- Change Password `POST /auth/users/set_password/`
	- Get Me -> `GET /auth/users/me`
- Hotel
	- Get all hotels -> `GET /api/hotels/`
	- Get specific hotel info -> `GET /api/hotels/:id/info`
- Rooms
	- Get all rooms -> `GET /api/rooms/`
	- Book a room -> `POST /api/bookings/create`
- Bookings
	- Get all my bookings -> `GET /api/visitors/:id/bookings`
	- Get booking report -> `GET /api/bookings/:id/report`
---
### Page Documentation

Please see:

- [Auth Pages](auths.md)
- [Rooms Page](rooms.md)
- [Hotel Page](hotels.md)
- [My Bookings Page](bookings.md)

---
### Vue stack:
- API: `vue-axios`
- Theme: `vuetify`
- Route : `vue-router`
- Navigation guard
- Local Storage:
	- Save `authToken`
	- Save current user id `meId`
- Store: `vuex`
	- Save `authToken`