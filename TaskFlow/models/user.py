import json
from models.task import tasks
user_list = []

class User:
     def __init__(self, name : str, age : int):
          self.name = name
          self.age = age
          self.task_assigned = []
          self.id = id(self)
    
     @staticmethod
     def add(name : str, age : int) -> None:
          new_user = User(name, age)
          user_list.append(new_user)
          return new_user



     def delete(self) -> None:
          user_list.remove(self)



     def edit(self, name : str, age : int) -> None:
          self.name = name
          self.age = age
          return self
    
     def assigned_to(self, index_task : int) -> None:
          tasks[index_task].user = self.name
          self.task_assigned.append(tasks[index_task]) 

    
     
     def turn_json(self) -> dict:
          return vars(self)


     @staticmethod
     def all_json() -> json:
          return json.dumps((user.turn_json for user in user_list ))    