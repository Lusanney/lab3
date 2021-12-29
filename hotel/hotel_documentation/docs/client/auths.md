# Auth-related Pages
### Backend API interfaces implemented:

- Sign In -> `POST /auth/token/login`
- Sign Out -> `POST /auth/token/logout`
- Registration -> `POST /api/visitors/create`
- Change Password `POST /auth/users/set_password/`
- Get Me -> `GET /auth/users/me`

### Pages include
- Sign In page
- Registration page (sign up)
- Change password

### Description

**1. On App Load & Sign In**

*Client URL:* `/signin`

The app will first load from Local Storage to see if you have `authToken` in order to know whether you are authenticated or not. If not, it will redirect you to **Sign In** page, where you will make a request to server to authenticate.

- If successful:
    - save `authToken` to Local Storage
    - set `authToken` state globally via VueX store
    - redirect you to **Home** page
- If not successful:
    - Show a toast via `vue-toast`

It is very important to obtain this `authToken` as every request made to server will need to be authenticated

**2. Sign Up**

*Client URL:* `/signup`

You can sign up a new account as a **Visitor**. Right now, we are not using **Host** as this can be considerred to be an admin of the app, which is not very crucial to represent the functionality of server.

**3. Change Password**

*Client URL:* `/me/changepassword`

*Authenticated: YES, you must logged in to use this page*

You can change your password with your old password, new password, and re-confirm password.

**4. Sign Out**

*Client URL: N/A -> Appeared as a button on NavBar*

*Authenticated: YES, you must logged in to use this function*

You can log out from your account by pressing the sign out button on NavBar.

- If successful:
    - clear `authToken` from Local Storage
    - set `authToken = null` state globally via VueX store
    - redirect you to **Sign In** page
- If not successful:
    - Show a toast via `vue-toast`
