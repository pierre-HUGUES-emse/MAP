# Multi Agent Project

This project is done in Python 3.7, with the framework FRODO.

## Input files for FRODO

FRODO needs a XML file at the XCSP format. We need to generate this file thanks to 3 other files :
- ``var.txt``
- ``dom.txt``
- ``ctr.txt``

This files go to a translator, outputting a XCSP file, representing the problem we try to solve.

## FRODO

### Prerequisites

You can install Graphviz in order to print out the graph of the problem you're trying to solve.
Java 12 will be necessary to launch FRODO.

FRODO needs the previous XCSP file and a agent file (JaCoP).
It outputs a file containing the solution cost, the solving runtime, the number of messages.

## Goal

We try to benchmark the different algorithms.
