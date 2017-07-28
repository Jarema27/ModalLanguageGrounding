from src.sc.pwr.inz.memory.semantic.ObjectType import ObjectType


class SingleThreadCycle:

    def main(self):
        self.first_scenario()

    def first_scenario(self):
        object_type = ObjectType.get_object_types()
        print(object_type)
if __name__ == "__main__":
    a = SingleThreadCycle()
    a.main()
