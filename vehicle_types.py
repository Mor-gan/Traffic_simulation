import numpy as np
from car_simulation import (move_car, calculate_average_speed)

#Exapnd the initial road function by adding buses
def initialize_road(road_length, num_cars, num_buses, v_max):
    num_vehicles = num_cars + num_buses
    if num_vehicles > road_length:
        return None    
    road = [-1] * road_length
    vehicle_positions = np.random.choice(range(road_length), num_vehicles, replace=False)

    for i in range(num_cars):
        road[vehicle_positions[i]] = np.random.randint(0, v_max + 1)

    for i in range(num_cars, num_vehicles):# Assign bus type
        road[vehicle_positions[i]] = 2  

    return road, vehicle_positions

#Move car method is imported    
def move_bus(position, road_length):
    return (position + 1) % road_length
#Average speed method is imported

#Update method with new vehicle considering the density of the vehicle type
def simulate_traffic_for_density_position(road_length, density_cars, density_buses, num_iterations, v_max=5):
    num_cars = int(road_length * density_cars)
    num_buses = int(road_length * density_buses)   
    if num_cars + num_buses > road_length:
        return None    
    road, vehicle_positions = initialize_road(road_length, num_cars, num_buses, v_max)
    average_speeds = []
    for i in range(num_iterations):
        for i in range(len(vehicle_positions)):
            current_pos = vehicle_positions[i]
            vehicle = road[current_pos]          
            if vehicle == -1:
                continue           
            if vehicle >= 0:
                next_pos = move_car(vehicle, current_pos, road_length)
            else:
                next_pos = move_bus(current_pos, road_length)

            road[current_pos] = -1
            vehicle_positions[i] = next_pos
            road[next_pos] = vehicle
            
        average_speed = calculate_average_speed(road)
        average_speeds.append((density_cars, density_buses, average_speed))

    return average_speeds

#test 
if __name__ == "__main__": # Code inside this block will only execute when the script is run directly

    road_length = 100
    num_iterations = 100
    densities_cars = np.linspace(0.05, 1.0, num=20)
    densities_buses = np.linspace(0.05, 1.0, num=20)
    average_speed_results = []

    for density_cars in densities_cars:
        for density_buses in densities_buses:
         average_speeds = simulate_traffic_for_density_position(road_length, density_cars, density_buses, num_iterations)
         #print(average_speeds)

         if average_speeds:
                average_speed_results.extend(average_speeds)

print (average_speed_results)
