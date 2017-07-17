class IndividualModel:
    identifier = None
    object_type = None

    def __init__(self,idn,ot):
        self.identifier = idn
        self.object_type = ot

    def get_identifier(self):
        return self.identifier

    def get_object_type(self):
        return self.object_type

    def set_identifier(self,idn):
        self.identifier = idn

    def set_object_type(self,ot):
        self.object_type = ot

    def check_if_contains_traits(self, traits):
        for x in traits:
            if x not in self.object_type.get_traits():
                return False
        return True

    def __eq__(self, other):
        return self.identifier.get_code() == other.identifier.get_code()

    def __str__(self):
        return "IndividualModel{" + "identifier=" + self.identifier + " type=" + self.object_type + " };"
