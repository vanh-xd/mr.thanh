from chap4.ex90.models.listDevice import listDevice
from chap4.ex90.models.listGroup import listGroup

if __name__ == "__main__":
    group_list = listGroup()
    device_list = listDevice()
    group_filename = "group_list.xml"
    device_filename = "device_list.xml"
    # Import XML Data
    group_list.import_data_from_xml(group_filename)
    device_list.import_data_from_xml(device_filename)

    # (a) Display Device Groups
    group_list.print_groups()

    # (b) Display All Devices
    device_list.print_devices()

    # (c) Filter Devices by Group (Example: g1)
    device_list.filter_by_group("g1")

    # (d) Print the Device Group with Most Devices
    device_list.get_largest_group()