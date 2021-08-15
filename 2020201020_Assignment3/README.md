## Data Systems ( Assignment 3 )

### Files used :

`1) bptree.py` : Python file containing source code for B plus tree implementation. 

`2) input.txt` : Input file with name of his/her choice passed as command line argument. For example, `input.txt` is the name of the input file used. The queries are witten in appropriate format and in consecutive new lines in the input file.

### Output Format:

`1) output.txt` : This text file contains results of the queries present in the input file.

### Execution Flow and Format :

1) User needs to add the input file as a command line input and compile the python source code file in following format:

    `python3 bptree.py input.txt`

    Here, `input.txt` file is the input file used as example. User can pass the input file name of his/her choice using the above format.

2) The results to the queries present in the input file get written to the `output.txt` file.

### Basic Implementation Details :

1) For order=3, every node in the B plus tree can hold a maximum of 2 keys and 3 child pointers.

2) All the leaf nodes in the B-Plus tree contain all the keys and are connected.

3) For `Insertion` operation, we traverse from the root node to the leaf node where the insertion needs to be done. If upon insertion, the number of keys in the leaf node exceeds 2, then that node gets split into 2 parts and the key for which branching occurs is passed to its parent node and is merged with the parent where further validation is done to ensure that the total number of keys do not exceed 2. This process of spliiting and merging continues until we get a stable tree ( where number of keys in any node do not exceed 2).

4) For `Find` operation, we traverse from the root node to the leaf node where the value to be searched is likely to be present. This value is then searched within the keyLst list of the node where the keys are stored during insertion. If value to be searched is found, then `YES` is written to the output.txt file else `NO` is written to the output.txt file.

5) For `Count` operation, we traverse from the root node to the leaf node where the value is likely to be present. The count of that particular value is retieved from the `countLst` list maintained for every node which maintains the count of the values which are inserted in the B-plus tree. This count value is written in the `output.txt` file.

6) For `Range` operation, we use 2 arguments to find the number of values present between these 2 arguments. In this case, we maintain references of the leaf node where each of these arguments are present and then traverse all the leaf nodes connecting these 2 references and using the `countLst` list for each leaf node to write the total number of values present between the 2 input arguments in the `output.txt` file.


 





















