# SmartGrid


Many houses nowadays have their own solar panels to produce the energy that powers the electronics in the house. Occasionally, they even produce more energy than they consume. This surplus of energy can potentially be returned to the energy providers, but this would require special infrastructure. All houses in a district must be connected to the available batteries in that same distrcit to collect the excess of energy.  However, this infrastructure is not free. Each battery costs $5 000 and each cable segment costs $9. 

There are 150 houses and 5 batteries located on a grid in each of the 3 districts. Our job is to find a way to connect each house to a battery while minimizing costs. With such a tremendous amount of possible combinations, we'll try to use different algorithms to find the optimal soultion. 
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