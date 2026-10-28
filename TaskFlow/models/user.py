import json
from models.task import tasks
user_list = []

class User:
     def __init__(self, name : str, age : int):
          self.name = name
          self.age = age
          self.task_assigned = []
          self.id = id(self)
    
    
     def add(name : str , age : int) -> None:
          user_list.append(User(name, age))


     def delete(index : int) -> None:
          user_list.pop(index)


     def edit(index : int, name : str, age : int) -> None:
          user_list[index] = name
          user_list[index ]= age
         
    
     def assigned_to(index_task : int, index_user : int) -> None:
          tasks[index_task].user = user_list[index_user]


     def all_json() -> json:
          return json.dumps((user.turn_json for user in user_list ))    
    
     
     def turn_json(self) -> dict:
          return {'name': self.name, 'age' : self.age}


