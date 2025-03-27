class Graph:
    def __init__(self, num_vertices):
        """
        Initialise un graphe avec une matrice d'adjacence.
        :param num_vertices: Nombre de sommets dans le graphe.
        """
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        """
        Ajoute une arête entre les sommets u et v.
        :param u: Sommet source.
        :param v: Sommet destination.
        """
        if u != v : 
            if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
                self.adj_matrix[u][v] = 1
                self.adj_matrix[v][u] = 1  # Pour un graphe non orienté

    def remove_edge(self, u, v):
        """
        Supprime l'arête entre les sommets u et v.
        :param u: Sommet source.
        :param v: Sommet destination.
        """
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0  # Pour un graphe non orienté

    def get_neighbors(self, vertex):
        """
        Retourne les voisins d'un sommet donné.
        :param vertex: Le sommet pour lequel trouver les voisins.
        :return: Liste des sommets voisins.
        """
        if 0 <= vertex < self.num_vertices:
            return [i for i in range(self.num_vertices) if self.adj_matrix[vertex][i] == 1]
        return []

    def display(self):
        """
        Affiche la matrice d'adjacence.
        """
        for row in self.adj_matrix:
            print(row)

    def graph_coloring(self):
        """
        Résout le problème de coloriage de graphe en utilisant un algorithme glouton.
        :return: Liste des couleurs assignées à chaque sommet.
        """
        if self.num_vertices == 0:
            return []  # Retourner une liste vide si le graphe n'a pas de sommets

        colors = [-1] * self.num_vertices  # -1 signifie qu'aucune couleur n'est encore assignée
        available_colors = [True] * self.num_vertices  # Liste des couleurs disponibles

        # Assigner la première couleur au premier sommet
        colors[0] = 0

        # Assigner des couleurs aux sommets restants
        for u in range(1, self.num_vertices):
            # Marquer les couleurs des voisins comme indisponibles
            for neighbor in self.get_neighbors(u):
                if colors[neighbor] != -1:
                    available_colors[colors[neighbor]] = False

            # Trouver la première couleur disponible
            for color in range(self.num_vertices):
                if available_colors[color]:
                    colors[u] = color
                    break

            # Réinitialiser les couleurs disponibles pour le prochain sommet
            available_colors = [True] * self.num_vertices

        return colors