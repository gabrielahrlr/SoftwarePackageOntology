#!/usr/bin/env python3
__author__ = 'Gabriela'
import re
from RDFConverter import *
class InstancesParser(str):

    def packagesSep(str,files):
        package = re.sub(r'\,+\n',',',str)
        getFields = re.split(r'\n',package)
       # print(getFields)

        s={}
        for item in getFields:
            key,value = item.split(":",1 )
            s[key]=[value]

        dictData = {k:v for (k,v) in s.items() if k in ['Package', 'Version', 'Description', 'Architecture','Filename', 'Tag', 'Maintainer']}
        dictObj = {k:v for (k,v) in s.items() if k in ['Depends', 'Recommends', 'Suggests', 'Conflicts']}


        finalDictO={}

        #Dictionary data


        #print(packageName)
        #print(packageName)
        s= re.sub(r' ','', dictData['Package'][0])
        dictData['Package']=[s]
        w= re.sub(r' ','', dictData['Version'][0])
        s = re.sub(r'\W+','', w)
        dictData['Version']=[s]
        z= re.sub(r' ','', dictData['Description'][0])
        s = re.sub(r'\W+','', z)
        dictData['Description']=[s]
        e= re.sub(r' ','', dictData['Architecture'][0])
        dictData['Architecture']=[e]
        packageName = dictData['Package'][0]

        if dictData.__contains__('Tag'):
            if re.search('window-manager', dictData['Tag'][0]):
                dictData['Manager'] = ['Window Manager']
                del dictData['Tag']
            else:
                del dictData['Tag']

        elif re.search('window manager',dictData['Description'][0]):
            dictData['Manager'] = ['Window Manager']

      #      del dictData['Tag']


        else:
            dictData['Manager'] = ['Other Manager']

        if re.search('.deb',dictData['Filename'][0]):
            concept = 'DebianPackage'
            del dictData['Filename']
        else:
            concept = 'OtherPackage'
            del dictData['Filename']
        man = re.sub(r' <', ',', dictData['Maintainer'][0])
        man = re.sub(r'>','', man)
        man = re.sub(r' ','_',man)
        if re.search(r'[D|d]ebian', man):
            dictData['Maintainer']= ['Debian Community Maintainer']

        else:
            dictData['Maintainer'] = ['Other Maintainer']

        #Dictionary for Object Properties
        for s in list(dictObj.keys()):
            if s == 'Depends':
                dep = re.split(r',+ | +\|+ | +,|\|', dictObj['Depends'][0])
                aux = []
                aux2 = []
                for l in dep:
                    dep1 = re.split(r' +\(', l)
                    aux.append(dep1)
                for s in aux:
                    aux2.append(s[0])
                s =re.sub(' ','',aux2[0])
                aux2[0]=s
                finalDictO['Depends']=aux2
            if s== 'Recommends':
                dep = re.split(r',+ | +\|+ | +,|\|', dictObj['Recommends'][0])
                aux = []
                aux2 = []
                for l in dep:
                    dep1 = re.split(r' +\(', l)
                    aux.append(dep1)
                for s in aux:
                    aux2.append(s[0])
                s =re.sub(' ','',aux2[0])
                aux2[0]=s
                finalDictO['Recommends']=aux2
            if s == 'Suggests':
                dep = re.split(r',+ | +\|+ | +,|\|', dictObj['Suggests'][0])
                aux = []
                aux2 = []
                for l in dep:
                    dep1 = re.split(r' +\(', l)
                    aux.append(dep1)
                for s in aux:
                    aux2.append(s[0])
                s =re.sub(' ','',aux2[0])
                aux2[0]=s
                finalDictO['Suggests']=aux2
            if s == 'Conflicts':
                dep = re.split(r',+ | +\|+ | +,|\|', dictObj['Conflicts'][0])
                aux = []
                aux2 = []
                for l in dep:
                    dep1 = re.split(r' +\(', l)
                    aux.append(dep1)
                for s in aux:
                    aux2.append(s[0])

                s =re.sub(' ','',aux2[0])
                aux2[0]=s
                finalDictO['Conflicts'] = aux2
        f = RdfXml(' http://www.semanticweb.org/ontomer.owl','ontomer',files)
      #  print(finalDictO)
        RdfXml.addPackage(f, packageName, concept, dictData, finalDictO)
        return 0