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
	print("5. retour")
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
				secondary_loop("tache","description","une",Task,answer2,tasks)
			case "2":
				answer2 = None
				secondary_loop("utilisateur","age","un",User,answer2,user_list)

			case "3":
				print("merci et au revoir !")
		
			case _:
				print("ERREUR : reponse invalide ")

 
def secondary_loop(category,subcategory,determinant,classe,answer2,list):
	while answer2 != "5":
		answer2 = print_choice(category, determinant)
		match answer2:
							
			case "1":
				name = input_and_strip(f"quelle est le nom de votre {category} : ")				
				classe.add(name, input_and_strip(f"quelle est la {subcategory} de votre {category} : "))
				print(f"votre {category} {name} a bien etait ajouter")
							
			case "2":
				try:	
					classe.delete(int(input_and_strip("quelle est l'index que vous voulez supprimer : ")))
				except ValueError:
					print("ERREUR : vous devez mettre un index et non du texte")
				except IndexError:
					print("ERREUR : vous devez mettre un index valide")	
							
			case "3":
				for i,print_to in enumerate(list):
					print(f"nom de votre {category} : {print_to.name}")
					print(f"{subcategory} de votre {category} :  {print_to.description}" if category == "tache" else f"{subcategory} de votre {category} : {print_to.age}"  )
					print(f"index : {i}")
					print()		

			case "4":
				try:
					classe.edit(
						int(input_and_strip("quelle est l'index a modifier : ")),
						input_and_strip(f"quelle est le nouveau nom de votre {category} : "),
						input_and_strip(f"quelle est la nouvelle {subcategory} votre {category}: ")
						)
				except ValueError:
					print("ERREUR : vous devez mettre un index")
				except IndexError:
					print("ERREUR : cette index n'existe pas")		

			case "5":
				print("retour au menu principal")

			case _:
				print("ERREUR : reponse invalide ")
			


main_loop()






