from src.scripts.connectingBlockchain import get_w3, get_chain_id, getPublicKey, getPrivateKey
from src.scripts.contractCreation import create_contract


nonce = get_w3().eth.getTransactionCount(getPublicKey())


def build_transaction() -> dict:
    transaction: dict = (
        create_contract()
        .constructor()
        .buildTransaction(
            {
                "gasPrice": get_w3().eth.gas_price,
                "chainId": get_chain_id(),
                "from": getPublicKey(),
                "nonce": nonce,
            }
        )
    )
    return transaction


def signed_transaction():
    return get_w3().eth.account.sign_transaction(build_transaction(), private_key=getPrivateKey())


def deploying_contract():
    print("Deploying contract...")
    tx_hash = get_w3().eth.send_raw_transaction(signed_transaction().rawTransaction)
    tx_receipt = get_w3().eth.wait_for_transaction_receipt(tx_hash)
    print("Deployed!")
    return tx_receipt
