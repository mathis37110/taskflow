answer = None
task = []
def input_and_strip(question):
  return input(question).strip()
def add_task_fuction():
  add_task = input_and_strip("quelle tache voulez vous ajoutez :")
  task.append(add_task)
  print("votre tache ",add_task,"a bien etait ajouter")
  return
def delete_task_function():
 task_delete = input_and_strip("quelle tache voulez vous supprimer :")
 try:
  task.remove(task_delete)
  print("votre tache a bien etait supprimer")
 except ValueError:
  print("cette tache n'existe pas")
 
 return
def print_task_function():
 print("voici vos tache :")
 for task_name in task:
   print(task_name)
 
 return
def leave_TaskFlow_function():
 print("au revoir")
 return
def print_choice():
 print("------------------------------------------------")
 print("que voulez-vous faire ?")
 print("1. ajouter une tache")
 print("2. supprimer une tache")
 print("3. voir les taches")
 print("4. quitter")
 answer = input("choix :")
 print("----------------------------------------------------")
 return answer
def main_loop(answer):
 while answer != "4":
  answer = print_choice()
  match answer:
   case "1":
    add_task_fuction()
   case "2":
    delete_task_function()
   case "3":
    print_task_function()
   case "4":
    leave_TaskFlow_function()
   case _:
    print("answer invalide ")
 return


main_loop(answer)
 