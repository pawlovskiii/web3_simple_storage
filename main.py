from dotenv import load_dotenv
from src.connectingBlockchain import get_w3, get_chain_id, getPublicKey, getPrivateKey
from src.contractCreation import create_contract, get_abi

load_dotenv()


# Get the lastest transaction
nonce = get_w3().eth.getTransactionCount(getPublicKey())

# 1. Build a transaction
transaction = create_contract().constructor().buildTransaction(
    # This nonce can only be used once
    {"gasPrice": get_w3().eth.gas_price, "chainId": get_chain_id(), "from": getPublicKey(), "nonce": nonce}
)

# 2. Sign a transaction
signed_tx = get_w3().eth.account.sign_transaction(transaction, private_key=getPrivateKey())

# 3. Send a transaction
print("Deploying contract...")
tx_hash = get_w3().eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = get_w3().eth.wait_for_transaction_receipt(tx_hash)
print("Deployed!")

# To work with the contract, we always need:
# 1. contract address
# 2. contract ABI
simple_storage = get_w3().eth.contract(address=tx_receipt.contractAddress, abi=get_abi())
# Call -> simulate making the call and getting a return value (these don't make a state change -> same as blue buttons in remix)
# Transact -> Actually make a state change (in here we need to build/sign and send a transaction -> same as orange buttons in remix)

# Initial value of favorite number
print(simple_storage.functions.retrieve().call())
print("Updating Contract...")
store_transaction = simple_storage.functions.store(15).buildTransaction(
    # A nonce can only be used once for each transaction, that's why we add + 1
    {"gasPrice": get_w3().eth.gas_price, "chainId": get_chain_id(), "from": getPublicKey(), "nonce": nonce + 1}
)
signed_store_tx = get_w3().eth.account.sign_transaction(store_transaction, private_key=getPrivateKey())
send_store_tx = get_w3().eth.send_raw_transaction(signed_store_tx.rawTransaction)
tx_receipt = get_w3().eth.wait_for_transaction_receipt(send_store_tx)
print("Updated!")
