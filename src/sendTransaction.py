from src.connectingBlockchain import get_w3, get_chain_id, getPublicKey, getPrivateKey
from src.contractCreation import create_contract, get_abi


nonce = get_w3().eth.getTransactionCount(getPublicKey())


def build_transaction():
    transaction = (
        create_contract()
        .constructor()
        .buildTransaction(
            # This nonce can only be used once
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
