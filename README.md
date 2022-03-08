# Working with Web3.py within SimpleStorage contract
This project was my first contact with Web3.py. Before that I played around with Remix IDE and created SimpleStorage contract.

## My learning experience within project:
### 1. Compilation of smart contract to **bytecode** and **ABI** to enables EVM to read it
I needed to write our own compiler to extract **bytecode** and **ABI** from our SimpleStorage contract. 
### 2. Ganache ecosystem
Ganache is a simulated or a fake blockchain, that we can actually use to deploy our smart contracts. It's something similar to JavaScript VM in remix IDE. It's much faster and easier to test things rather than standard TestNet like Rinkeby.
### 3. Building a transaction (build/sign/send)