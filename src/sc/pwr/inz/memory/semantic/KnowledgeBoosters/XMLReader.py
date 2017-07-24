import xml.etree.ElementTree as ET
import os
from src.sc.pwr.inz.language.components.Trait import Trait


class XMLReader:

    def __init__(self):
        tree = ET.parse(os.path.abspath(os.path.dirname(__file__)) + '\config.xml')
        root = tree.getroot()

#       1 ObjectTypeDir
#       self.object_type_dir = root.find('varibalepaths').find('objecttypepath').text
    @staticmethod
    def read_object_types_xml():
        tree = ET.parse(os.path.abspath(os.path.dirname(__file__)) + '\ObjectTypes.xml')
        root = tree.getroot()
        ot = {}
        print(os.path.abspath(os.path.dirname(__file__)))
        for i, child in enumerate(root):
            traits = []
            for j, childchild in enumerate(child.iter('traitname')):
                traits += [Trait(root[i][j].text)]
                ot[root[i].get('id')] = traits
        return ot

    @staticmethod
    def read_agent_variables():
        pass