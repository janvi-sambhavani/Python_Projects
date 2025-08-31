📖 API Endpoints
Root

GET / → Welcome message.

Dashboard

GET /dashboard?username=janvi → Returns task summary for the given user.

Tasks

GET /tasks → Get all tasks.

GET /tasks/{task_id} → Get task by ID.

POST /tasks → Create new task.

PUT /tasks/{task_id} → Update existing task.

DELETE /tasks/{task_id} → Soft delete task.

🗄️ Data Models
Task
{
  "id": 1,
  "title": "Task 1",
  "owner": "janvi",
  "status": "new",
  "is_deleted": false
}

TaskCreate
{
  "title": "New Task",
  "owner": "janvi",
  "status": "new"
}

📊 Example

Request:

POST /tasks

{
  "title": "Prepare README",
  "owner": "janvi",
  "status": "active"
}


Response:

{
  "id": 5,
  "title": "Prepare README",
  "owner": "janvi",
  "status": "active",
  "is_deleted": false
}
