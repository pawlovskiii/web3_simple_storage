from src.scripts.compiledContract import compiledSol
from src.scripts.connectingBlockchain import get_w3


def get_bytecode() -> str:
    return compiledSol()["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]


def get_abi() -> str:
    return compiledSol()["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]


def create_contract():
    return get_w3().eth.contract(abi=get_abi(), bytecode=get_bytecode())
