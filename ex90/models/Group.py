class Group:
    def __init__(self, GroupID, GroupName):
        self.GroupID = GroupID
        self.GroupName = GroupName
    def __str__(self):
        return f'{self.GroupID}\t{self.GroupName}'