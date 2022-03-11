# Working with Web3.py within SimpleStorage contract

## Table of contents
* [General info](#general-info)
* [Learned experience during the project](#learned-experience-during-the-project)
* [Setup](#setup)
### General info
This project was my first contact with Web3.py. Before that I played around with Remix IDE and created SimpleStorage contract.

### Learned experience during the project
#### 1. Compilation of smart contract to **bytecode** and **ABI** to enables EVM to read it
I needed to write our own compiler to extract **bytecode** and **ABI** from our SimpleStorage contract. 
#### 2. Ganache ecosystem
Ganache is a simulated or a fake blockchain, that we can actually use to deploy our smart contracts. It's something similar to JavaScript VM in remix IDE. It's much faster and easier to test things rather than standard TestNet like Rinkeby.
#### 3. Building a transaction (build/sign/send)
In here I had to create separate things like:
- creating a contract in Python
- nonce (in order to get the lastest transaction)
- build a transaction (using contract in Python, nonce and few other things to create a dictionary with all the features)
- sign a transaction (using previous dictionary and our private key)
- send a transaction (using singed tx)

#### 4. Working with deployed contract 

### Setup
To clone and run this application, you'll need [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/download/) (which comes with [npm](http://npmjs.com)) installed on your computer. In this case Node.js is only needed for installing prettier-plugin for Solidity. Additionally you'll have to download [Python](https://www.python.org/downloads/) 3.6+ version in order to install all the required packages via pip. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/pawlovskiii/web3_simple_storage

# Go into the repository
$ cd web3_simple_storage

# Install web3.py
$ pip install web3

# Install python-dotenv
$ pip install python-dotenv

# Install dependencies
$ npm install 

# Run the app
$ python .\deploy.py
```