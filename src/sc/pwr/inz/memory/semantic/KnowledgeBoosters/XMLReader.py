import xml.etree.ElementTree as ET
from src.sc.pwr.inz.language.Trait import Trait


class XMLReader:

    def __init__(self):
        tree = ET.parse('C://Users/radomjar/IdeaProjects/ModalLanguageGroundingv2/src/sc/pwr/inz/memory/semantic/'
                        'KnowledgeBoosters/config.xml')
        root = tree.getroot()

#       1 ObjectTypeDir
        self.object_type_dir = root.find('varibalepaths').find('objecttypepath').text

    def read_object_types_xml(self):
        tree = ET.parse(self.object_type_dir)
        root = tree.getroot()
        ot = {}

        for i, child in enumerate(root):
            traits = []
            for j, childchild in enumerate(child.iter('traitname')):
                traits += [Trait(root[i][j].text)]
                ot[root[i].get('id')] = traits
        return ot