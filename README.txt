----DESCRIPTION----
This script Parse a text file containing information about the packages into RDF, creating a complete RDF Ontology.
It connects to cwm, to convert a RDF file into Notation 3.
It connects to Pellet reasoner, to check consistency of the Ontology and to make queries to a given Ontology.

---- PRE-REQUISITES----
Python3
libraries: re,os
Pellet 2.3.1
cwm 1.2.1

---INSTALLATION-----
1. Place LabWorkOntology Folder in Desktop, within Pellet and cwm folders (three of them should be in Desktop).
2. For running, from the Terminal:
    $ cd ~/Desktop/LabWorkOntology/
    $./main.py

--- FILES TO PARSE ----

As an example this folder contains a file to parse name PackageStable.txt, it contains the Debian Packages
with Distribution: Stable, Section: Main and Architecture:i386, if you want to add another file to parse please
add the file into this folder.

You can use this file to check how the program works on to parse the text file into a RDF Ontology.

-----EXAMPLE------
Two files are provided as examples, OntologyBase.owl and ontology.owl, you can play with these files to convert them into Notation3,
check consistency and fire some queries, to find out how the program works

----PROBLEMS-----
For any problem, please send an email to gabrielahrlr@gmail.com

