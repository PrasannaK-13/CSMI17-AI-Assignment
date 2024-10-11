# Define the people and their weights
people = {'man': 80, 'woman': 80, 'child1': 30, 'child2': 30}

# Function to check if a given combination of people can cross the river in the boat
def can_cross(group):
    return sum(people[person] for person in group) <= 100

# Recursive function to find the solution
def river_crossing(start_side, end_side):
    if len(start_side) == 0:
        print("All have crossed the river!")
        return
    for i in range(len(start_side)):
        for j in range(i, len(start_side)):
            group = [start_side[i], start_side[j]] if i != j else [start_side[i]]
            if can_cross(group):
                # Move the group across the river
                new_start_side = [p for p in start_side if p not in group]
                new_end_side = end_side + group
                print(f"{group} cross the river.")
                river_crossing(new_start_side, new_end_side)
                # Move one person back
                if len(new_end_side) > 1:
                    person_back = new_end_side[0]
                    print(f"{person_back} returns.")
                    river_crossing(new_end_side, new_start_side + [person_back])
                return

# Initial state: everyone is on the starting side of the river
start_side = ['man', 'woman', 'child1', 'child2']
end_side = []
river_crossing(start_side, end_side)
