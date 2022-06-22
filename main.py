from dotenv import load_dotenv
from src.scripts.connectingBlockchain import get_w3
from src.scripts.sendTransaction import nonce
from src.scripts.contractCreation import get_abi
from src.scripts.sendTransaction import deploying_contract
from src.scripts.contractManipulation import checkStoredNumber, storeNumberInContract

load_dotenv()

simple_storage = get_w3().eth.contract(address=deploying_contract().contractAddress, abi=get_abi())

checkStoredNumber(simple_storage)
print("Updating Contract...")
storeNumberInContract(simple_storage, 15, nonce)
print("Updated!")
checkStoredNumber(simple_storage)
