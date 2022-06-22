import json
from web3 import Web3
import os
from dotenv import load_dotenv
from src.compiledContract import compiledSol

load_dotenv()


with open("compiled_code.json", "w") as file:
    json.dump(compiledSol(), file)

# get bytecode
bytecode = compiledSol()["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compiledSol()["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# for connecting to ganache-cli
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
chain_id = 1337
my_address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
private_key = os.getenv("PRIVATE_KEY")

# Create the contract in Python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get the lastest transaction
nonce = w3.eth.getTransactionCount(my_address)

# 1. Build a transaction
transaction = SimpleStorage.constructor().buildTransaction(
    # This nonce can only be used once
    {"gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce}
)

# 2. Sign a transaction
signed_tx = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# 3. Send a transaction
print("Deploying contract...")
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Deployed!")

# To work with the contract, we always need:
# 1. contract address
# 2. contract ABI
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
# Call -> simulate making the call and getting a return value (these don't make a state change -> same as blue buttons in remix)
# Transact -> Actually make a state change (in here we need to build/sign and send a transaction -> same as orange buttons in remix)

# Initial value of favorite number
print(simple_storage.functions.retrieve().call())
print("Updating Contract...")
store_transaction = simple_storage.functions.store(15).buildTransaction(
    # A nonce can only be used once for each transaction, that's why we add + 1
    {"gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce + 1}
)
signed_store_tx = w3.eth.account.sign_transaction(store_transaction, private_key=private_key)
send_store_tx = w3.eth.send_raw_transaction(signed_store_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)
print("Updated!")