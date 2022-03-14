# Working with Web3.py within SimpleStorage contract

## Table of contents
* [General info](#general-info)
* [Learned experience during the project](#learned-experience-during-the-project)
* [Setup](#setup)
### General info
This project was my first contact with Web3.py. Before that I played around with Remix IDE and created SimpleStorage contract. In here I was mainly working with ganache via desktop app, ganache-cli (console version of dekstop app) and TestNet (Rinkeby).
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

#### Additional file for private key
There's three different ways of working with this project and each way require different approach with certain things like (changing public/private keys, HTTPProvider and chain_id).
1. Using [Ganache](https://trufflesuite.com/ganache/index.html)
2. Using [ganache-cli](https://trufflesuite.com/ganache/index.html)
3. Using TestNet (e.g Rinkeby)

Ganache and ganache-cli are quite similar. The difference is that in ganache-cli you're using command line instead of desktop app.


You must create file named **.env** in order to put there your exported private key (no matter, which way above you choose), but if you prefer working with TestNet I suggest to use [MetaMask](https://metamask.io/). It has to be in hexadecimal version, so we put **0x** at the beginning (only when you use TestNet, in ganache is right away, so check it carefully). 
```
export PRIVATE_KEY=0x...
```

To clone and run this application, you'll need [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/download/) (which comes with [npm](http://npmjs.com)) installed on your computer. In this case Node.js is only needed for installing prettier-plugin for Solidity. Furthermore you'll have to download [Python](https://www.python.org/downloads/) 3.6+ version in order to install all the required packages via pip. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/pawlovskiii/web3_simple_storage

# Go into the repository
$ cd web3_simple_storage

# Install web3.py
$ pip install web3

# Install python-dotenv
$ pip install python-dotenv

# Install ganache-cli
$ npm install -g ganache-cli

# Install dependencies
$ npm install 
```

After installing above dependencies I suggest to use below commands in order to play around with the project.
Within Ganache approach firstly open the desktop app in order to spin up the local blockchain (remember to check HTTPProvider address and public/private keys).
If you prefer command line, simply type below command.
```bash
# Run a local blockchain (always spin up with the exact same private/public keys)
$ ganache-cli --deterministic

# Run the app
$ python .\deploy.py
```