#*********************************************************************************#
# FILE: Gallon Bukect Problem                                                     #
#                                                                                 #
# DESCRIPTION: This program solve the Gallon Bucket Problem.                      #
# For example, 2 kids are trying to fetch 4 gallon of water from a streams.       #
# They have only an unmarked 3 gallon bucket and an unmarked 5 gallon bucket.     #
# They shoud be done with fetching 4 in 15 steps.                                 #
# DEVELOPER: Yingqiang Yuan                                                       #
# DEVELOPER PHONE: +1 (509) 288-2111                                              #
# DEVELOPER EMAIL: yingqiang.yuan@gmail.com                                       #
#                                                                                 #
# VERSION: 1.0                                                                    #
# CREATED DATE-TIME: 202502010-14:33 Pacfic Time Zone USA                         #
#                                                                                 #
# VERSION: 1.1                                                                    #
# REVISION DATE-TIME: 20250211-16:54                                              #
# DEVELOPER MAKING CHANGE: First_name Last_name                                   #
# DEVELOPER MAKING CHANGE: PHONE: +1 (XXX) XXX-XXXX                               #
# DEVELOPER MAKING CHANGE: EMAIL: first.last@email.com                            #
#                                                                                 #
# VERSION: 1.2                                                                    #
# REVISION DATE-TimeL 20250212-02:21                                              #
# ADD THE FEATUR WHERE TWO BUCKETS, TARGET VOLUME AND TARGET BUCKET ARE PARAMETER.#
#*********************************************************************************#

from collections import deque 

def waterJugSolver(bucket1, bucket2, target, target_bucket):
    """
    Parameters:
    - bucket1 (int): Capacity of the first bucket.
    - bucket2 (int): Capacity of the second bucket.
    - target (int): The target volume to reach.
    - target_bucket (int): The bucket (1 or 2) where the target volume should appear.
    """
    
    if target > max(bucket1, bucket2):
        return "Impossible: Target exceeds the largest bucket."
    
    if target_bucket not in [1, 2]:
        return "Invalid target bucket! Choose 1 or 2."

    # Determine the final goal state
    if target_bucket == 1:
        goal_state = (target, 0)
    else:
        goal_state = (0, target)

    visited = set()  # Stores visited states to avoid cycles
    queue = deque([((0, 0), [])])  # (current state, list of actions taken)
    
    while queue:
        (currentState, steps) = queue.popleft()
        a, b = currentState  # Current water levels in bucket1 and bucket2
        
        if currentState == goal_state:
            return steps + [(a, b, "Goal reached!")]

        if currentState in visited:
            continue
        visited.add(currentState)

        # Possible actions
        possibleStatesAfterOneAction = [
            ((bucket1, b), "Fill Bucket1"),  
            ((a, bucket2), "Fill Bucket2"),  
            ((0, b), "Empty Bucket1"),       
            ((a, 0), "Empty Bucket2"),       
            ((a - min(a, bucket2 - b), b + min(a, bucket2 - b)), "Pour Bucket1 to Bucket2"),  
            ((a + min(b, bucket1 - a), b - min(b, bucket1 - a)), "Pour Bucket2 to Bucket1") 
        ]
        
        for newState, action in possibleStatesAfterOneAction:
            if newState not in visited:
                queue.append((newState, steps + [(newState[0], newState[1], action)]))
    
    return f"Impossible to reach {goal_state}"

# Example usage with a 5L and 3L bucket, aiming for 4L in bucket2
solution = waterJugSolver(3, 5, 4, 2)

if isinstance(solution, str):
    print(solution)
else:
    for step in solution:
        print(step)
