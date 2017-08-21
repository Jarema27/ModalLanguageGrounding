"""
Cluster is both the most general tool of ObjectTypes distinction. It's superior to all of it's OT, it defines some,
most basic traits a.e Cluster Fishes - Traits [Smelly, Wet ,Fishy]. OT might belong to few Clusters a.e  Jerry might
belong to Clusters 'Humans' and 'Toxic pieces of human garbage'
"""


class Cluster:

    def __init__(self, string_id, traits):
        self.stringID = string_id
        self.traits = traits

    def get_string(self):
        return self.stringID

    def get_traits(self):
        return self.traits

    def set_traits(self, traits):
        self.traits = traits

    def add_trait_to_cluster(self, trait):
        self.traits.append(trait)
