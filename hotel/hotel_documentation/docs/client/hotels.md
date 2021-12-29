# Hotel Page and its related components
### Backend API interfaces implemented:

- Get all hotels -> `GET /api/hotels/`
- Get specific hotel info -> `GET /api/hotels/:id/info`


### Pages & Component include
- Hotel
- Hotel Details Information

### Description

**1. On Page Load, Get All Hotels**

*Client URL:* `/hotels`  
*Authenticated: YES, you must logged in to use this page*

On Page loaded, the page will make a request to server to get all hotels that are in the system. After that, it will represent as a list, which each item will have hotel name and details button next to it.

**2. Get Specific Hotels Information**

*Client Component:* **Hotel Details Dialog**  
*Authenticated: YES, you must logged in to use this page*

Once you click the details button, there will be a pop up dialog showing the details of hotel such as:

- Hotel name
- Address
- Description
- Owner contact
- Hotel report: total room, min price, max price
