# Continual Next Activity Prediction with Prompts (CNAPwP)

This github page contains the code for CNAPwP. The framework of CNAPwP can be seen in the figure below.

![framework_new_version](https://github.com/user-attachments/assets/c4c99a54-85f3-4ade-a11e-b04d2b5a5fc9)

**Continual Next Activity Prediction with Prompts (CNAPwP)** is an advanced machine learning framework designed to predict the next activity in a sequence of events by leveraging continual learning and prompt-based techniques. CNAPwP continually learns from new data without forgetting previously learned patterns in previous tasks, ensuring accurate and up-to-date predictions. The integration of prompts enhances the model's ability to understand and adapt to various task-specific behaviors, making it a powerful tool for applications in dynamic environments such as user behavior analysis, workflow management, and recommendation systems. 

## The Repository
The repository contains the main code for running CNAPwP, including the preprocessing on the datasets, the configurations of each dataset, and the results. 

In [main.py](main.py) it is possible to run the experiments. In [preprocess.py](Preprocess.py) is the code for converting an event log into a dataset with prefixes. [EPrompt.py](EPrompt.py) and [G_Prompt](G_Prompt.py) contain the code for creating the E- and G-Prompt, respectively. [MHSAM.py](MHSAM.py) contains the Multi Head Self-Attention Model with training and initialization. 

All other files and folders contain additional functions. Such as the [configs](configs) folder containing the configurations for all datasets, the [PrefixtreeCDDmain](PrefixTreeCDDmain) folder containing functions for creating the prefix trees, and the [data.py](Data.py) and [Utils](Utils) folder containing additional functions. 
