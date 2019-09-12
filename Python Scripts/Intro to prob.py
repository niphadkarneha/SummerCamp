# 
import numpy as np  

total_tosses = 30
num_heads = 24
prob_head = 0.5

#0 is tail. 1 is heads. Generate one experiment
experiment = np.random.randint(0,2,total_tosses)
print ("Data of the Experiment:", experiment)

#Find the number of heads
print ("Heads in the Experiment:", experiment[experiment==1])  #This will give all the heads in the array
head_count = experiment[experiment==1].shape[0] #This will get the count of heads in the array
print ("Number of heads in the experiment:", head_count)

#Now, the above experiment needs to be repeated 100 times. Let's write a function and put the above code in a loop

def coin_toss_experiment(times_to_repeat):

    head_count = np.empty([times_to_repeat,1], dtype=int)
    
    for times in np.arange(times_to_repeat):
        experiment = np.random.randint(0,2,total_tosses)
        head_count[times] = experiment[experiment==1].shape[0]
    
    return head_count

head_count = coin_toss_experiment(100)

head_count[:10]

print ("Dimensions:", head_count.shape, "\n","Type of object:", type(head_count))

#Number of times the experiment returned 24 heads.
head_count[head_count>=24]

print ("No of times experiment returned 24 heads or more:", head_count[head_count>=24].shape[0])
print ("% of times with 24 or more heads: ", head_count[head_count>=24].shape[0]/float(head_count.shape[0])*100)