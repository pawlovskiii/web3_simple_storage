# Working with Web3.py within SimpleStorage contract

## Table of contents

- [General info](#general-info)
- [Learned experience during the project](#learned-experience-during-the-project)
- [Setup](#setup)
  - [Additional file for environment variable](#additional-file-for-environment-variable)
  - [Specification for using ganache-cli within deploy file](#specification-for-using-ganache-cli-within-deploy-file)
  - [Specification for using Rinkeby TestNet within deploy file](#specification-for-using-rinkeby-testnet-within-deploy-file)
  - [Installing dependencies](#installing-dependencies)
  - [Available commands for the project](#available-commands-for-the-project)

### General info

This project was my first contact with Web3.py. Before that I played around with Remix IDE and created SimpleStorage contract. In here I was mainly working with ganache via desktop app, ganache-cli (console version of dekstop app) and TestNet (Rinkeby).

### Learned experience during the project

#### 1. SimpleStorage contract

I studied the most basic structure of the contract. I wanted to share things that were new for me when entering Solidity language.
- SPDX License.

#### 2. Compilation of smart contract to **bytecode** and **ABI** to enable EVM to read it

I needed to write our own compiler using Web3 to extract **bytecode** and **ABI** from our SimpleStorage contract.

#### 3. Ganache ecosystem

Ganache is a simulated or a fake blockchain, that we can actually use to deploy our smart contracts. It's something similar to JavaScript VM in remix IDE. It's much faster and easier to test things rather than standard TestNet like Rinkeby.

#### 4. Building a transaction

I've learned that a transaction consists of several things like:

- building a transaction
- signing a transaction
- sending a transaction

#### 5. Working with deployed contract

I studied that whenever we work with a **contract** we always need two things:

- contract address
- contract ABI (application binary interface)

#### 6. Keeping safe your private keys

I understood that it's crucial thing for our security. Even if we don't work with real money and we're using empty Metamask account, it's always good to build healthy habits around important topics.

When making transactions into the blockchain there's actually two different ways, that we can interact with them.

1. Interact with a **call**
   - **calls** don't make a state change to the blockchain (nothing on the blockchain would actually change), it's just a simulation
   - we can always just **call** a function no matter what that function is
2. Interact with a **transact**
   - actually make a state change
   - we can also always **transact** on a function even if it's just a _view_

### Setup

There's three different ways of working with this project and each way require different approach with certain things like (changing public/private keys, HTTPProvider and chain_id).

1. Using [Ganache](https://trufflesuite.com/ganache/index.html)
2. Using [ganache-cli](https://www.npmjs.com/package/ganache-cli)
3. Using TestNet (e.g Rinkeby)

Ganache and ganache-cli are quite similar. The difference is that in ganache-cli you're using command line instead of desktop app.

#### Additional file for environment variable

You must create file named **.env** in order to put there your exported private key (no matter, which way above you choose). Also if you prefer working with TestNet I suggest to use [MetaMask](https://metamask.io/). It has to be in hexadecimal version, so we put **0x** at the beginning (only when you use TestNet, in ganache is right away, so check it carefully).

```
export PRIVATE_KEY=0x...
```

#### Specification for using ganache-cli within deploy file

```bash
# for connecting to ganache-cli
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
chain_id = 1337
my_address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
```

#### Specification for using Rinkeby TestNet within deploy file

Firstly go to [Infura](https://infura.io/) and create account. After that you have to create a new project from which you need to get HTTPProvider. Here you can check [ChainID](https://chainlist.org/) for Rinkeby. Public and private keys are in the Metamask account (remeber to add **0x** at the beginning of the private key in the **.env** file).

```bash
# for connecting to Rinkeby TestNet
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/7abda71ad2fa49b18ca946c72c6b558a"))
chain_id = 4
my_address = "0xD3E4842d2bD11E18E96Ad08D2Fd6264C66A5D52f"
```

#### Installing dependencies

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

#### Available commands for the project

Within Ganache approach firstly open the desktop app in order to spin up the local blockchain (remember to check HTTPProvider address and public/private keys). If you prefer command line, simply type below command. With the **--deterministic** flag you should have same public key as shown before [here](#specification-for-using-ganache-cli-within-deploy-file).

```bash
# Run a local blockchain (always spin up with the exact same private/public keys)
$ ganache-cli --deterministic

# Run the app
$ python .\deploy.py
```

If you want to use Rinkeby set [this](#specification-for-using-rinkeby-testnet-within-deploy-file) configuration and type below command.

```bash
# Run the app
$ python .\deploy.py
```
