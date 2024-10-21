# Task Management App

## Overview
This is a task management application built using Django and Django Rest Framework. It allows users to create tasks, assign tasks to users, and retrieve tasks assigned to specific users.

## Features
- Create new tasks with a name and description.
- Assign tasks to one or multiple users.
- Retrieve all tasks assigned to a specific user.

## Technologies Used
- Python 3.x
- Django
- Django Rest Framework
- Poetry (for dependency management)

## Setup Instructions

### Prerequisites
- Python 3.x
- Poetry (for managing dependencies)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/pandemic07/UserTask_Assignment_JoshTalks.git
   cd task_management_app

2. **Create a Virtual Environment using Poetry**
    ```bash
    poetry install

3. **Activate the Virtual Environment**
    ```bash
    poetry shell

4. **Apply Migrations**
    ```bash
    poetry shell
5. **Create a Superuser (Admin)**
    ```bash
    python manage.py createsuperuser


6. **Run the Development Server**
    ```bash
    python manage.py runserver


7. **Access the Admin Panel**
    ```bash
    http://127.0.0.1:8000/admin/
    

## API Endpoints

### 1. Create a Task
- **Endpoint**: `POST /api/tasks/`
- **Description**: Creates a new task with a name and description.
- **Request Body**:
  - `name`: **String** - The name of the task.
  - `description`: **String** - A brief description of the task.
  - `task_type`: **String** - The type of the task.
  
- **Response**:
  - **Status Code**: 201 Created
  - **Body**:
    - `id`: **Integer** - The unique identifier for the task.
    - `name`: **String** - The name of the task.
    - `description`: **String** - The description of the task.
    - `created_at`: **DateTime** - The timestamp when the task was created.
    - `task_type`: **String** - The type of the task.
    - `completed_at`: **DateTime** or **null** - The timestamp when the task was completed (if applicable).
    - `status`: **String** - The current status of the task (e.g., pending, in_progress, completed).
    - `assigned_users`: **Array** - List of users assigned to this task.

---

### 2. Assign a Task to Users
- **Endpoint**: `POST /api/tasks/{task_id}/assign/`
- **Description**: Assigns a task to one or multiple users.
- **Request Body**:
  - `user_ids`: **Array of Integers** - List of user IDs to assign the task to.

- **Response**:
  - **Status Code**: 200 OK
  - **Body**:
    - `status`: **String** - Message indicating that the task has been assigned (e.g., "task assigned").

---

### 3. Get Tasks Assigned to a Specific User
- **Endpoint**: `GET /api/users/{user_id}/tasks/`
- **Description**: Fetches all tasks assigned to a particular user.
  
- **Response**:
  - **Status Code**: 200 OK
  - **Body**: An array of task objects:
    - **Task Object**:
      - `id`: **Integer** - The unique identifier for the task.
      - `name`: **String** - The name of the task.
      - `description`: **String** - The description of the task.
      - `created_at`: **DateTime** - The timestamp when the task was created.
      - `task_type`: **String** - The type of the task.
      - `completed_at`: **DateTime** or **null** - The timestamp when the task was completed (if applicable).
      - `status`: **String** - The current status of the task.
      - `assigned_users`: **Array of User Objects** - List of users assigned to this task, each containing:
        - `id`: **Integer** - The unique identifier for the user.
        - `username`: **String** - The username of the user.
        - `email`: **String** - The email of the user.
        - `mobile`: **String** - The mobile number of the user.

---

## Conclusion
This task management app provides a simple yet effective way to manage tasks and their assignments. You can extend its functionality by adding features like due dates, priority levels, and notifications.

Feel free to explore the code and customize it further!
