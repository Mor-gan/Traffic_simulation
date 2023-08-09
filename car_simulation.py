import numpy as np

# A function to place cars/cars on the road
def initialize_road(road_length, num_cars, v_max):
    road = [-1] * road_length
    car_positions = np.random.choice(range(road_length), num_cars, replace=False)
    for pos in car_positions:
        road[pos] = np.random.randint(0, v_max + 1)
    return road, car_positions

# Function to move a car based on its speed and position
def move_car(car, position, road_length):
    return (position + car) % road_length

# A function that defines the speed and number of cars  
def calculate_average_speed(road):
    total_speed = sum(speed for speed in road if speed != -1)
    num_cars = len([speed for speed in road if speed != -1])
    return total_speed / num_cars if num_cars > 0 else 0

# A function to simulate traffic for a specific number of cars and number of iterations
def simulate_traffic(road_length, num_cars, num_iterations, v_max=5):
    road, car_positions = initialize_road(road_length, num_cars, v_max)
    simulations = []

    for _ in range(num_iterations):
        for i in range(len(car_positions)):
            current_pos = car_positions[i]
            car = road[current_pos]
            next_pos = move_car(car, current_pos, road_length)
            road[current_pos] = -1
            car_positions[i] = next_pos
            road[next_pos] = car

        simulation = calculate_average_speed(road)
        simulations.append(simulation)

    return simulations
#test
if __name__ == "__main__":
    road_length = 10
    num_cars = 5
    num_iterations = 10
    simulations = simulate_traffic(road_length, num_cars, num_iterations)   
    print("Average speeds:", simulations)