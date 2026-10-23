
tasks = []

class task():
 
 
 def __init__(self, name, description):
  self.name = name
  self.description = description


 def add_task() -> None:
  name = input_and_strip("quelle tache voulez vous ajoutez :")
  description = input_and_strip("quelle est la description de votre tache :")
  new_task = task(name, description)
  tasks.append(new_task)
  print("votre tache",new_task.name,"a bien etait ajouter") 


 def delete_task() -> None:
  try:
   task_delete = int(input_and_strip("quelle est l'index de la tâche que vous voulez supprimer :"))
   tasks.pop(task_delete)
  except ValueError:
   print("ERREUR : vous devez mettre un index")
  except IndexError:
   print("ERREUR : cette index n'existe pas")


 def print_tasks() -> None:
  print("voici vos tache :")
  i = 0
  for task_print in tasks:
   print("nom de la tache :",task_print.name)
   print("description de la tache :",task_print.description)
   print("index de la tache :",i)
   print()
   
   i = i + 1



def input_and_strip(question : str) -> str: 
  return input(question).strip()


def leave_taskflow() -> None:
 print("au revoir")
 

def print_choice() -> None:
 print("------------------------------------------------")
 print("que voulez-vous faire ?")
 print("1. ajouter une tache")
 print("2. supprimer une tache")
 print("3. voir les taches")
 print("4. quitter")
 answer = input_and_strip("choix :")
 print("----------------------------------------------------")
 return answer


def main_loop() -> None:
 answer = None
 while answer != "4":
  answer = print_choice()
  match answer:
   case "1":
    task.add_task()
   case "2":
    task.delete_task()
   case "3":
    task.print_tasks()
   case "4":
    leave_taskflow()
   case _:
    print("ERREUR : reponse invalide ")

 
main_loop()
 