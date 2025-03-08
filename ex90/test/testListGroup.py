from chap4.ex90.models.listGroup import listGroup

lg = listGroup()
filename = 'group_list.xml'
lg.import_data_from_xml(filename)
print('List of groups after importing:')
lg.print_groups()