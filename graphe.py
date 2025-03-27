from graphviz import Graph as GraphvizGraph
import random

class Graph:

    @staticmethod
    def generate_random_graph(num_vertices, num_edges):
        """
        Génère un graphe connexe aléatoire avec un nombre donné de sommets et d'arêtes.
        :param num_vertices: Nombre de sommets dans le graphe.
        :param num_edges: Nombre d'arêtes dans le graphe.
        :return: Une instance de la classe Graph représentant le graphe généré.
        """
        if num_edges < num_vertices - 1 or num_edges > (num_vertices * (num_vertices - 1)) // 2:
            raise ValueError("Le nombre d'arêtes doit être compris entre num_vertices - 1 et num_vertices * (num_vertices - 1) // 2 pour garantir un graphe connexe.")

        edges = []
        vertices = list(range(num_vertices))
        random.shuffle(vertices)
        for i in range(num_vertices - 1):
            u, v = vertices[i], vertices[i + 1]
            edges.append((u, v))

        possible_edges = [(u, v) for u in range(num_vertices) for v in range(u + 1, num_vertices)]
        random.shuffle(possible_edges)

        for edge in possible_edges:
            if len(edges) >= num_edges:
                break
            if edge not in edges:
                edges.append(edge)

        return Graph(num_vertices, edges)
   
    def __init__(self, num_vertices, edges=None):
        """
        Initialise un graphe avec une matrice d'adjacence.
        :param num_vertices: Nombre de sommets dans le graphe.
        """
        assert edges is not None and num_vertices > 0 or (edges is None)
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.colors = []

        if edges is not None:
            for edge in edges:
                self.add_edge(edge[0], edge[1])

    def add_edge(self, u, v):
        """
        Ajoute une arête entre les sommets u et v.
        :param u: Sommet source.
        :param v: Sommet destination.
        """
        if u != v:
            if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
                self.adj_matrix[u][v] = 1
                self.adj_matrix[v][u] = 1

    def remove_edge(self, u, v):
        """
        Supprime l'arête entre les sommets u et v.
        :param u: Sommet source.
        :param v: Sommet destination.
        """
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0

    def get_neighbors(self, vertex):
        """
        Retourne les voisins d'un sommet donné.
        :param vertex: Le sommet pour lequel trouver les voisins.
        :return: Liste des sommets voisins.
        """
        if 0 <= vertex < self.num_vertices:
            return [i for i in range(self.num_vertices) if self.adj_matrix[vertex][i] == 1]
        return []

    def display(self, visual=True):
        """
        Affiche la matrice d'adjacence et/ou génère une image .png du graphe
        :visual (optional): True pour générer le .png , False pour n'afficher que la matrice d'adjacence
        """
        for row in self.adj_matrix:
            print(row)

        if visual:
            self.visualize_with_colors()

    def graph_coloring(self):
        """
        Résout le problème de coloriage de graphe en utilisant un algorithme glouton (introduire une couleur à chaque blocage). 
        :return: Liste des couleurs assignées à chaque sommet.
        """
        if self.num_vertices == 0:
            return []

        colors = [-1] * self.num_vertices
        available_colors = [True] * self.num_vertices
        colors[0] = 0

        for u in range(1, self.num_vertices):
            for neighbor in self.get_neighbors(u):
                if colors[neighbor] != -1:
                    available_colors[colors[neighbor]] = False

            for color in range(self.num_vertices):
                if available_colors[color]:
                    colors[u] = color
                    break

            available_colors = [True] * self.num_vertices

        self.colors = colors
        return colors
    
    def welsh_powell_coloring(self):
        """
        Résout le problème de coloriage de graphe en utilisant l'algorithme de Welsh-Powell.
        :return: Liste des couleurs assignées à chaque sommet.
        """
        if self.num_vertices == 0:
            return []

        degrees = [(i, sum(self.adj_matrix[i])) for i in range(self.num_vertices)]
        degrees.sort(key=lambda x: x[1], reverse=True)

        colors = [-1] * self.num_vertices
        current_color = 0

        for vertex, _ in degrees:
            if colors[vertex] == -1:
                colors[vertex] = current_color
                for other_vertex, _ in degrees:
                    if colors[other_vertex] == -1 and not any(
                        self.adj_matrix[other_vertex][neighbor] == 1 and colors[neighbor] == current_color
                        for neighbor in range(self.num_vertices)
                    ):
                        colors[other_vertex] = current_color
                current_color += 1

        self.colors = colors
        return colors
    
    def welsh_powell_partial_coloring(self, k, inverted=True):
        """
        Welsh-Powell adapté : colore un maximum de sommets avec au plus k couleurs.
        Les sommets non coloriables avec k couleurs restent non coloriés (-1).
        :param k: Nombre maximum de couleurs autorisées.
        :param inverted: Si True, trie les sommets par degré croissant au lieu de décroissant.
        :return: Liste des couleurs assignées aux sommets (non colorié = -1).
        """
        if self.num_vertices == 0:
            return []

        degrees = [(i, sum(self.adj_matrix[i])) for i in range(self.num_vertices)]
        degrees.sort(key=lambda x: x[1], reverse=not inverted)

        colors = [-1] * self.num_vertices

        for current_color in range(k):
            for vertex, _ in degrees:
                if colors[vertex] == -1:
                    if all(colors[neighbor] != current_color for neighbor in self.get_neighbors(vertex)):
                        colors[vertex] = current_color

        self.colors = colors
        return colors

    def visualize_with_colors(self):
        """
        Visualise le graphe en utilisant Graphviz avec des couleurs pour les sommets.
        """
        color_palette = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'cyan', 'lime']
        dot = GraphvizGraph(format='png')

        for i in range(self.num_vertices):
            color = None
            if self.colors != [] and self.colors[i] != -1:
                color = color_palette[self.colors[i] % len(color_palette)]
            dot.node(str(i), label=f'{i}', style='filled' if color else '', fillcolor=color if color else '')

        for u in range(self.num_vertices):
            for v in range(u + 1, self.num_vertices):
                if self.adj_matrix[u][v] == 1:
                    dot.edge(str(u), str(v))

        dot.render('graph_colored_visualization', view=True)