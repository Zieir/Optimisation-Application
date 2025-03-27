from heuristiques import nearest_neighbor_tsp, recuit_simule, two_opt_tsp

def test_nearest_neighbor_tsp():
    distance_matrix = [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ]
    tour, distance = nearest_neighbor_tsp(distance_matrix)
    print("Nearest Neighbor TSP:")
    print(f"Tour: {tour}, Distance: {distance}")
    assert len(tour) == len(distance_matrix) + 1, "Erreur : le tour ne contient pas toutes les villes."
    assert tour[0] == tour[-1], "Erreur : le tour ne revient pas à la ville de départ."


def test_recuit_simule():
    distance_matrix = [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ]
    tour, distance = recuit_simule(distance_matrix, initial_temperature=1000, cooling_rate=0.99, max_iterations=1000)
    print("\nRecuit Simulé:")
    print(f"Tour: {tour}, Distance: {distance}")
    assert len(tour) == len(distance_matrix) + 1, "Erreur : le tour ne contient pas toutes les villes."
    assert tour[0] == tour[-1], "Erreur : le tour ne revient pas à la ville de départ."


def test_two_opt_tsp():
    distance_matrix = [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ]
    initial_tour = [0, 1, 2, 3, 0]
    tour, distance = two_opt_tsp(distance_matrix, initial_tour)
    print("\n2-opt TSP:")
    print(f"Tour: {tour}, Distance: {distance}")
    assert len(tour) == len(distance_matrix) + 1, "Erreur : le tour ne contient pas toutes les villes."
    assert tour[0] == tour[-1], "Erreur : le tour ne revient pas à la ville de départ."



if __name__ == "__main__":
    test_nearest_neighbor_tsp()
    test_recuit_simule()
    test_two_opt_tsp()
    print("Tous les tests pour heuristiques.py ont réussi.")
