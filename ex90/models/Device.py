class Device:
    def __init__(self, GroupID, DeviceID, DeviceName):
        self.GroupID = GroupID
        self.DeviceID = DeviceID
        self.DeviceName = DeviceName
    def __str__(self):
        return f'{self.GroupID}\t{self.DeviceID}\t{self.DeviceName}'
    def get_group_id(self):
        return self.GroupID
