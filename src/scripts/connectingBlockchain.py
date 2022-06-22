from web3 import Web3
import os


def get_w3():
    return Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))


def get_chain_id() -> int:
    return 1337


def getPublicKey() -> str:
    return "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"


def getPrivateKey() -> str:
    return os.getenv("PRIVATE_KEY")
