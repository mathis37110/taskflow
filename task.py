reponse = None
task = []


while reponse != "4":
 print("------------------------------------------------")
 print("que voulez-vous faire ?")
 print("1. ajouter une tache")
 print("2. supprimer une tache")
 print("3. voir les taches")
 print("4. quitter")
 reponse = input("choix :")
 print(reponse)
 print("----------------------------------------------------")
 if reponse == "1":
  tache_ajout = input("quelle tache voulez vous ajoutez :").strip()
  task.append(tache_ajout)
  print("votre tache ",tache_ajout,"a bien etait ajouter")

 elif reponse == "2":
  tache_supprimer = input("quelle tache voulez vous supprimer :").strip()
  try:
    task.remove(tache_supprimer)
    print("votre tache a bien etait supprimer")
  except ValueError:
    print("cette tache n'existe pas")
 elif reponse == "3":
  print("voici vos tache :")
  for tache in task:
    print(tache)
    
 elif reponse == "4":
  print("au revoir")

 else:
  print("reponse invalide ")
 
