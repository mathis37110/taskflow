
tasks = []
def input_and_strip(question : str) -> str: 
  return input(question).strip()


def add_task() -> None:
  new_task = input_and_strip("quelle tache voulez vous ajoutez :")
  tasks.append(new_task)
  print("votre tache ",new_task,"a bien etait ajouter")
  


def delete_task() -> None:
 task_delete = input_and_strip("quelle tache voulez vous supprimer :")
 try:
  tasks.remove(task_delete)
  print("votre tache a bien etait supprimer")
 except ValueError:
  print("cette tache n'existe pas")


def print_tasks() -> None:
 print("voici vos tache :")
 for task_name in tasks:
   print(task_name)
 

def leave_taskflow() -> None:
 print("au revoir")
 


def print_choice() -> None:
 print("------------------------------------------------")
 print("que voulez-vous faire ?")
 print("1. ajouter une tache")
 print("2. supprimer une tache")
 print("3. voir les taches")
 print("4. quitter")
 answer = input("choix :")
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
 