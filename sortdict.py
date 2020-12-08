# -*- coding: UTF-8 -*-

import json

def sortBySpecailValue(inputfile, outputfile):
    def takeSecond(selfitem, otheritem):
        self = selfitem[1] #dict value
        other = otheritem[1]
        if(self.has_key('value') and other.has_key('value')):
            return self['value'] - other['value'] # asc 升序
        elif self.has_key('value'):
            return self['value'] - 0
        elif other.has_key('value'):
            return 0 - other['value']
        else:
            return 0
    
    origindata ={}
    with open(inputfile, 'r') as f:
        origindata = json.load(f)
        newlist = sorted(origindata.items(), takeSecond)
        with open(outputfile, 'w') as f:
            json.dump(newlist, f)
sortBySpecailValue('a.json', 'b.json')