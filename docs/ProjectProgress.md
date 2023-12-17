# *Django Human Resources API-REST Progress*

## Employees Module

### Endpoints


#### Base URL: *employees/*

#### 1. Retrieve Employee Information

- **Endpoint:** `GET /employees/{employee_id}/`
- **Description:** Retrieve information about a specific employee.
- **Parameters:**
  - `employee_id` (path): Unique identifier for the employee.
- **Response:**
  - Status Code: 200 OK
  - Content: JSON representation of the employee's information.
- **Example:**
  ```http
  GET /employees/123456789/
  ```

#### 2. List All Employees

- **Endpoint:** `GET /employees/`
- **Description:** Retrieve a list of all employees.
- **Parameters:**
  - None
- **Response:**
  - Status Code: 200 OK
  - Content: JSON array containing information about all employees.
- **Example:**
  ```http
  GET /employees/
  ```

#### 3. Create a New Employee

- **Endpoint:** `POST /employees/`
- **Description:** Create a new employee with the provided information.
- **Parameters:**
  - Request Body: JSON representation of the new employee's information.
    ```json
    {
      "id": "987654321",
      "first_name": "John",
      "last_name": "Doe",
      "birth_date": "1990-05-15",
      "gender": 1,  # Assuming 1 represents the ID of the desired gender
      "role": 1,    # Assuming 1 represents the ID of the desired role
      "address": "123 Main St",
      "email": "john.doe@example.com"
    }
    ```
- **Response:**
  - Status Code: 201 Created
  - Content: JSON representation of the newly created employee.
- **Example:**
  ```http
  POST /employees/
  ```

#### 4. Update Employee Information

- **Endpoint:** `PUT /employees/{employee_id}/`
- **Description:** Update information for a specific employee.
- **Parameters:**
  - `employee_id` (path): Unique identifier for the employee.
  - Request Body: JSON representation of the updated employee's information.
- **Response:**
  - Status Code: 200 OK
  - Content: JSON representation of the updated employee.
- **Example:**
  ```http
  PUT /employees/987654321/
  ```

#### 5. Delete Employee

- **Endpoint:** `DELETE /employees/{employee_id}/`
- **Description:** Delete a specific employee from the system.
- **Parameters:**
  - `employee_id` (path): Unique identifier for the employee.
- **Response:**
  - Status Code: 204 No Content
- **Example:**
  ```http
  DELETE /employees/987654321/
  ```

### Data Models

#### Employee Model

```json
{
  "id": "string",
  "first_name": "string",
  "last_name": "string",
  "birth_date": "YYYY-MM-DD",
  "gender": "string",  # Name of the gender
  "role": "string",    # Name of the role
  "address": "string",
  "email": "string"
}
```

#### Gender Model

```json
{
  "id": 1,
  "name": "Male"
}
```

#### Role Model

```json
{
  "id": 1,
  "name": "Employee"
}
```

