from resources.todo.todos import Todo, TodoList

resources = [
    (TodoList, '/todos'),
    (Todo, '/todos/<todo_id>')
]
