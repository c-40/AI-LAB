Input:-
import random

def objective_function(solution):
    return sum(solution)

def generate_neighbor(current_solution):
    neighbor = current_solution[:]
    index = random.randint(0, len(neighbor) - 1)
    neighbor[index] = 1 - neighbor[index] 
    return neighbor

def hill_climbing():
    current_solution = [random.randint(0, 1) for _ in range(10)]  # Generate an initial solution
    current_fitness = objective_function(current_solution)

    while True:
        neighbor = generate_neighbor(current_solution)
        neighbor_fitness = objective_function(neighbor)

        if neighbor_fitness >= current_fitness:
            current_solution = neighbor
            current_fitness = neighbor_fitness
        else:
            break 

    return current_solution, current_fitness

best_solution, best_fitness = hill_climbing()
print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)

Output:-
Best Solution: [0, 0, 0, 0, 1, 1, 1, 0, 1, 1]
Best Fitness: 5
