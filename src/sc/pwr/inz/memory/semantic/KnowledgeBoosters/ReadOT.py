import xml.etree.ElementTree as ET
from src.sc.pwr.inz.language.Trait import Trait


class ReadOT:

    @staticmethod
    def read_xml():
        tree = ET.parse('C://Users/radomjar/IdeaProjects/ModalLanguageGroundingv2/src/sc/pwr/inz/memory/semantic/'
                        'KnowledgeBoosters/ObjectTypes.xml')
        root = tree.getroot()
        ot = {}

        for i, child in enumerate(root):
            traits = []
            for j, childchild in enumerate(child.iter('traitname')):
                traits += [Trait(root[i][j].text)]
                ot[root[i].get('id')] = traits
        return ot
ReadOT.read_xml()