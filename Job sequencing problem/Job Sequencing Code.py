#Abdallah Code

def JobSequencing(arr):
    
    # To arrange the array in decreasing order by profit
    arr = sorted(arr, key=lambda x: x[2], reverse=True)
    
    # To Get Number of Jobs to Schedule
    Unique_Time = list(set(i[1] for i in arr))

    # Creating 2 Empty Lists
    job_profit = [0] * len(Unique_Time) 

    # Find a free slot for each job
    for i in range(len(Unique_Time)):
        for j in arr:
            if j[1] == Unique_Time[i]:
                job_profit[i] = max(job_profit[i], j[2])
                break
                
    print(len(Unique_Time))
    print(sum(job_profit))
    
    # Our Array
    arr = [[1,4,20],
          [2,1,10],
          [3,1,40],
          [4,1,30]]
          
    # Testing      
    JobSequencing(arr)
