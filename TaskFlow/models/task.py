import json

tasks = []

class Task():
	def __init__(self, name : str, description : str):
		self.name = name
		self.description = description
		self.user = None

		
	@staticmethod
	def add(name : str, description : str) -> None:
		new_task = Task(name, description)
		tasks.append(new_task)
		return new_task
		 


	def delete(self) -> None:
		tasks.remove(self)


	def edit(self, name : str, description : str) -> None:
		self.name = name
		self.description = description
	


	def turn_json(self) -> dict:
		return vars(self)


	def all_json() -> json:
		return json.dumps((task.turn_json() for task in tasks))		

