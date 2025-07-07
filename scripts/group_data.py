class GroupData:
    def __init__(self):
        self.order = 0
        self.numOfGenerators = 0
        self.ords = []
        self.indexMap = dict()
        self.indexMapInv = []
        self.product_table = [[]]
        self.op = [[]]

    def __str__(self):
        return f"order={self.order}, numOfGenerators={self.numOfGenerators}, ords={self.ords}, product_table={self.product_table}, indexMap={self.indexMap}, indexMapInv={self.indexMapInv}, op={self.op}"
