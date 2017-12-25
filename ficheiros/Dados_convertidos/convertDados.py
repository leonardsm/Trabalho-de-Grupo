import xml.etree.ElementTree as ET
import re
import os
file = 'horario_paulo_Nunes_ESTG_2017-2018.xml'

# tree = ET. parse ( file )
# root = tree . getroot ()
# for node in root :
# print ( node )
# <Element 'teachers ' at 0 x026DF8D0 >
# <Element 'classes ' at 0 x026F96F0 >
# <Element 'subjects ' at 0 x02700360 >
# <Element 'classrooms ' at 0 x02809810 >
# <Element 'lessons ' at 0 x02815C30 >
# <Element 'cards ' at 0 x0284A270 >
# exit ()
def ConvertXMLCardsToCSV ( entity ):
    print ("# Entidade | Entity : %s" % entity )
    tree = ET.parse ( file )
    root = tree.getroot ()
    es = root.find ( entity )
    print (len(es))
    csv_all = ""
    heads = ""
    csv = ""
    f = open(entity + ".txt", "wt")
    for e in es:
        for k in e.keys () :
            heads = heads + "%s;" % k
        break
    heads = heads.rstrip (';')
    print ( heads, file=f )
    for e in es:
        csv = ''
        for k in e.keys () :
            csv = csv + "%s;" % (e.get (k))
        csv = csv.rstrip (';')
        print ( csv, file=f )
    f.close()
tree = ET.parse ( file )
root = tree.getroot ()
for node in root:
    ConvertXMLCardsToCSV ( node.tag)
