#!/usr/bin/env python3
__author__ = 'Gabriela'

from instancesParser import *
import os
def parser(inputName,outputName):
    file = open(inputName, 'r')
    packagesText = file.read()
    ontologyDefinition = open("OntologyBase.owl", 'r').read()
    filer = open(outputName, "a")
    filer.write(ontologyDefinition)
    packages = re.split(r'\n{2,}', packagesText)
    for i in packages:
        s = InstancesParser.packagesSep(i, outputName)
    filer.write('\n</rdf:RDF>')
    file.close()
    filer.close()
    return s


if __name__ == "__main__":

    ans = True
    while ans:
        output = ''
        print('==============================================')
        print('          Package Manager System              ')
        print('==============================================')
        print('==== DMKM Ontology Project 2015 ==============')
        print('                     Author:Gabriela HERNANDEZ')
        print('==============================================')
        print('\n')
        print('PRINCIPAL MENU')
        print('1. Parse Package instances into a RDF Ontology')
        print('2. Convert a RDF Ontology to Notation 3')
        print('3. Start Reasoning to check consistency')
        print('4. Query an Ontology')
        print('5. Exit')
        option = input('Enter an option number:')
        option = int(option)
        print('\n')
        if option == 1:
            inputName = input('Write the name of the file to parse: ')
            inputName = str(inputName)
            outputName = input('Write the output Ontology name:  ')
            outputName = str(outputName)
            parser(inputName,outputName)
            print('The output Ontology can be found under ~/Desktop/LabWorkOntology as:', outputName)

        if option == 2:
            inputOnto = input('Write the name of the ontology to convert: ')
            inputOnto = str(inputOnto)
            outputOnto = input('Write the name of the output file: ')
            os.chdir('/Users/Gabriela/Desktop/cwm-1.2.1')
            r = './cwm --rdf ~/Desktop/LabWorkOntology/'+inputOnto+ ' --n3 > ~/Desktop/LabWorkOntology/'+outputOnto
            os.system('./cwm --rdf ~/Desktop/LabWorkOntology/'+inputOnto+ ' --n3 > ~/Desktop/LabWorkOntology/'+outputOnto)
            print('Ontology in Notation 3 is saved under ~/Desktop/LabWorkOntology as:', outputOnto)
        if option == 3:
            outputName = input('Write the Ontology name:  ')
            outputName = str(outputName)
            os.chdir('/Users/Gabriela/Desktop/pellet-2.3.1')
            os.system('./pellet.sh consistency -v '+'~/Desktop/LabWorkOntology/'+outputName)
            print('Consistency Checked!')

        if option == 4:
            loop = True
            onto = input('Write The Name of the Ontology to query: ')
            onto = str(onto)
            while loop:
                os.chdir('/Users/Gabriela/Desktop/pellet-2.3.1')
                print("1. List of packages that DEPENDS on a specific package ")
                print("2. List of packages that a specific package DEPENDS ON ")
                print("3. List of packages that are RECOMMENDED by a specific package")
                print("4. List of packages that are SUGGESTED by a specific package")
                print("5. List of Packages CONFLICTING with a specific package")
                print("6. List of Conflicts given a list of Packages to install")
                print("7. List of all Window Manager Packages")
                print("8. List of all Debian Maintainer Packages")
                print("9. Return to the Principal Menu")
                queryOption = input("Please choose a query: ")
                queryOption = int(queryOption)
                if queryOption == 1:
                    packageName = input("Type the name of the package: ")
                    packageName = str(packageName)
                    query1 = open('query1.txt', 'w+')
                    query1.write('PREFIX url: <http://www.semanticweb.org/ontomer.owl#>\n')
                    query1.write('SELECT DISTINCT ?Packages\n')
                    query1.write(
                        'WHERE{' + '\n' + '\turl:' + packageName + ' a url:DebianPackage.\n\turl:' + packageName + ' url:Dependency ?Packages.\n}')
                    query1.close()
                    r = './pellet.sh query -q query1.txt -v '+'~/Desktop/LabWorkOntology/'+ onto
                    os.system(r)

                elif queryOption == 2:
                    packageName = input("Type the name of the package: ")
                    packageName = str(packageName)
                    query2 = open('query2.txt', 'w+')
                    query2.write('PREFIX url: <http://www.semanticweb.org/ontomer.owl#>\n')
                    query2.write('SELECT DISTINCT ?Packages\n')
                    query2.write(
                        'WHERE{' + '\n' + '\turl:' + packageName + ' a url:DebianPackage.\n\turl:' + packageName + ' url:Depends ?Packages.\n}')
                    query2.close()
                    r = './pellet.sh query -q query2.txt -v '+'~/Desktop/LabWorkOntology/'+onto
                    os.system(r)

                elif queryOption == 3:
                    packageName = input("Type the name of the package: ")
                    packageName = str(packageName)
                    query3 = open('query3.txt', 'w+')
                    query3.write('PREFIX url: <http://www.semanticweb.org/ontomer.owl#>\n')
                    query3.write('SELECT ?Packages\n')
                    query3.write(
                        'WHERE{' + '\n' + '\turl:' + packageName + ' a url:Package.\n\turl:' + packageName + ' url:Recommends ?Packages.\n}')
                    query3.close()
                    r = './pellet.sh query -q query3.txt -v '+'~/Desktop/LabWorkOntology/'+onto
                    os.system(r)

                elif queryOption == 4:
                    packageName = input("Type the name of the package: ")
                    packageName = str(packageName)
                    query4 = open('query4.txt', 'w+')
                    query4.write('PREFIX url: <http://www.semanticweb.org/ontomer.owl#>\n')
                    query4.write('SELECT ?Packages\n')
                    query4.write(
                        'WHERE{' + '\n' + '\turl:' + packageName + ' a url:Package.\n\turl:' + packageName + ' url:Suggests ?Packages.\n}')
                    query4.close()
                    r = './pellet.sh query -q query4.txt -v '+'~/Desktop/LabWorkOntology/'+onto
                    os.system(r)

                elif queryOption == 5:
                    packageName = input("Type the name of the package:")
                    packageNAme = str(packageName)
                    query5 = open('query5.txt', 'w+')
                    query5.write('PREFIX url: <http://www.semanticweb.org/ontomer.owl#>\n')
                    query5.write('SELECT DISTINCT ?Conflicts\n')
                    query5.write('WHERE{\n\turl:'+packageName+ ' a url:Package.\n')
                    query5.write('\t{\n\t?y a url:Package.\n\t?Conflicts a url:Package.\n\turl:'+packageName+' url:Depends ?y.\n')
                    query5.write('\t?y url:Conflicts ?Conflicts.\n\t}\n\tUNION\n\t{?Conflicts a url:Package.\n')
                    query5.write('\turl:'+packageName+' url:Conflicts ?Conflicts.\n\t}\n}')
                    query5.close()
                    r = './pellet.sh query -q query5.txt -v '+'~/Desktop/LabWorkOntology/'+ onto
                    os.system(r)

                elif queryOption == 6:
                    packageName = input("Type the name of the packages to install separated by a comma: ")
                    packageName = str(packageName)
                    packageName = packageName.split(r',')
                    s = ''
                    i = 1
                    for pack in packageName:
                        if i < len(packageName):
                            s += 'url:'+pack+', '
                            i += 1
                        else:
                            s += 'url:'+pack
                            i += 1
                    query6 = open('query6.txt', 'w+')
                    query6.write('PREFIX url: <http://www.semanticweb.org/ontomer.owl#>\n')
                    query6.write('SELECT DISTINCT ?Package ?Conflict\n')
                    query6.write('WHERE {\n')
                    query6.write('\t?Package a url:Package.\n')
                    query6.write('\t?Conflict a url:Package.\n')
                    query6.write('\t?Package url:Conflicts ?Conflict.\n')
                    query6.write('\tFILTER(?Package in ('+s+') && ')
                    query6.write('?Conflict in ('+s+')).\n}')
                    query6.close()
                    r = './pellet.sh query -q query6.txt -v '+'~/Desktop/LabWorkOntology/'+onto
                    os.system(r)
                elif queryOption == 7:
                    query7 = open('query7.txt', 'w+')
                    query7.write('PREFIX url: <http://www.semanticweb.org/ontomer.owl#>\n')
                    query7.write('SELECT ?WindowManagerPackages\n')
                    query7.write(
                        'WHERE{\n\t?WindowManagerPackages a url:WindowManagerPackage\n}')
                    query7.close()
                    r = './pellet.sh query -q query7.txt -v '+'~/Desktop/LabWorkOntology/'+onto
                    os.system(r)
                elif queryOption == 8:
                    query8 = open('query8.txt', 'w+')
                    query8.write('PREFIX url: <http://www.semanticweb.org/ontomer.owl#>\n')
                    query8.write('SELECT ?DebianMaintainerPackages\n')
                    query8.write(
                        'WHERE{\n\t?DebianMaintainerPackages a url:DebianMaintainerPackage\n}')
                    query8.close()
                    r = './pellet.sh query -q query8.txt -v '+'~/Desktop/LabWorkOntology/'+onto
                    os.system(r)

                elif queryOption == 9:
                    break

                else:
                    print('Invalid Option, please try again :)')

        if option == 5:
            print('À la prochaine fois!')
            break

