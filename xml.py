#! /usr/bin/python
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import xml.dom.minidom
from xml.dom.minidom import parseString

for line in open("1.log", "r"):
        xml = line.split("xml:")[1].strip()
        domTree = parseString(xml)
        collection = domTree.documentElement

        id = collection.getElementsByTagName("id")[0].childNodes[0].data

        # if childNodes length is 0, it means this node dosen't have value(null value)
        carNode = collection.getElementsByTagName("car")[0].childNodes
        if len(carNode) == 0:
                car = "null"
        else:
                car = virusNode[0].data

        product = collection.getElementsByTagName("product")[0].childNodes[0].data
        datatype = collection.getAttribute("datatype")
        print str(id) + "\t" + product + "\t" + str(car) + "\t"  + datatype
