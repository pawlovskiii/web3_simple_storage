from solcx import compile_standard, install_solc

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Compile Out Solidity
def compiledSol():
    install_solc("0.6.4")
    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
            "settings": {"outputSelection": {"*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}}},
        },
        solc_version="0.6.4",
    )
    return compiled_sol
