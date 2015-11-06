#!/usr/bin/env python3
__author__ = 'Gabriela'
class RdfXml:
    def __init__(self, namespace,url,files):

        self.namespace = str(namespace)
        self.files = files
        self.url = url


    def addPackage(self,Instance, subconcept, dict, dict2):

        self.output = open(self.files, 'a')
        self.output.write('\n\n\n')
        self.output.write('    <!-- '+self.namespace+'#'+Instance+ ' -->\n\n')
        self.output.write('    <owl:NamedIndividual rdf:about="&'+self.url+';'+Instance+'">\n')
        self.output.write('\t<rdf:type rdf:resource="&'+self.url+';'+subconcept+'"/>\n')
        self.addDataType(dict)
        self.addObjProp(dict2)
        self.output.write('    </owl:NamedIndividual>')
        return 0

    def addDataType(self,dict):
        keys = list(dict.keys())
        for l in keys:
            self.output.write('\t<'+l+'>'+dict[l][0]+"</"+l+'>\n')
        return 0

    def addObjProp(self,dict):
        keys = list(dict.keys())
        for l in keys:
            if len(dict[l])>1:
                for s in dict[l]:
                    self.output.write('\t<'+l+' '+'rdf:resource="&'+self.url+';'+s+'"/>\n')
            else:
                self.output.write('\t<'+l+' '+'rdf:resource="&'+self.url+';'+dict[l][0]+'"/>\n')
        return 0
