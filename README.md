# Short Corridor Problem

The short corridor problem is an example given in Sutton, Barto: Introduction to Reinforcement Learning. It is solved using a vanilla policy gradient algorithm.

## Requirements

- numpy: https://www.numpy.org/
- matplotlib: https://matplotlib.org/
- scipy: https://www.scipy.org/

## The model

The underlying action space *A*={left, right} is described by a random variable *a*=0,1. The policy is parametrised by the Bernoulli distribution

![alt text](imgs/policy.png "policy")

In this parametrisation, the parameter *θ*∈(0,1) is equivalent to the probability *p* of choosing *a*=1. Given a batch of trajectories, the update rule for the parameter is given by  

![alt text](imgs/updaterule.png "update rule")


## Results

Expected:  
final probability  ≈ 0.59  
mean reward &ensp;&ensp;≈ -11.6 

o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

  &ensp;Initial Probability: &ensp;&ensp;&ensp; 0.43894003064197507  
  &ensp;Discount Factor: &ensp;&ensp;&ensp;&ensp;0.99  
  &ensp;Batch Size:	&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;100  
  &ensp;Number of Episodes:&ensp;10000000  
  &ensp;Learning Rate: &ensp;&ensp;&ensp;&ensp;&ensp; 1e-08  
  &ensp;final mean probability: 0.586863737507272  
  &ensp;final mean reward: &ensp;&ensp; -11.644556  

o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o

![alt text](data/Figure_1.png "plot")

