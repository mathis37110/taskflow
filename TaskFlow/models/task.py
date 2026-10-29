import json

tasks = []

class Task():
	def __init__(self, name : str, description : str):
		self.name = name
		self.description = description
		self.user = None

		

	def add(name : str, description : str) -> None:
		new_task = Task(name, description)
		tasks.append(new_task)
		return new_task
		 


	def delete(task_delete : int) -> None:
		tasks.pop(task_delete)


	def edit(index : str, name : str, description : str) -> None:
		
		tasks[index].name = name
		tasks[index].description = description
		return name, description


	def turn_json(self) -> dict:
		return {"name": self.name, "description": self.description, "user": self.user}


	def all_json() -> json:
		return json.dumps((task.turn_json() for task in tasks))		

