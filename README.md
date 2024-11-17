# SuperSecurityAPI

## Overview
SuperSecurityAPI is a robust, secure, and scalable API designed to manage and validate security keys for software and application usage. This API ensures that only authorized users or developers with valid credentials can access or execute specific functionalities. It provides endpoints for requesting, approving, and validating security keys to prevent unauthorized usage or piracy of your application.

### Hosted URL
- **Base URL**: [https://supersecure.agratasinfotech.com](https://supersecure.agratasinfotech.com)

### Key Endpoints
1. **Request a Security Key**
   - **URL**: `/api/request-key/`
   - **Method**: `POST`
   - **Description**: Allows users to submit a request for a security key by providing their details (Employee ID, Name, Email, Phone, and Description).

2. **Approve a Security Key**
   - **URL**: `/api/approve-key/<employee_id>/`
   - **Method**: `POST` / `GET`
   - **Description**: Enables administrators to approve a security key request and generate a unique security key for the user. Users can also fetch the approved key via a `GET` request.

3. **Validate a Security Key**
   - **URL**: `/api/validate-key/<employee_id>/`
   - **Method**: `GET`
   - **Description**: Validates the security key for a specific Employee ID, ensuring it matches the one issued by the system.

---

## Why SuperSecurityAPI is Important
### The Problem
In today’s digital age, software piracy and unauthorized access are significant challenges. Applications hosted in public repositories (e.g., GitHub) are vulnerable to cloning and misuse, leading to:
- **Revenue Loss**: Unauthorized users can exploit your application for free.
- **Security Risks**: Unapproved access can compromise sensitive data.
- **Brand Dilution**: Pirated versions of your application can tarnish your reputation.

### The Solution
SuperSecurityAPI addresses these issues by:
- **Providing Controlled Access**: Only users with approved security keys can execute or access specific functionalities.
- **Ensuring Compliance**: Tracks who is using the application and for what purpose, ensuring adherence to licensing agreements.
- **Streamlining Key Management**: Automates the process of requesting, approving, and validating security keys, reducing manual overhead.

---

## Features
1. **Secure Key Generation**
   - Unique and unguessable keys generated for each user.
   - Prevents unauthorized sharing of keys.

2. **Key Validation**
   - Real-time validation of security keys against the server.
   - Ensures the key matches the registered Employee ID.

3. **Admin Controls**
   - Admins can approve or reject key requests.
   - Detailed logging and tracking of all key-related activities.

4. **User-Friendly Interface**
   - Clear and simple API endpoints for seamless integration.
   - Responsive error handling and informative messages.

---

## How It Works
### Step 1: Request a Key
Users submit their details using the `/api/request-key/` endpoint. Required fields include:
- Employee ID
- Name
- Email
- Phone Number
- Reason for requesting the key

### Step 2: Admin Approval
Admins review the request via the `/api/approve-key/<employee_id>/` endpoint and approve or reject it. Upon approval, a unique security key is generated and stored in the database.

### Step 3: Validation
Applications validate the key against the API using `/api/validate-key/<employee_id>/` to ensure the key is authorized and matches the user’s credentials.

---

## Example Usage
### Requesting a Key
**Endpoint**: `POST /api/request-key/`

**Payload**:
```json
{
    "employee_id": "EMP001",
    "employee_name": "John Doe",
    "employee_email": "john.doe@example.com",
    "employee_phone": "9876543210",
    "description": "Requesting key for project development."
}
```

**Response**:
```json
{
    "message": "Request submitted successfully.",
    "employee_id": "EMP001"
}
```

### Approving a Key
**Endpoint**: `POST /api/approve-key/EMP001/`

**Response**:
```json
{
    "message": "Key approved successfully.",
    "security_key": "233897-asdjksadajksld-e33294-jknjas"
}
```

### Validating a Key
**Endpoint**: `GET /api/validate-key/EMP001/`

**Response**:
```json
{
    "message": "Key validation successful.",
    "status": "valid"
}
```

---

## Benefits
### For Developers
- Prevents unauthorized usage of your application.
- Automates the key management process, saving time and effort.

### For Organizations
- Secures intellectual property and software licenses.
- Tracks usage to ensure compliance with licensing policies.

---

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/agratas/supersecurityapi.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the server:
   ```bash
   python manage.py runserver
   ```

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure all tests pass before submitting your PR.

---

## License
SuperSecurityAPI is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact
For questions or support, contact:
- **Email**: support@agratasinfotech.com
- **Website**: [https://agratasinfotech.com](https://agratasinfotech.com)

---
