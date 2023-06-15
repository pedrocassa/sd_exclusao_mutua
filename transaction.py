class Transaction:
    def __init__(self, id_transaction):
        self.id_transaction = id_transaction
        self.blocks = []

    def acquire_block(self, item):
        if item.blocked_by == self.id_transaction:
            return True

        if item.blocked_by is None:
            item.blocked_by = self.id_transaction
            self.blocks.append(item)
            
            return True

        return False

    def release_blocks(self):
        for item in self.blocks:
            item.blocked_by = None
            
        self.blocks = []
