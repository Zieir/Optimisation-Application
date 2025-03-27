import math
from grapheWeighted import Graph
from heuristiques import nearest_neighbor_tsp, recuit_simule, two_opt_tsp

def distance(point1, point2):
    """
    Calcule la distance euclidienne entre deux points.
    :param point1: Tuple (x1, y1) représentant le premier point.
    :param point2: Tuple (x2, y2) représentant le second point.
    :return: Distance euclidienne entre les deux points.
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def create_graph_from_points(points, threshold):
    """
    Crée un graphe à partir d'une liste de points et d'un seuil de distance.
    :param points: Liste de tuples représentant les coordonnées des points [(x1, y1), (x2, y2), ...].
    :param threshold: Distance maximale pour connecter deux points.
    :return: Objet Graph représentant le graphe construit.
    """
    num_points = len(points)
    edges = []

    for i in range(num_points):
        for j in range(i + 1, num_points):
            if distance(points[i], points[j]) <= threshold:
                edges.append((i, j, 1))  # Ajouter une arête entre les points i et j

    return Graph(num_points, edges)

def graph_to_distance_matrix(graph, points):
    """
    Convertit un graphe en une matrice de distances complète.
    :param graph: Objet Graph représentant le graphe.
    :param points: Liste des coordonnées des points [(x1, y1), (x2, y2), ...].
    :return: Matrice des distances.
    """
    num_points = len(points)
    distance_matrix = [[math.inf] * num_points for _ in range(num_points)]

    for i in range(num_points):
        for j in range(num_points):
            if i == j:
                distance_matrix[i][j] = 0  # La distance d'un point à lui-même est 0
            elif graph.adj_matrix[i][j] != 0:  # Si une arête existe, calculer la distance
                distance_matrix[i][j] = distance(points[i], points[j])

    return distance_matrix


# Exemple d'utilisation
if __name__ == "__main__":
    # Liste des coordonnées
    points = [(0, 0), (3, 2), (10, 4), (8, 6), (1, 5), (7, 9), (4, 9), (5, 6), (8, 2), (4, 4), (9, 9), (10, 5), (2, 6)]
    threshold = math.inf  # Tous les points peuvent être connectés dans cet exercice

    # Créer le graphe à partir des points
    graph = create_graph_from_points(points, threshold)
    
    # Convertir le graphe en matrice de distances
    distance_matrix = graph_to_distance_matrix(graph, points)

    # Appliquer les heuristiques
    print("=== Heuristique du plus proche voisin ===")
    tour, distance = nearest_neighbor_tsp(distance_matrix)
    print(f"Tour: {tour}, Distance: {distance:.2f}")

    print("\n=== Recuit simulé ===")
    tour, distance = recuit_simule(distance_matrix, initial_temperature=1000, cooling_rate=0.99, max_iterations=1000)
    print(f"Tour: {tour}, Distance: {distance:.2f}")

    print("\n=== 2-opt ===")
    initial_tour = list(range(len(points))) + [0]  # Chemin initial
    tour, distance = two_opt_tsp(distance_matrix, initial_tour)
    print(f"Tour: {tour}, Distance: {distance:.2f}")