# Marwan Task
def interval_scheduling(jobs):
    # Sort jobs based on end time
    # we sort the jobs based on their ending times, so we  can easily identify if there are any overlapping intervals 
    sorted_jobs = sorted(jobs, key=lambda x: x[1])
    size  = len(sorted_jobs)
    
    # Initialize a list to store the maximum profits
    max_profits = [0] * size
    
    # Iterate through sorted jobs
    # We iterate through the sorted jobs using a for loop. At each iteration, we consider the current job
for i in range(size):
        current_profit = sorted_jobs[i][2]
        print('c',current_profit)
        # Find the latest non-overlapping job
        
# Abdelrahman Task

        # We then search for the latest non-overlapping job by iterating backward through the previously processed jobs
        # backword loop
        for j in range(i - 1, -1, -1):
            print(j)
            if sorted_jobs[j][1] <= sorted_jobs[i][0]:
                current_profit += max_profits[j]
                print(max_profits[j])
                break
        # Store the maximum profit for the current job
        # it compare between the current_profit and the 
        max_profits[i] = max(current_profit, max_profits[i-1] if i > 0 else 0)
    
    return max_profits[-1]
  
 jobs = [(1, 6, 6), (2, 5, 5), (5, 7, 5), (6, 8, 3)]

interval_scheduling(jobs)
