# OA2025-TP1
# LALAOUI Rayan rayan.lalaoui@gmail.com
# KERMADJ Zineddine zineddinekermadj@gmail.com
from grapheWeighted import Graph

def main():
    """# Demander à l'utilisateur le nombre de sommets
    num_vertices = int(input("Entrez le nombre de sommets dans le graphe : "))
    g = Graph(num_vertices)

    # Demander à l'utilisateur d'ajouter des arêtes
    print("Ajoutez les arêtes du graphe (entrez -1 -1 pour arrêter) :")
    while True:
        u, v, w = map(int, input("Entrez une arête (u v w) : ").split())
        if u == -1 and v == -1 and w == -1:
            break
        if 0 <= u < num_vertices and 0 <= v < num_vertices:
            g.add_edge(u, v, w)
            g.add_edge(v, u, w)
        else:
            print("Sommets invalides. Veuillez entrer des sommets entre 0 et", num_vertices - 1)

    # Afficher la matrice d'adjacence
    print("\nMatrice d'adjacence :")
    g.display(False)"""
    
    # Exemple d'utilisation
    edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1), (0, 2, 1)]
    graph = Graph(4, edges)

    if graph.has_hamiltonian_cycle():
        print("Le graphe contient un cycle hamiltonien.")
    else:
        print("Le graphe ne contient pas de cycle hamiltonien.")

if __name__ == "__main__":
    main()
