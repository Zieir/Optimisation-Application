#!usr/bin/env
#OA2025-TP1
#LALAOUI Rayan rayan.lalaoui@gmail.com
#KERMADJ Zineddine zineddinekermadj@gmail.com
import random
from graphe import Graph
import sys

def main():
    """
    Utilisation en ligne de commande :
    - python main.py <num_vertices> [-v]
      - <num_vertices> : Nombre de sommets pour le graphe aléatoire (entier).
      - -v : Optionnel, active la visualisation PNG du graphe.
    Exemple :
    - python main.py 5 -v
    - python main.py 5
    """
    random.seed(42)
    # Gestion des arguments en ligne de commande
    if len(sys.argv) > 1:
        try:
            num_vertices = int(sys.argv[1])
            generate_png = '-v' in sys.argv

            # Générer un graphe aléatoire et le colorier
            num_edges = random.randint(num_vertices - 1, (num_vertices * (num_vertices - 1)) // 2)
            graph = Graph.generate_random_graph(num_vertices, num_edges)
            print(f"Graphe généré avec {num_vertices} sommets et {num_edges} arêtes :")
            

            # Effectuer le coloriage avec Welsh-Powell
            colors = graph.welsh_powell_partial_coloring(3)
            print(f"Couleurs assignées aux sommets : {colors}")
            graph.display(visual=generate_png)

            return
        except ValueError:
            print("Entrée invalide. Veuillez fournir un entier pour <num_vertices> et éventuellement utiliser -v pour la visualisation.")
            return

    # Comportement par défaut si aucun argument n'est fourni
    N = 50
    moy = 0.0
    for k in range(50):
        random.seed(k)

        cpt = 0
        cptn = 0
        for num_vertices in range(3, 7):
            for num_edges in range(num_vertices - 1, (num_vertices * (num_vertices - 1)) // 2 + 1):
                graph = Graph.generate_random_graph(num_vertices, num_edges)
                for k in range(2, num_vertices):
                    with_inversion = graph.welsh_powell_partial_coloring(k)
                    without_inversion = graph.welsh_powell_partial_coloring(k, inverted=False)
                    cptn += 1
                    
                    is_worse = without_inversion.count(-1) < with_inversion.count(-1)
                    if is_worse: 
                        cpt += 1  
        
        moy += cpt/cptn*100 / N

    print(f"L'inversion est en moyenne : {moy:.2f}% plus efficace.")

if __name__ == "__main__":
    main()