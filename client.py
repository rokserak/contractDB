from web3 import Web3
import json

w3 = Web3(Web3().HTTPProvider('http://127.0.0.1:7545'))
if not w3.isConnected():
    print('connection to node failed')
    exit(1)

# private key is from local testnet so doesn't matter
address = '0x896470F5f5C2a75921103Df31939f9377bB51Ac1'
private_key = '8f089ca5b72b82ebd8640f717b53699fb771fc1d5748e5c7659189b133cedf36'

w3.eth.defaultAccount = address

with open('contract/contract_info.json') as info:
    contract = json.load(info)

interface = w3.eth.contract(
    address=contract['contract_address'],
    abi=contract['abi']
)

# functions that don't return
tx_hash = interface.functions.create(10, 'deset').transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# functions that return value
n = interface.functions.get_number(0).call()
t = interface.functions.get_text(0).call()

print(n, t)
