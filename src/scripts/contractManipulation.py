from src.scripts.connectingBlockchain import get_w3
from src.scripts.connectingBlockchain import get_w3, get_chain_id, getPublicKey, getPrivateKey


def checkStoredNumber(simple_storage):
    print(simple_storage.functions.retrieve().call())


def storeNumberInContract(simple_storage, num, nonce):
    store_transaction = simple_storage.functions.store(num).buildTransaction(
        {"gasPrice": get_w3().eth.gas_price, "chainId": get_chain_id(), "from": getPublicKey(), "nonce": nonce + 1}
    )

    signed_store_tx = get_w3().eth.account.sign_transaction(store_transaction, private_key=getPrivateKey())
    send_store_tx = get_w3().eth.send_raw_transaction(signed_store_tx.rawTransaction)
    tx_receipt = get_w3().eth.wait_for_transaction_receipt(send_store_tx)
