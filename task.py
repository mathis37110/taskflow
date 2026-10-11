
tasks = []


def input_and_strip(question : str) -> str: 
  return input(question).strip()


def add_task() -> None:
  new_task = {}
  new_task['name'] = input_and_strip("quelle tache voulez vous ajoutez :")
  new_task['description'] = input_and_strip("quelle est la description de votre tache :")
  tasks.append(new_task)
  print("votre tache",new_task['name'],"a bien etait ajouter")
  

def delete_task() -> None:
 task_delete = int(input_and_strip("quelle est l'index de la tâche que vous voulez supprimer :"))
 
 tasks.pop(task_delete)
 
  
 

def print_tasks() -> None:
 print("voici vos tache :")
 i = 0
 for task_name in tasks:
   print("nom de la tache :",task_name['name'])
   print("description de la tache :",task_name['description'])
   print("index de la tache :",i)
   print()
   
   i = i + 1
 

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
    add_task()
   case "2":
    delete_task()
   case "3":
    print_tasks()
   case "4":
    leave_taskflow()
   case _:
    print("answer invalide ")
 

main_loop()
 