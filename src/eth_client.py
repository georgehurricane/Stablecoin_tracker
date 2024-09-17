# src/eth_client.py

from web3 import Web3
import requests
from src.config import ETH_NODE_URL, BLOCKSCOUT_API_URL

class EthClient:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(ETH_NODE_URL))

    def get_balance(self, address):
        return self.web3.eth.get_balance(address)

    def get_transactions(self, address):
        params = {
            'module': 'account',
            'action': 'txlist',
            'address': address,
            'startblock': 0,
            # 'endblock': 99999999,
            'sort': 'asc',
            'apikey': 'YourBlockscoutAPIKey'  # Replace with your Blockscout API key
        }
        try:
            response = requests.get(BLOCKSCOUT_API_URL, params=params)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")