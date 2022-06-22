from src.scripts.compiledContract import compiledSol
from src.scripts.connectingBlockchain import get_w3

# get bytecode
def get_bytecode():
    return compiledSol()["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]


# get abi
def get_abi():
    return compiledSol()["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]


# Create the contract in Python
def create_contract():
    return get_w3().eth.contract(abi=get_abi(), bytecode=get_bytecode())
