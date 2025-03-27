#OA2025-TP1
#LALAOUI Rayan rayan.lalaoui@gmail.com
#KERMADJ Zineddine zineddinekermadj@gmail.com
import random
from graphe import Graph

def main():
    random.seed(42)

    cpt = 0
    cptn =0
    # Tester si le coloriage partiel sans inversion est pire qu'avec inversion
    for num_vertices in range(3, 7):  # Graphes de 3 à 6 sommets
        for num_edges in range(num_vertices - 1, (num_vertices * (num_vertices - 1)) // 2 + 1):  # Nombre d'arêtes
            graph = Graph.generate_random_graph(num_vertices, num_edges)
            for k in range(2, num_vertices):  # Tester avec des couleurs de 2 à num_vertices - 1
                with_inversion = graph.welsh_powell_partial_coloring(k)
                without_inversion = graph.welsh_powell_partial_coloring(k, inverted=False)
                cptn+=1
                
                is_worse = without_inversion.count(-1) < with_inversion.count(-1)
                if is_worse: 
                    cpt +=1  
    
    print(f"Nombre de graphes testé : {cptn} , nombre de graphe ou l'inversion est moins efficace {cpt}\n Pourcentage: {cpt/cptn*100 :.2f}%")


if __name__ == "__main__":
    main()