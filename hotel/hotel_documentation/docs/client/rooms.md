# Room Page and its related components

### Backend API interfaces implemented:

- Get all rooms -> `GET /api/rooms/`
- Book a room -> `POST /api/bookings/create`

### Pages & Component include

- Room
- Booking Form Dialog

### Description

**1. On Page Load, Get All Rooms**

_Client URL:_ `/rooms`  
_Authenticated: YES, you must logged in to use this page_

On Page loaded, the page will make a request to server to get all rooms that are in the system. After that, it will represent as a list, which each item will have Room number of hotel name. It also has a button to make a booking with that room.

**2. Make a booking**

_Client Component:_ **Booking Form Dialog**  
_Authenticated: YES, you must logged in to use this page_

Once you click the booking button, there will be a pop up dialog showing the form of booking details such as:

- Date check in
- Date check out

It will automatically assign you as a **main_guest** of the booking with the clicked **room**
