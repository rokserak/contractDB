from web3 import Web3
import json

with open('node.json') as n:
    node = json.load(n)

with open('contract/contract_info.json') as info:
    contract = json.load(info)


class Client:
    def __init__(self):
        self.w3 = Web3(Web3().HTTPProvider(node['ip']))
        if not self.w3.isConnected():
            print('connection to node failed, check your configuration in node.json')
            exit(1)

        self.address = node['account']
        self.w3.eth.defaultAccount = self.address

        # interface for calling function of contract
        self.interface = self.w3.eth.contract(
                            address=contract['contract_address'],
                            abi=contract['abi']
                        )

        # use as call.function_name(*args)
        # result of function is not shown on blockchain
        self.call = self.interface.caller

    # use as self.transaction('function_name', *args)
    # result of function is shown on blockchain
    # not really useful for reading data from contract
    def transaction(self, func, *args):
        tx_hash = self.interface.functions[func](*args).transact()
        return self.w3.eth.waitForTransactionReceipt(tx_hash)
