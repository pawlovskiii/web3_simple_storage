from dotenv import load_dotenv
from src.scripts.connectingBlockchain import get_w3, get_chain_id, getPublicKey, getPrivateKey
from src.scripts.contractCreation import get_abi
from src.scripts.sendTransaction import nonce, deploying_contract

load_dotenv()


# To work with the contract, we always need:
# 1. contract address
# 2. contract ABI
simple_storage = get_w3().eth.contract(address=deploying_contract().contractAddress, abi=get_abi())
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
print(simple_storage.functions.retrieve().call())
