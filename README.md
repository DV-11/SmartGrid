# SmartGrid


Many houses nowadays have their own solar panels to produce the energy that powers the electronics in the house. Occasionally, they even produce more energy than they consume. This surplus of energy can potentially be returned to the energy providers, but this would require special infrastructure: batteries to collect the energy and cables to connect he houses to the batteries.  However, this infrastructure is not free. Each battery costs $5 000 and each cable segment costs $9. Furthermore, batteries have a limit to the energy they can receive. The total output of all the houses connected to a battery can not exceed the maximum capacity of that battery and at the same time, no house can remain unconnected.  

There are 150 houses and 5 batteries located on a grid in each of the 3 districts. Our job is to find a way to connect each house to a battery while minimizing costs. With such a tremendous amount of possible combinations, we'll try to use different algorithms to find the optimal soultion. The case can be divided into two parts: In the first part, each house must be connected to a battery by a unique cable. In the second part, the same cable or cable section can be used by multiple houses, reducing costs.  

## Algorithms 

### Restricted Greedy

This algorithm is called greedy because it makes the most convenient decision in each step without considering the whole picture. This means that in a randomly determined but always constant order, the algorithm goes trhough all the houses in a district and in each instance, it connects the given house to the closest available battery. The algorithm is restricted because it keeps track of the current output each battery is receiving and won't connect a house to a battery if adding it's output would be too much for the battery. This algorithm is meant for the first part of the case, so it creates unique cables for each house. 

### Shared Randomize

It's called shared because it allows houses to share the cables. In adition to houses being connected to batteries, a cable can be ste from a house to another cable, connecting that house to the destinated battery of the already-existing cable. For each given house, the algorithm chosses randomly from the surrounding cable points or batteries to connect to. 

### Hillclimber 

This one is for the second prat of the case. The hillclimber algorithm starts with a random assignment. All houses get connected to a random battery as a starting point. From there, random adjustments are made (i.e. a random house would be randomly re-connected to another cable or battery) and if the total cost after this adjusment is lower than before, this change is accepted as the new state of the grid. This process is repeated many times, further reducing the total cost with each repetition. 

## Getting started

### Requirements

This codebase is completely written in Python .... In the requirements.txt you will find all packages needed to run the code successfully. 

Install instructions:
```
pip install -r requirements.txt
```

Or via conda:
```
conda install --file requirements.txt
```

### Use

To run an example:
```
python main.py
```

You'll be prompted to choose one of the districts:
```
Choose a district (1, 2, 3)
```

Simply input the number of one of the districts to continue.
Then you must select which algorithm you want to run: 
```
Choose an algorithm dict_keys(['restricted_greedy', 'hillclimber', 'shared_randomize']) 
```

Input the name of the desired algorithm as written on the prompt. 
After runing the algorithm, an image of the resulting grid will be displayed, as well as the total cost. 

### Structure

The following list describes the most important folders and files from the project, and their location:

- **/code**: contains all the code from this project
    - **/code/algorithms**: contains the code for the algorithms
    - **/code/classes**: contains the needed classes for this case
    - **/code/visualization**: contains the code for the visualization
- **/data**: contains the input data files that map the grid, batteries and houses

## Authors
- Storm Hartkamp
- David Valero Martinez
- Jim Li
