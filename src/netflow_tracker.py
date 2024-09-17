from src.eth_client import EthClient
from src.config import WALLET_ADDRESSES
import json
import logging

logging.basicConfig(filename='logs/tracker.log', level=logging.INFO)

class NetflowTracker:
    def __init__(self):
        self.eth_client = EthClient()

    def track_netflows(self):
        netflows = {}
        for address in WALLET_ADDRESSES:
            transactions = self.eth_client.get_transactions(address)
            netflows[address] = transactions
            logging.info(f"Tracked netflows for {address}: {transactions}")

        return netflows

    def save_to_json(self, netflows):
        with open('netflows.json', 'w') as json_file:
            json.dump(netflows, json_file, indent=4)