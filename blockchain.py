"""
This is a sample Blockchain that will use the block in the 'coin_block' file

Date Created: Friday, 6th May, 2022
"""
from coin_block import CoinBlock


class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(CoinBlock("0",["Genesis Block"]))

    def create_block_from_transaction(self,transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(CoinBlock(previous_block_hash,transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i+1}: {self.chain[i].block_data}")
            print(f"Hash {i+1}: {self.chain[i].block_hash}\n")

    @property
    def last_block(self):
        return self.chain[-1]


t1 = "Lincoln sends 9.1 coin to Macron"
t2 = "Macron sends 2 coins to Trump"
t3 = "Trump sends 3.4 coins to Buhari"
t4 = "Buhari sends 7.01 coins to Putin"
t5 = "Putin sends 8.31 coins to The Queen"
t6 = "The Queen sends 2.3 coins to Kim Jong Un"


blockchain = Blockchain()

blockchain.create_block_from_transaction([t1,t2])
blockchain.create_block_from_transaction([t3,t4])
blockchain.create_block_from_transaction([t5,t6])

blockchain.display_chain()


