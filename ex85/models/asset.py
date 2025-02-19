class Asset:
    def __init__(self, assetID, assetName, importYear, value):
        self.assetID = assetID
        self.assetName = assetName
        self.importYear = importYear
        self.value = value
    def __str__(self):
        return f'{self.assetID}\t{self.assetName}'