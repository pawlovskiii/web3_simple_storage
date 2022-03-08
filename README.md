# Working with Web3.py within SimpleStorage contract
This project was my first contact with Web3.py. Before that I played around with Remix IDE and created SimpleStorage contract.

## My learning experience within project:
### 1. Compilation of smart contract to **bytecode** and **ABI** to enables EVM to read it
I needed to write our own compiler to extract **bytecode** and **ABI** from our SimpleStorage contract. 
### 2. Ganache ecosystem
Ganache is a simulated or a fake blockchain, that we can actually use to deploy our smart contracts. It's something similar to JavaScript VM in remix IDE. It's much faster and easier to test things rather than standard TestNet like Rinkeby.
### 3. Building a transaction (build/sign/send)
In here I had to create separate things like:
- creating a contract in Python
- nonce (in order to get the lastest transaction)
- build a transaction (using contract in Python, nonce and few other things to create a dictionary with all the features)
- sign a transaction (using previous dictionary and our private key)
- send a transaction (using singed tx)

### 4. Working with deployed contract 