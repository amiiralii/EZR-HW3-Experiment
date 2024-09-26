# HW3 - The JJR Experiment!

With respect to [EZR](https://github.com/timm/ezr/tree/24Aug14) source code, this repo contains experiments that aims to verify the validity of the following hypothesis, claimed by former CSC 591 students Jacob, Joshua, and Rohan:

>    **JJR: Nothing works better than 50 random guessed for low dimensional problems (less than 6 x attributes), but such random guessing is rubbish for higher dimensional data. Let us test that.**

## How to run?

For using this code, you need to have at least **Python3.12** installed on your machine. If you need assist on newer versions of python you can check this [Link](https://www.python.org/downloads/).

To run the experiment, you can open the terminal on your local machine and type:

    Python3.13 extend.py data/optimize/misc/auto93.csv
   This script runs the experiment for the `auto93.csv` dataset 20 times, and print out the results of that single dataset on the terminal.
   In order to run the experiment with all datasets to check whether `JJR` statement works, `script-generator.py` file is used. This piece of python code generates a script per each dataset running the experiment on them and saves the output into a CSV file with the same name as the original dataset. You can use this file with a simple command:
   
    Python3.13 script-generator.py  > exp/script.sh 

After running this line you will find a new file named `script.sh` under the `exp` directory.
\* Remember to have a sub-directory named `exp` in the main directory.
