# HW3 - The JJR Experiment!

With respect to [EZR](https://github.com/timm/ezr/tree/24Aug14) source code, this repo contains experiments that aim to verify the validity of the following hypothesis, claimed by former CSC 591 students Jacob, Joshua, and Rohan:

>    **JJR: Nothing works better than 50 random guessed for low dimensional problems (less than 6 x attributes), but such random guessing is rubbish for higher dimensional data. Let us test that.**



## How to run?

For using this code, you need to have at least **Python3.12** installed on your machine. If you need assist on newer versions of python you can check this [Link](https://www.python.org/downloads/).

To run the experiment, you can open terminal on your local machine and type:

    Python3.13 extend.py data/optimize/misc/auto93.csv
   This script runs the experiment for the `auto93.csv` dataset 20 times, and print out the results of that single dataset on the terminal.
   In order to run the experiment with all datasets to check whether `JJR` statement works, `script-generator.py` file is used. This piece of python code generates a script per each dataset running the experiment on them and saves the output into a CSV file with the same name as the original dataset. You can use this file with a simple command:
   
    Python3.13 script-generator.py  > exp/script.sh 

After running this line you will find a new file named `script.sh` under the `exp` directory.
\* Remember to have a sub-directory named `exp` in the main directory.

---
Now, your tank is full of gas and you only need the following script to Ignite the fire!

    bash exp/script.sh
Following running this script you will find tens of processes starts simoulteanously. (each runs the experiment with a different dataset) After a while, results from each execution starts to show up on your terminal. You can ignore them since all of them are also saved into a file. 
When all executions are done you can check the following directories to find the results for each dataset:

    exp/res/low-dimension/
    exp/res/high-dimension/

Results of the datasets with less than 6 features can be found in the first sub-directory, and the rest are in the second one.
Now it's the time for analyzing results. For this purpose there is a script file in the main directory called `rq.sh`. By running this file you can analyze all of the results you gathered so far, and make conclusions about stuff. You may run this file with the following command.

    bash rq.sh exp/res/low-dimension/ > low-dimension-res.txt
   
Keep in mind that `rq.sh` should be runned twice, one for low dimensional results and one for high dimensional results. Once you have two files, `low-dimension-res.txt` and  `high-dimension-res.txt`, you have all the materials you need to wrap-up the experiment with statistically reliable, data-driven conclusions!
