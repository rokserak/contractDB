from web3 import Web3
import json

with open('node.json') as node:
    info = json.load(node)

w3 = Web3(Web3().HTTPProvider(info['ip']))
if not w3.isConnected():
    print('connection to node failed')
    exit(1)

address = info['account']

# bin and abi precompiled with solc via terminal
# solc -o build --bin --ast --asm --abi database.sol
with open('build/database.bin') as db:
    contract_bytecode = db.read()
with open('build/database.abi') as abi:
    contract_abi = json.load(abi)

w3.eth.defaultAccount = address

greeter = w3.eth.contract(
                    abi=contract_abi,
                    bytecode=contract_bytecode
            )

# sent contract on blockchain
tx_hash = greeter.constructor().transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# save contract data in file
contract_data = {
    'abi': contract_abi,
    'owner_address': w3.eth.defaultAccount,
    'contract_address': tx_receipt.contractAddress
}
with open('contract/contract_info.json', 'w') as outfile:
    json.dump(contract_data, outfile)
