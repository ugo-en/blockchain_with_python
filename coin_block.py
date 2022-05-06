"""
Just a simple blockchain block in python

Date Created: Friday, 6th May, 2022
"""
import hashlib


class CoinBlock:
    def __init__(self,previous_block_hash,transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(self.transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

# the following code is just to sample our block
# t1 = "John sends 2 coins to Mark"
# t2 = "Mark sends 5.6 coins to Lisa"
# t3 = "Lisa sends 12.1 coins to Mona"
# t4 = "Mona sends 2.1 coins to Pep"
#
# block1 = CoinBlock("block1",[t1,t2])
#
# print(f"Block 1 data: {block1.block_data}")
# print(f"Block 1 hash: {block1.block_hash}")
#
# print()
#
# block2 = CoinBlock("block2",[t3,t4])
#
# print(f"Block 2 data: {block2.block_data}")
# print(f"Block 2 hash: {block2.block_hash}")
#
