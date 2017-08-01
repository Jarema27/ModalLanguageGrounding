import xml.etree.ElementTree as ET
import os
from src.sc.pwr.inz.language.components.Trait import Trait
"""
Module used to extract data from various XML files.
"""


class XMLReader:

    def __init__(self):
        tree = ET.parse(os.path.abspath(os.path.dirname(__file__)) + '\config.xml')
        self.root = tree.getroot()

#       1 ObjectTypeDir
#       self.object_type_dir = root.find('varibalepaths').find('objecttypepath').text
    @staticmethod
    def read_object_types_xml():
        """
        :return list(ObjectType): list of Object types read from ObjectTypes.xml
        """
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
        """
        Reads agent's variables kept in one file for variables which exists to ensure flexibility of code
        :return list(int): list of integers
        """
        tree = ET.parse(os.path.abspath(os.path.dirname(__file__)) + '\config.xml')
        root = tree.getroot()
        out = []
        for i, child in enumerate(root):
            for j, childchild in enumerate(child):
                out.append(root[i][j].text)
        return out

    @staticmethod
    def read_ids():
        """
        Reads IDs.xml which contains possible IDs which agent can use in order to tell a difference between objects
        :return list(str): list of strings which one day might become grown up  UniqueNames
        """
        tree = ET.parse(os.path.abspath(os.path.dirname(__file__)) + '\Ids.xml')
        root = tree.getroot()
        out = []
        for i, child in enumerate(root):
            for j, childchild in enumerate(child):
                out.append(root[i][j].text)
        return out
