from collections import deque 

def waterJugSolver(bucket1, bucket2, target, target_bucket):
    """
    Solves the Water Jug Problem for two given bucket sizes.
    Finds the shortest sequence of steps to reach the target amount in the chosen bucket.
    
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

# Example usage with a 5L and 3L bucket, aiming for 4L in bucket1
solution = waterJugSolver(5, 3, 4, 1)

if isinstance(solution, str):
    print(solution)
else:
    for step in solution:
        print(step)
