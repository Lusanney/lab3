# My Booking Page and its related components

### Backend API interfaces implemented:

- Get all my bookings -> `GET /api/visitors/:id/bookings`
- Get booking report -> `GET /api/bookings/:id/report`

### Pages & Component include

- Booking
- Booking Report Dialog

### Description

**1. On Page Load, Get All Bookings**

_Client URL:_ `/bookings`  
_Authenticated: YES, you must logged in to use this page_

On Page loaded, the page will make a request to server to get all bookings that you have made. After that, it will represent as a list, which each item will have a booking code of your booking. It also has an adjacent button to show booking report.

**2. Booking Report**

_Client Component:_ **Booking Report Dialog**  
_Authenticated: YES, you must logged in to use this page_

Once you click the booking details button, there will be a pop up dialog showing the booking details such as:

- Check-in date
- Check-out date
- Bills you have
- Total money you need to pay
- Total days stayed

