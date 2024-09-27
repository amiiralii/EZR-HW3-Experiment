# HW3 - The JJR Experiment!

With respect to [EZR](https://github.com/timm/ezr/tree/24Aug14) source code, this repo contains experiments that aim to verify the validity of the following hypothesis, claimed by former CSC 591 students Jacob, Joshua, and Rohan:

>    **JJR: Nothing works better than 50 random guessed for low dimensional problems (less than 6 x attributes), but such random guessing is rubbish for higher dimensional data. Let us test that.**

## Table of contents

 - [**How to run?**](https://github.com/amiiralii/EZR-HW3-Experiment/blob/main/README.md#how-to-run)
 - [**Understanding Results**](https://github.com/amiiralii/EZR-HW3-Experiment/blob/main/README.md#understanding-results)
 - **[Analyzing all results](https://github.com/amiiralii/EZR-HW3-Experiment/blob/main/README.md#analyzing-all-results)**
 - **[Conclusion](https://github.com/amiiralii/EZR-HW3-Experiment/blob/main/README.md#conclusion)**

---------

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


Regarding the experiment, we have a set of methods that we want to see how well each of them performs and compare them with each other. Details about each treatment are accessible in the following table:
| &nbsp;&nbsp;&nbsp;&nbsp;Treatments&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   | Info |
|---|---|
| asIs | Baseline, Chebyshev distance of all rows in the dataset. (Per each row, the normalized sum of the distances of all dependent variables to their ideal value(0 or 1)) |
| dumb,N <br> *N in [20,30,40,50]* | Chebyshev distance of #N Randomly guessed rows |
| smart,N <br> *N in [20,30,40,50]* | Chebyshev distance of #N best rows found by Active Learning Method |


Since randomized paramethers exist in our methods, in order to be able to statistically rely on the results, each experiment is repeated **20** times. This way there are 20 different values reported per each dataset-method pair. By looking at the table, you can find each row representing th results of each pair. 

 - First number in each row is the rank of that treatment compared to all others. These ranks are calculated using **Scott-Knott** method. These ranks identifies whether two distributions are statistically distinguishable or not. For example, in table above, the first three treatments are statistically indistinguishable, thus having the same rank. For more information regarding [SK](https://www.scielo.br/j/tema/a/KMMPHsqnZnW9RnkmDdsYgtH/#:~:text=Scott-Knott%20is%20an%20hierarchical,overlapping%20in%20its%20grouping%20results.) and it's [implementation](https://github.com/amiiralii/EZR-HW3-Experiment/blob/main/stats.py#L118) you can use these links. 
 - Second column of the table simply shows the name of each treatment. For example, `smart,30`.
 - Third column represents the median of the distribution.
 - The forth number is the difference between 0.70th and 0.30th row of the dataset. For example, here each distribution contains 20 different values. If you sort them and find the difference between 6th and 14th value, you can easily calculate the value on the table (0.20 for the first treatment).
 - Last column showcases a visual form of the distribution. 



## Analyzing all results

As mentioned before there are tens of different files looks exactly like `auto93.csv` with differents numbers. Thereby, there is a need for a method to summerize all these results even more. And `rq.sh`, which is already discussed, is the solution. Two outputs of  `rq.sh`, `low-dimension-res.txt` and  `high-dimension-res.txt` demonstrate how well each method perform for different grups of datasets.
Each of these files contains three parts: Rank, EVALS, and DELTAS.

#### RANK shows how often each method appears on each rank. For example, in `high-dimension-res.txt`, you can see smart methods appear on the best rank 88 percent of the time.

    high-dimension-res.txt
    
    RANK       0            1            2             3            4            5
    smart     88           12                                                     
    dumb      56           26           15             3                          
    asIs       3           24           18            26           15           15
                                                     100                          
    
  
>

    low-dimension-res.txt
    
    RANK       0           1            2           3           4
    smart     87          13                                     
    dumb      67          13           20                        
                                                  100            
    asIs                  33           27           7          33
 

#### EVALS shows the mean and standard deviation of the N in the treatments. For example, in `high-dimension-res.txt`, the distribution of N in the smart methods that appear on the best rank is around 31 with a standard deviation of 12.

    high-dimension-res.txt
                             
    #
    #EVALS
    RANK             0            1            2             3            4            5
    smart     31 ( 12)     25 (  0)      0 (  0)       0 (  0)      0 (  0)      0 (  0)
    dumb      28 (  0)     36 (  0)     40 (  0)      30 (  0)      0 (  0)      0 (  0)
    asIs     3840 (  0)   2834 (  0)   11138 (  0)   9306 (  0)   3687 (  0)   34523 (  0)
               0 (  0)      0 (  0)      0 (  0)       0 (  0)      0 (  0)      0 (  0)
   
>

    low-dimension-res.txt
 
    #
    #EVALS
    RANK             0           1            2           3           4
    smart     28 (  4)    35 (  0)      0 (  0)     0 (  0)     0 (  0)
    dumb      26 (  8)    25 (  0)     30 (  0)     0 (  0)     0 (  0)
               0 (  0)     0 (  0)      0 (  0)     0 (  0)     0 (  0)
    asIs       0 (  0)   4118 (  0)   668 (  0)   259 (  0)   643 (  0)
    

#### DELTAS is a metric for improvement regarding the baseline and is calculated with this function :
 $$100 * {asIs - treatment \over asIs}$$

    high-dimension-res.txt
    
    #
    #DELTAS
    RANK             0            1            2             3            4            5
    smart     71 ( 23)     51 (  0)      0 (  0)       0 (  0)      0 (  0)      0 (  0)
    dumb      65 ( 26)     63 (  0)     60 (  0)      75 (  0)      0 (  0)      0 (  0)
               0 (  0)      0 (  0)      0 (  0)      94 (  0)      0 (  0)      0 (  0)
>

    low-dimension-res.txt
    
    #DELTAS
    RANK             0           1            2           3           4
    smart     76 ( 29)    36 (  0)      0 (  0)     0 (  0)     0 (  0)
    dumb      65 ( 29)    61 (  0)     71 (  0)     0 (  0)     0 (  0)
               0 (  0)     0 (  0)      0 (  0)    93 ( 39)     0 (  0)


## Conclusion

Based on the information in `low-dimension-res.txt` and  `high-dimension-res.txt` we can make the following conclusions:

    low-dimension-res.txt
    RANK       0           1            2           3           4
    smart     87          13                                     
    dumb      67          13           20                        
                                                  100            
    asIs                  33           27           7          33
    #
    #EVALS
    RANK             0           1            2           3           4
    smart     28 (  4)    35 (  0)      0 (  0)     0 (  0)     0 (  0)
    dumb      26 (  8)    25 (  0)     30 (  0)     0 (  0)     0 (  0)
               0 (  0)     0 (  0)      0 (  0)     0 (  0)     0 (  0)
    asIs       0 (  0)   4118 (  0)   668 (  0)   259 (  0)   643 (  0)
    #
    #DELTAS
    RANK             0           1            2           3           4
    smart     76 ( 29)    36 (  0)      0 (  0)     0 (  0)     0 (  0)
    dumb      65 ( 29)    61 (  0)     71 (  0)     0 (  0)     0 (  0)
               0 (  0)     0 (  0)      0 (  0)    93 ( 39)     0 (  0)
>

    high-dimension-res.txt
    RANK       0            1            2             3            4            5
    smart     88           12                                                     
    dumb      56           26           15             3                          
    asIs       3           24           18            26           15           15
                                                     100                          
    #
    #EVALS
    RANK             0            1            2             3            4            5
    smart     31 ( 12)     25 (  0)      0 (  0)       0 (  0)      0 (  0)      0 (  0)
    dumb      28 (  0)     36 (  0)     40 (  0)      30 (  0)      0 (  0)      0 (  0)
    asIs     3840 (  0)   2834 (  0)   11138 (  0)   9306 (  0)   3687 (  0)   34523 (  0)
               0 (  0)      0 (  0)      0 (  0)       0 (  0)      0 (  0)      0 (  0)
    #
    #DELTAS
    RANK             0            1            2             3            4            5
    smart     71 ( 23)     51 (  0)      0 (  0)       0 (  0)      0 (  0)      0 (  0)
    dumb      65 ( 26)     63 (  0)     60 (  0)      75 (  0)      0 (  0)      0 (  0)
               0 (  0)      0 (  0)      0 (  0)      94 (  0)      0 (  0)      0 (  0)

In both groups(low and high dimensional), the **smart** methods consistently rank highly, with most evaluations in **rank 0** (88% in the high dimensional, 87% in the low dimensional). Its EVALS and DELTAS scores also remain strong and steady.

The **dumb** methods show more variability but better performance in the low dimensional group, with a higher concentration in **rank 0** (67% vs. 56%).


Finally, considering all the information,

> **Since it is observed that smart methods outperform dumb methods in both groups, JJR hypothesis is not supported by the results of this experiment. Instead, based on the results, it can be concluded that smart methods are more powerful for all datasets. However, if the dataset has fewer than 6 features, it is more probable that a dumb method works as well compared to the datasets with more than 6 features.**

