from item import Item
from transaction import Transaction
from datetime import datetime
from logger import write_log

LOG_FILE_NAME = "transactionLog.txt"
class TwoPhaseLocking:
    def __init__(self):
        self.transactions = {}
        self.items = {}

    def start_transaction(self, id_transaction):
        transaction = Transaction(id_transaction)
        
        write_log(LOG_FILE_NAME, "-trans_id:" + str(id_transaction))
        
        self.transactions[id_transaction] = transaction

    def end_transaction(self, id_transaction):
        if id_transaction in self.transactions:
            transaction = self.transactions[id_transaction]
            transaction.release_blocks()
            del self.transactions[id_transaction]

    def read_item(self, id_transaction, id_item):
        transaction = self.transactions[id_transaction]
        item = self.items.setdefault(id_item, Item(id_item))

        if transaction.acquire_block(item):
            return item.id_item

        self.end_transaction(id_transaction)
        return None

    def write_item(self, id_transaction, id_item, valor):
        transaction = self.transactions[id_transaction]
        item = self.items.setdefault(id_item, Item(id_item))

        if transaction.acquire_block(item):
            item.id_item = valor
            return item.id_item

        self.end_transaction(id_transaction)
        return None