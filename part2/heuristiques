def nearest_neighbor_tsp(distance_matrix):
    """
    Résout le TSP en utilisant l'heuristique du plus proche voisin.
    :param distance_matrix: Matrice des distances entre les villes.
    :return: Liste représentant l'ordre des villes visitées et la distance totale.
    """
    num_cities = len(distance_matrix)
    visited = [False] * num_cities
    tour = [0]  # Commence par la première ville (indice 0)
    visited[0] = True
    total_distance = 0

    for _ in range(num_cities - 1):
        last_city = tour[-1]
        nearest_city = None
        nearest_distance = float('inf')

        for city in range(num_cities):
            if not visited[city] and distance_matrix[last_city][city] < nearest_distance:
                nearest_city = city
                nearest_distance = distance_matrix[last_city][city]

        tour.append(nearest_city)
        visited[nearest_city] = True
        total_distance += nearest_distance

    # Retour à la ville de départ
    total_distance += distance_matrix[tour[-1]][tour[0]]
    tour.append(0)

    return tour, total_distance

import random
import math

def simulated_annealing_tsp(distance_matrix, initial_temperature, cooling_rate, max_iterations):
    """
    Résout le TSP en utilisant le recuit simulé.
    :param distance_matrix: Matrice des distances entre les villes.
    :param initial_temperature: Température initiale.
    :param cooling_rate: Taux de refroidissement.
    :param max_iterations: Nombre maximum d'itérations.
    :return: Liste représentant l'ordre des villes visitées et la distance totale.
    """
    def calculate_total_distance(tour):
        return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    num_cities = len(distance_matrix)
    current_tour = list(range(num_cities)) + [0]  # Chemin initial
    current_distance = calculate_total_distance(current_tour)
    best_tour = current_tour[:]
    best_distance = current_distance

    temperature = initial_temperature

    for _ in range(max_iterations):
        # Générer une solution voisine (échange de deux villes)
        i, j = random.sample(range(1, num_cities), 2)
        new_tour = current_tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        new_distance = calculate_total_distance(new_tour)

        # Accepter la nouvelle solution selon la probabilité de Boltzmann
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
            current_tour = new_tour
            current_distance = new_distance

            if current_distance < best_distance:
                best_tour = current_tour
                best_distance = current_distance

        # Refroidir la température
        temperature *= cooling_rate

    return best_tour, best_distance

def two_opt_tsp(distance_matrix, initial_tour):
    """
    Améliore une solution TSP initiale en utilisant l'algorithme 2-opt.
    :param distance_matrix: Matrice des distances entre les villes.
    :param initial_tour: Solution initiale (liste représentant l'ordre des villes visitées).
    :return: Liste représentant l'ordre des villes visitées et la distance totale améliorée.
    """
    def calculate_total_distance(tour):
        return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    best_tour = initial_tour[:]
    best_distance = calculate_total_distance(best_tour)
    improved = True

    while improved:
        improved = False
        for i in range(1, len(best_tour) - 2):  # Éviter de modifier le point de départ (0)
            for j in range(i + 1, len(best_tour) - 1):
                # Effectuer un échange 2-opt
                new_tour = best_tour[:i] + best_tour[i:j + 1][::-1] + best_tour[j + 1:]
                new_distance = calculate_total_distance(new_tour)

                # Si une meilleure solution est trouvée, l'accepter
                if new_distance < best_distance:
                    best_tour = new_tour
                    best_distance = new_distance
                    improved = True
                    break  # Sortir de la boucle interne pour appliquer le changement
            if improved:
                break  # Sortir de la boucle externe pour appliquer le changement

    return best_tour, best_distance

distance_matrix = [
    [0, 2, 9, 10, 7],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 5],
    [10, 4, 8, 0, 6],
    [7, 3, 5, 6, 0]
]

if __name__ == "__main__":
    initial_tour, initial_distance = nearest_neighbor_tsp(distance_matrix)
    print("Solution initiale (Nearest Neighbor):")
    print(f"Tour: {initial_tour}, Distance: {initial_distance}")

    print("\nSimulated Annealing:")
    tour, distance = simulated_annealing_tsp(distance_matrix, initial_temperature=1000, cooling_rate=0.99, max_iterations=1000)
    print(f"Tour: {tour}, Distance: {distance}")
    
    

    # Amélioration avec 2-opt
    improved_tour, improved_distance = two_opt_tsp(distance_matrix, initial_tour)
    print("\nSolution améliorée (2-opt):")
    print(f"Tour: {improved_tour}, Distance: {improved_distance}")
