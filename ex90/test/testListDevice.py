from chap4.ex90.models.listDevice import listDevice

ld = listDevice()
filename = 'device_list.xml'
ld.import_data_from_xml(filename)
print('list of devices after importing:')
ld.print_devices()