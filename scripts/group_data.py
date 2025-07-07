class GroupData:
    def __init__(self):
        self.order = 0
        self.numOfGenerators = 0
        self.ords = []
        self.indexMap = dict()
        self.indexMapInv = []
        self.productTable = [[]]
        self.op = [[]]
        self.invs = []

    def __str__(self):
        return f"order={self.order}, numOfGenerators={self.numOfGenerators}, ords={self.ords}, productTable={self.productTable}, indexMap={self.indexMap}, indexMapInv={self.indexMapInv}, op={self.op}, invs={self.invs}"
