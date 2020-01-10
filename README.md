# Multi Agent Project

This project is done in Python 3.7, with the framework FRODO.
The goal is to benchmark different DCOP solution methods on simple FAP problems. You can find a better description of the FAP problem defined by the CELAR [here](http://www7.inra.fr/mia/T/schiex/Doc/CELAR.shtml).

## Architecture of the project

### Input files

We've taken the files provided on the website above and modified some of them in order to ease the parsing (especially the `cst.txt` files). The different instances of the problems can be found in the repository `FullRLFAP\CELAR`.

We've created some lighter instances (`scen00` and `scen12`) with less data, in order to benchmarck solutions like ADOPT or DPOP.

### Python scripts

In the `src` file, we have the Python scripts used in this project :
  - `scen_parse.py` which contains the main function in order to parse the FAP problem files and to create a XCSP file to pass to FRODO.
  - `Main.py` takes 13 instances (from 0 to 12) and creates 13 XCSP files in the repository `problems_xml`.
  - `get_criteria.py` is a simple Python script allowing to get the number of different frequencies used in a solution and the max frequency in a solution. For the FAP problem, it's the two criteria we try to optimize.
  - `plot_graph.py` displays the graphs from an Excel file.

## FRODO files

We've used some customized agents from FRODO in order to measure messages.

## Runtime

In order to run FRODO, you can execute the following commands :
  - With GUI :
    ```
    java -jar frodo2.17.1/frodo2.17.1.jar
    ```
  - Without GUI :
  ```
  java -cp frodo2.17.1/frodo2.17.1.jar frodo2.algorithms.AgentFactory path_to_xml_problem_file path_to_agent_file
  ```

We've used only JaCoP agents because our XCSP files use predicates that are not supported by other agent.

# Results

You can find our different result in the repository `output`. An instance solved with a particular method is split in two files :
  - `METHOD_instance.xml` contains the solution found by the method on this instance. You can find the solution cost and the values assigned to each variable.
  - `METHOD_instance_result.txt` is the output of FRODO in the terminal. You can find the execution time, the number of message sent and the size of information sent.

In order to get some graphs out of all of this, we regroup these information in an Excel file and use a Python script in order to plot the data.
