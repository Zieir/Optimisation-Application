from graphe import Graph

# Test de la méthode add_edge
g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
assert g.adj_matrix[0][1] == 1, "Erreur : l'arête (0, 1) n'a pas été ajoutée correctement."
assert g.adj_matrix[1][0] == 1, "Erreur : l'arête (1, 0) n'a pas été ajoutée correctement."
assert g.adj_matrix[1][2] == 1, "Erreur : l'arête (1, 2) n'a pas été ajoutée correctement."
assert g.adj_matrix[2][1] == 1, "Erreur : l'arête (2, 1) n'a pas été ajoutée correctement."

# Test de la méthode remove_edge
g.remove_edge(0, 1)
assert g.adj_matrix[0][1] == 0, "Erreur : l'arête (0, 1) n'a pas été supprimée correctement."
assert g.adj_matrix[1][0] == 0, "Erreur : l'arête (1, 0) n'a pas été supprimée correctement."
assert g.adj_matrix[1][2] == 1, "Erreur : l'arête (1, 2) a été supprimée par erreur."
assert g.adj_matrix[2][1] == 1, "Erreur : l'arête (2, 1) a été supprimée par erreur."

# Test de la méthode get_neighbors
neighbors = g.get_neighbors(1)
assert neighbors == [2], f"Erreur : les voisins du sommet 1 sont incorrects. Attendu : [2], Obtenu : {neighbors}"

# Test de la méthode graph_coloring
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)
colors = g.graph_coloring()
for u in range(g.num_vertices):
    for v in g.get_neighbors(u):
        assert colors[u] != colors[v], f"Erreur : les sommets adjacents {u} et {v} ont la même couleur."

# Test d'un graphe vide
g = Graph(0)
assert g.adj_matrix == [], "Erreur : la matrice d'adjacence d'un graphe vide n'est pas correcte."
assert g.graph_coloring() == [], "Erreur : le coloriage d'un graphe vide n'est pas correct."

print("Tous les tests ont réussi.")