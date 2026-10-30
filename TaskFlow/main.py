from utils import input_and_strip
from models.task import Task, tasks
from models.user import User, user_list

def print_choice(category, determinant) -> str:
	print("------------------------------------------------")
	print("que voulez-vous faire ?")
	print(f"1. ajouter {determinant} {category}")
	print(f"2. supprimer {determinant} {category}")
	print(f"3. voir les {category}s")
	print(f"4. modifier {determinant} {category}")
	print(f"5. assigner une tache a un utilisateur")
	print(f"6. retour")
	answer = input_and_strip("choix : ")
	print("----------------------------------------------------")
	return answer


def main_loop() -> None:
	answer = None
	while answer != "3":
		print("quelle menu voulez vous voir")
		print("1. le menu des taches")
		print("2. le menu des utilisateur")
		print("3. quitter task_flow")
		answer = input_and_strip("choix : ")
		


		match answer:
			case "1":
				answer2 = None
				secondary_loop("tache" ,"description", "une", Task, answer2, tasks)
			case "2":
				answer2 = None
				secondary_loop("utilisateur", "age", "un", User, answer2, user_list)

			case "3":
				print("merci et au revoir !")
		
			case _:
				print("ERREUR : reponse invalide ")

 
def secondary_loop(category, subcategory, determinant, _class, answer, list):
	while answer != "6":
		answer = print_choice(category, determinant)
		match answer:
							
			case "1":
				name = input_and_strip(f"quelle est le nom de votre {category} : ")				
				_class.add(name, input_and_strip(f"quelle est la {subcategory} de votre {category} : "))
				print(f"votre {category} {name} a bien etait ajouter")
							
			case "2":
				try:	
					list[int(input_and_strip("quelle est l'index que vous voulez supprimer : "))].delete()					
				except ValueError:
					print("ERREUR : vous devez mettre un index et non du texte")
				except IndexError:
					print("ERREUR : vous devez mettre un index valide")	
							
			case "3":
				for i in list:
					print(list[i].turn_json())
					print(f"index : {i}")
					print()		

			case "4":
				try:
					index_edit = int(input_and_strip("quelle est l'index a modifier : "))
					new_name = input_and_strip(f"quelle est le nouveau nom de votre {category} : ")
					new_subcategory = input_and_strip(f"quelle est la nouvelle {subcategory} votre {category}: ")
					list[index_edit].edit(new_name,new_subcategory)	
				except ValueError:
					print("ERREUR : vous devez mettre un index")
				except IndexError:
					print("ERREUR : cette index n'existe pas")		

			case "5":
				try:
					index_user = int(input_and_strip("quelle est l'index de l'utilisateur a ajouter : "))
					index_task = int(input_and_strip("quelle est l'index de la tache a associer : "))			
					user_list[index_user].assigned_to(index_task)
				except ValueError:
					print("ERREUR : vous devez mettre un index")					
				except IndexError:
					print("ERREUR : cette index n'existe pas")	

			case "6":
				print("retour au menu principal")

			case _:
				print("ERREUR : reponse invalide ")
			


main_loop()






