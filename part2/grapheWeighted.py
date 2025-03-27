#from graphviz import Graph as GraphvizGraph
import random
class Graph:
       
    def __init__(self, num_vertices, edges = None):
        """
        Initialise un graphe avec une matrice d'adjacence.
        :param num_vertices: Nombre de sommets dans le graphe.
        """
        assert edges is not None and num_vertices >0 or  (edges is None)
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.colors = []

        if edges is not None:
            for edge in edges:
                self.add_edge(edge[0], edge[1], edge)

        

    def add_edge(self, u, v, w):
        """
        Ajoute une arête entre les sommets u et v.
        :param u: Sommet source.
        :param v: Sommet destination.
        """
        if u != v : 
            if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
                self.adj_matrix[u][v] = w
                self.adj_matrix[v][u] = w  # Pour un graphe non orienté

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

    def display(self, visual = True):
        """
        Affiche la matrice d'adjacence.
        """
        for row in self.adj_matrix:
            print(row)

        if visual:
            self.visualize_with_colors()
        
    def visualize_with_colors(self):
        
        # Visualise le graphe en utilisant Graphviz avec des couleurs pour les sommets.
        #:param colors: Liste des couleurs assignées à chaque sommet.
        
        # Liste de couleurs prédéfinies
        color_palette = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'cyan', 'lime']

        # Créer un graphe Graphviz
        dot = GraphvizGraph(format='png')

        # Ajouter les sommets avec leurs couleurs
        for i in range(self.num_vertices):
            color = None
            if self.colors != [] and self.colors[i] != -1:
                color = color_palette[self.colors[i] % len(color_palette)]  # Assigner une couleur depuis la palette
            dot.node(str(i), label=f'{i}', style='filled' if color else '', fillcolor=color if color else '')

        # Ajouter les arêtes
        for u in range(self.num_vertices):
            for v in range(u + 1, self.num_vertices):  # Éviter les doublons pour un graphe non orienté
                if self.adj_matrix[u][v] == 1:
                    dot.edge(str(u), str(v))

        # Sauvegarder et afficher le graphe
        dot.render('graph_colored_visualization', view=True)

    def has_hamiltonian_cycle(self):
        """
        Vérifie s'il existe un cycle hamiltonien dans le graphe.
        :return: True si un cycle hamiltonien existe, False sinon.
        """
        def is_valid_vertex(v, pos, path):
            # Vérifie si le sommet v peut être ajouté au chemin
            if self.adj_matrix[path[pos - 1]][v] == 0:  # Vérifie la connectivité
                return False
            if v in path:  # Vérifie si le sommet est déjà dans le chemin
                return False
            return True

        def hamiltonian_cycle_util(path, pos):
            # Si tous les sommets sont inclus dans le chemin
            if pos == self.num_vertices:
                # Vérifie si le dernier sommet est connecté au premier
                return self.adj_matrix[path[pos - 1]][path[0]] != 0

            # Essaye d'ajouter un sommet au chemin
            for v in range(self.num_vertices):
                if is_valid_vertex(v, pos, path):
                    path[pos] = v
                    if hamiltonian_cycle_util(path, pos + 1):
                        return True
                    # Backtracking
                    path[pos] = -1
            return False

        # Initialise le chemin avec -1
        path = [-1] * self.num_vertices
        # Commence avec le premier sommet
        path[0] = 0

        return hamiltonian_cycle_util(path, 1)
