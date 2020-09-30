###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic follows the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    start = time.time()

    cows2 = cows.copy()
    cowlist = []
    firstPass = True
    capacity = limit
    trip = 0

    while cows2:            # as long as your cow dict isn't empty
        if firstPass:
            cowlist.append([])
            firstPass = False
    
        # Search through available cows to find best one that fits for current trip
        currCow_weight = 0     
        for cow in cows2.keys():                
            if cows2[cow] <= capacity and cows2[cow] > currCow_weight:
                currCow_weight = cows2[cow]
                currCow = cow
        
        # Add it to your list, adjust capacity and remove it from the herd
        cowlist[trip].append(currCow)
        capacity -= currCow_weight
        cows2.pop(currCow)     
        
        # If none of the cows fit, start a new trip
        if all(cows > capacity for cows in cows2.values()):           
            cowlist.append([])
            capacity = limit
            trip +=1
            continue
    
    end = time.time()
    print(end - start)     
    return cowlist  


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    start = time.time()

    result = []
    cowlist = list(cows.keys())
    weight = 0
    for partition in get_partitions(cowlist):
        # If partition has more trips than what we have so far stop trying
        numTrips = len(partition)
        if numTrips > len(result) and len(result) != 0: break

        # Get weight each trip in curr partition, move on if capacity overloads
        for trips in partition:
            weight = 0
            # List comp to get vals from dict, then sum it up
            weight += sum( [ cows[key] for key in trips ] )       
            if weight > limit: break

        if weight > limit: continue

        # If capacity not overloaded, add trips from partition
        for i in range(len(partition)):
            result.append(partition[i]) 

    end = time.time()
    print(end - start)             
    return result


        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("/Users/adityakuroodi/Documents/6002/pset1/ps1_cow_data.txt")

    greedy_cow_transport(cows, 100)
    brute_force_cow_transport(cows, 10)




compare_cow_transport_algorithms()


