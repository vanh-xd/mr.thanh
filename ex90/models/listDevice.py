from xml.dom import minidom

from chap4.ex90.models.Device import Device


class listDevice:
    def __init__(self):
        self.device_list = []
    def import_data_from_xml(self, filename):
        dom_tree = minidom.parse(filename)
        root = dom_tree.documentElement

        device_elements = root.getElementsByTagName("device")
        for device in device_elements:
            group_id = device.getAttribute("groupid").strip()
            device_id = device.getElementsByTagName("id")[0].childNodes[0].data.strip()
            device_name = device.getElementsByTagName("name")[0].childNodes[0].data.strip()
            self.device_list.append(Device(group_id, device_id, device_name))

    def print_devices(self):
        print("\nAll Devices:")
        for device in self.device_list:
            print(device)

    def filter_by_group(self, group_id):
        print(f"\nDevices in Group {group_id}:")
        filtered = [device for device in self.device_list if device.get_group_id() == group_id]
        if not filtered:
            print("No devices found for this group.")
        else:
            for device in filtered:
                print(device)

    def get_largest_group(self):
        group_count = {}
        for device in self.device_list:
            group_count[device.group_id] = group_count.get(device.group_id, 0) + 1

        if not group_count:
            print("\nNo devices found.")
            return

        max_group = max(group_count, key=group_count.get)
        print(f"\nGroup {max_group} has the most devices ({group_count[max_group]}).")