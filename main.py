#OA2025-TP1
#LALAOUI Rayan rayan.lalaoui@gmail.com
#KERMADJ Zineddine zineddinekermadj@gmail.com

from graphe import Graph

def main():
    # Demander à l'utilisateur le nombre de sommets
    num_vertices = int(input("Entrez le nombre de sommets dans le graphe : "))
    g = Graph(num_vertices)

    # Demander à l'utilisateur d'ajouter des arêtes
    print("Ajoutez les arêtes du graphe (entrez -1 -1 pour arrêter) :")
    while True:
        u, v = map(int, input("Entrez une arête (u v) : ").split())
        if u == -1 and v == -1:
            break
        if 0 <= u < num_vertices and 0 <= v < num_vertices:
            g.add_edge(u, v)
            g.add_edge(v, u)
        else:
            print("Sommets invalides. Veuillez entrer des sommets entre 0 et", num_vertices - 1)

    # Afficher la matrice d'adjacence
    print("\nMatrice d'adjacence :")
    g.display()

    # Résoudre le problème de coloriage de graphe
    print("\nColoriage du graphe :")
    colors = g.graph_coloring()
    print("Couleurs assignées :", colors)

if __name__ == "__main__":
    main()