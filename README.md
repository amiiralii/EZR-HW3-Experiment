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

Results of the datasets with less than 6 features can be found in the first sub-directory and the rest are in the second one.
Now it's the time for analyzing results. For this purpose there is a script file in the main directory called `rq.sh`. By running this file you can analyze all of the results you gathered so far, and make conclusions about stuff. You may run this file with the following command.

    bash rq.sh exp/res/low-dimension/ > low-dimension-res.txt
   
Keep in mind that `rq.sh` should be run twice, one for low dimensional results and one for high dimensional results. Once you have two files, `low-dimension-res.txt` and  `high-dimension-res.txt`, you have all the materials you need to wrap-up the experiment with statistically reliable, data-driven conclusions!


## Understanding Results

Now that you can run the experiment it's time to take a look at the results, generated with each dataset. As it discussed before, by running the experiment on each dataset you'll get a output file with the same name as the dataset. In each of these outputs you can see the following pattern with different numbers:


    exp/res/low-dimension/auto93.csv
    #
     0,                  smart,30,  0.25,  0.20, *         ---       |                   
     0,                  smart,40,  0.25,  0.13, *     -------       |                   
     0,                  smart,50,  0.25,  0.00, *------------       |                   
    #
     1,                  smart,20,  0.32,  0.25,    *                |                   
    #
     2,                   dumb,30,  0.37,  0.18, ---   *             |                   
     2,                   dumb,40,  0.37,  0.18, ---   *             |                   
     2,                   dumb,50,  0.39,  0.25,        *            |                   
    #
     3,                   dumb,20,  0.41,  0.13, ------  *           |                   
    #
     4,                  asIs,398,  0.75,  0.16,              -----  |     *------------ 

Regarding the experiment, we have a set of methods that we want to see how well each of them performs and compare them with each other. Details about each treatment is accessible in the following table:
| &nbsp;&nbsp;&nbsp;&nbsp;Treatments&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   | Info |
|---|---|
| asIs | Baseline, Chebyshev distance of all rows in the dataset. (Per each row, the normalized sum of the distances of all dependent variables to their ideal value(0 or 1)) |
| dumb,N <br> *N in [20,30,40,50]* | Chebyshev distance of #N Randomly guessed rows |
| smart,N <br> *N in [20,30,40,50]* | Chebyshev distance of #N best rows found by Active Learning Method |
