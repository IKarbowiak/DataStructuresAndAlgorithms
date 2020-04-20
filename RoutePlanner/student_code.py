import heapq
import math
from collections import defaultdict


def shortest_path(M, start, goal):
    number_of_intersections = len(M.roads)
    if goal > number_of_intersections or start > number_of_intersections or start < 0:
        return []
    
    distance_heap = []
    distance_dict = {}
    
    for i in range(number_of_intersections):
        heapq.heappush(distance_heap, (math.inf, i))
        distance_dict[i] = (math.inf, math.inf)

    shortest_paths = defaultdict(list)

    heapq.heappush(distance_heap, (0, start))
    distance_dict[start] = (0, 0)
    shortest_paths[start].append(start)

    while distance_dict:
        _, current_intersection = heapq.heappop(distance_heap)
        
        if current_intersection not in distance_dict:
            continue
        
        if current_intersection == goal:
            return shortest_paths[current_intersection]
        
        current_g_value = distance_dict.pop(current_intersection)[0]
        
        for intersection in M.roads[current_intersection]:
            if intersection not in distance_dict:
                continue
            g = current_g_value + calculate_distance(M, current_intersection, intersection)
            h = calculate_distance(M, intersection, goal)
            new_distance = g + h
            previous_distance = distance_dict[intersection][0] + distance_dict[intersection][1]
            if previous_distance > new_distance:
                distance_dict[intersection] = (g, h)
                heapq.heappush(distance_heap, (new_distance, intersection))
                shortest_paths[intersection] = shortest_paths[current_intersection] + [intersection]
    
    return []


def calculate_distance(M, start, end):
    x1, y1 = M.intersections[start]
    x2, y2 = M.intersections[end]
    
    return math.sqrt(((x1 - x2)**2.0 + (y1 - y2)**2.0))
