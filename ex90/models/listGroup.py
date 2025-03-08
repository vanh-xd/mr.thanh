from xml.dom import minidom

from chap4.ex90.models.Group import Group


class listGroup:
    def __init__(self):
        self.group_list = {}

    def import_data_from_xml(self, filename):
        dom_tree = minidom.parse(filename)
        root = dom_tree.documentElement

        group_elements = root.getElementsByTagName("group")
        for group in group_elements:
            group_id = group.getElementsByTagName("id")[0].childNodes[0].data.strip()
            group_name = group.getElementsByTagName("name")[0].childNodes[0].data.strip()
            self.group_list[group_id] = Group(group_id, group_name)

    def print_groups(self):
        print("\nDevice Groups:")
        for group in self.group_list.values():
            print(group)