# Working with Web3.py within SimpleStorage contract

## Table of contents

- [General info](#general-info)
- [Learned experience during the project](#learned-experience-during-the-project)
  - [SimpleStorage contract](#simplestorage-contract)
    - [SPDX License](#spdx-license)
    - [Keywords](#keywords)
    - [Visibility Quantifiers](#visibility-quantifiers)
    - [Functions](#functions)
      - [Functions that are view or pure](#functions-that-are-view-or-pure)
    - [Memory](#memory)
    - [EVM](#evm)
  - [Compilation of smart contract](#compilation-of-smart-contract)
  - [Ganache ecosystem](#ganache-ecosystem)
  - [Building a transaction](#building-a-transaction)
  - [Working with deployed contract](#working-with-deployed-contract)
  - [Keeping safe your private keys](#keeping-safe-your-private-keys)
  - [Interacting with the blockchain - call vs transact](#interacting-with-the-blockchain---call-vs-transact)
- [Setup](#setup)
  - [Additional file for environment variable](#additional-file-for-environment-variable)
  - [Specification for using ganache-cli within deploy file](#specification-for-using-ganache-cli-within-deploy-file)
  - [Specification for using Rinkeby TestNet within deploy file](#specification-for-using-rinkeby-testnet-within-deploy-file)
  - [Installing dependencies](#installing-dependencies)
  - [Available commands for the project](#available-commands-for-the-project)

## General info

This project was my first contact with Web3.py. Before that, I played around with Remix IDE and created a SimpleStorage contract. Here I was mainly working with ganache via desktop app, ganache-cli (console version of the desktop app), and TestNet (Rinkeby).

This project was created by [freecodecamp](https://www.freecodecamp.org/) in [tutorial](https://www.youtube.com/watch?v=M576WGiDBdQ&t=27066s). I'm extremely grateful for giving this cost-free opportunity to learn all the insights of Solidity, Blockchain, and Smart Contracts.

At first, I went through this project, created some notes, and fast moved to the more advanced ones. Later I understood, that I should go back and create this documentation in my own words to remember all the necessary basic concepts.

Before that, I always tried to create documentation after the project finished, but I never have put that amount of time as here.

## Learned experience during the project

### SimpleStorage contract

I studied the basic structure of the contract. I wanted to share things that were new for me when entering the Solidity language.

#### SPDX License

- Solidity and the Ethereum community found that trust in a smart contract can be better established if source code is available and in terms of legality and copyright it just makes life a lot easier if you add that license identifier right at the top of your solidity. I chose the MIT license identifier because it’s the most open license out there. It means that anybody can use this code and we don’t care. We put the line below at the top of any Solidity file.

  ```bash
  // SPDX-License-Identifier: MIT
  ```

#### Keywords:

- **contract**
  - Stands for the smart contract, that we're going to create. We can think of this keyword, similarly to class keyword in Java or other Object-Oriented languages.
- **interface**
  - Some contracts don't start with the contract keyword, only the interface keyword. Interfaces don't have full-function implementations.
- **import**
  - Allows us to add additional code from certain Github repositories.
- **mapping**

  - A dictionary-like data structure, with _1 value_ per _key_.

    ```java
    mapping(string => uint256) public nameToFavoriteNumber;
    ```

- **pragma**
  - It's used to enable certain compiler features or checks.
- **struct**

  - A way to define new types in Solidity. They're almost like creating new objects as well.

    ```java
     struct People {
          uint256 favoriteNumber;
          string name;
     }

     People public person = People({
          favoriteNumber: 69,
          name: "Jakub"
      });
    ```

- **uint256 vs int256**
  - Due to the fact of the Ethereum characteristic type **uint256** is crucial. It's an unsigned integer with a minimum value of 0. It's just can not be negative, unlike **int256**. It's an integer of size 256 bits, which gave us 32 bytes.

#### Visibility Quantifiers

Following are various visibility quantifiers for functions/state variables of a contract.

- **external**
  - External functions are not meant to be called by the same contract. It has to be called by an external contract.
  - For state variables, **external** is not possible.
- **public**
  - Public functions/variables can be called by anybody. Variables are a function call to just look at them and return whatever that variable is.
- **internal**
  - Internal functions/variables can only be called by other functions/variables inside of this contract or in its derived contract.
  - The reason that we cannot see this variable in our original contract deployment is that we don't give a state variable a _visibility_. It'll automatically get set to **internal**.
    ```java
    uint256 favoriteNumber; // internal
    uint256 public favoriteNumber; // public
    ```
- **private**
  - Private is the most restrictive as private functions and state variables are only visible for the contract they are defined in and not even by derived contracts.

#### Functions

Functions or methods are self-contained modules, that will execute some task for us.

- _state-changing_ function calls are _transactions_
  - transactions === smart contracts interactions === function calls

On a blockchain whenever you're calling a function or whenever you make some _state change_ to the blockchain, you're also making a transaction. That's why making a function call or deploying a contract costs a little bit of gas.

##### Functions that are view or pure

These two keywords define functions that you don't have to make a transaction on, which means that they are non-state changing functions.

- **view**
  - These function means that we want to read some state of the blockchain, so we're just reading off the blockchain. We're not making a state change then, we don't need to make a transaction.
  - **public** variables automatically, are also **view** functions
- **pure**
  - These are functions, that purely do some type of math.

#### Memory

In Solidity there are two ways to store information:

- **memory**
  - Data will only be stored during the execution of the function or the contract call.
    - **string** is a dynamically-sized byte array (a special type of array, that we can append text to), so because it's technically an object, we have to decide where we want to store it in **memory** or **storage**.
    - **string** is not a value-type!
    - In this case, since we only need parameter _\_name_ during the execution, we can have it be _string_ **memory** _\_name_.
      ```js
      function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
      }
      ```
- **storage**

  - if we hold it here, that means data will persist even after

In short:

- **memory** means, that after execution it deletes this variable.
- **storage** means keep it forever.

#### EVM

- All the solidity code that I wrote and when I interacted with this blockchain was compiled down to the EVM, also known as the Ethereum Virtual Machine. A lot of the blockchains out there today are called EVM compatible and that means all this solidity code that we’re creating can still compile down to EVM and deployed on their blockchain.

### Compilation of smart contract

I needed to write our compiler using Web3 to extract **bytecode** and **ABI** from our SimpleStorage contract to enable EVM to read it.

### Ganache ecosystem

Ganache is a simulated or a fake blockchain, that we can use to deploy our smart contracts. It's something similar to JavaScript VM in remix IDE. It's much faster and easier to test things rather than standard TestNet like Rinkeby.

### Building a transaction

We need to build our transaction, because in this case we'd be deploying a contract, which is going to make a state change.

I've learned that a transaction consists of several things like:

- **building a transaction**

  In web3.py we always have to give at least a couple of parameters.

  ```python
  transaction = SimpleStorage.constructor().buildTransaction(
    {"gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce}
  )
  ```

- **signing a transaction**

  We're signing a transaction using **private keys**. More precisely we're signing a transaction that is deploying a contract to the blockchain.

  ```python
  signed_tx = w3.eth.account.sign_transaction(transaction, private_key=private_key)
  ```

- **sending a transaction**

  We want to send this to the blockchain, so it actually can deploy.

  ```python
  print("Deploying contract...")

  tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
  tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

  print("Deployed!")
  ```

### Working with deployed contract

I studied that whenever we work with a **contract** we always need two things:

- contract address
- contract ABI (application binary interface)

```python
# Working with Contract -> 1. Contract Address | 2. Contract ABI
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
```

### Keeping safe your private keys

It's not so great idea to have plain text on our computer, but still better than hard coding it into our script. For purpose of **private key** safety, it's worth building healthy habits around that concept, even if at this moment we're not working with real money.

Later I'll introduce the safest way to keep your **private key** in your project.

### Interacting with the blockchain - call vs transact

We can interact with functions and variables of the Solidity code within two ways:

1. **call**

   - It doesn't make a state change to the blockchain (nothing on the blockchain would change). We can simply view the values, without making a state change.
   - Two examples from the SimpleStorage contract:

     ```js
      // this will get initialized to 0!
      uint256 favoriteNumber;

      function retrieve() public view returns(uint256) {
          return favoriteNumber;
      }
     ```

     ```java
      struct People {
          uint256 favoriteNumber;
          string name;
      }

      People public person = People({
          favoriteNumber: 69,
          name: "Jakub"
      });
     ```

2. **transact**

   - Make a state change.
   - Two examples from the SimpleStorage contract:

     ```java
       // this will get initialized to 0!
       uint256 favoriteNumber;

       function store(uint256 _favoriteNumber) external {
           favoriteNumber = _favoriteNumber;
       }
     ```

     ```java
      // this will get initialized to 0!
      uint256 favoriteNumber;

      struct People {
          uint256 favoriteNumber;
          string name;
       }

      People public person = People({
          favoriteNumber: 69,
           name: "Jakub"
       });

       People[] public people;
       mapping(string => uint256) public nameToFavoriteNumber;

      function addPerson(string memory _name, uint256 _favoriteNumber) public {
           people.push(People(_favoriteNumber, _name));
          nameToFavoriteNumber[_name] = _favoriteNumber;
       }
     ```

## Setup

There are three different ways of working with this project and each way requires a different approach with certain things like (changing public/private keys, HTTPProvider, and chain_id).

1. Using [Ganache](https://trufflesuite.com/ganache/index.html)
2. Using [ganache-cli](https://www.npmjs.com/package/ganache-cli)
3. Using TestNet (e.g Rinkeby)

Ganache and ganache-cli are quite similar. The difference is that in ganache-cli you're using a command-line instead of the desktop app.

### Additional file for environment variable

You must create a file named **.env** to put there your exported private key (no matter, which way above you choose). It has to be in hexadecimal version, so we put 0x at the beginning (only when you use TestNet, in ganache is right away, so check it carefully).

Below I put the private key from the first wallet, that you're gonna see when you try to [run your local blockchain](#available-commands-for-the-project) within ganache-cli with **--deterministic** flag. So feel free to copy & paste it.

```
export PRIVATE_KEY=0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d
```

**.env** has to be in the **.gitignore** file! Here it's done. Remember to put it in your projects!

### Specification for using ganache-cli within deploy file

Currently the **deploy.py** is set to run on the Rinkeby TestNet, but if you prefer to work with **ganache-cli**, just copy & replace the current code with the below.

```python
# for connecting to ganache-cli
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
chain_id = 1337
my_address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
private_key = os.getenv("PRIVATE_KEY")
```

### Specification for using Rinkeby TestNet within deploy file

1. Go to [Infura](https://infura.io/) and create an account. After that, you have to create a new project from which you need to get HTTPProvider.
2. Here you can check [ChainID](https://chainlist.org/) for Rinkeby.
3. You need to create a crypto wallet, I suggest [MetaMask](https://metamask.io/).

   - Firstly extract **public key**, which is right below your account name in your MetaMask.
   - Secondly, take out **private key**. Open MM, then click on the 3 vertical dots (_Accounts Options_), then _Account details_ and _Export Private Key_.

     Here remember to add **0x** at the beginning of the private key in the **.env** file, because it has to be in the hexadecimal version.

```python
# for connecting to Rinkeby TestNet
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/7abda71ad2fa49b18ca946c72c6b558a"))
chain_id = 4
my_address = "0xD3E4842d2bD11E18E96Ad08D2Fd6264C66A5D52f"
private_key = os.getenv("PRIVATE_KEY")
```

### Installing dependencies

To clone and run this application, you'll need [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/download/) (which comes with [npm](http://npmjs.com)) installed on your computer. In this case, Node.js is only needed for installing a prettier-plugin for Solidity. Furthermore, you'll have to download [Python](https://www.python.org/downloads/) 3.6+ version to install all the required packages via pip. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/pawlovskiii/web3_simple_storage

# Go into the repository
$ cd web3_simple_storage

# Install web3.py
$ pip install web3

# If within cmd occurs any problem, try to add the below flag
$ pip install web3 --user

# Install python-dotenv
$ pip install python-dotenv

# Install solcx
$ pip install py-solc-x

# Install ganache-cli
$ npm install -g ganache-cli

# Install dependencies (not required)
$ npm install
```

### Available commands for the project

Within the Ganache approach firstly open the desktop app to spin up the local blockchain (remember to check HTTPProvider address and public/private keys). If you prefer the command line, simply type the below command. With the **--deterministic** flag you should have the same public key as shown before [here](#specification-for-using-ganache-cli-within-deploy-file).

```bash
# Run a local blockchain (always spin up with the exact same private/public keys)
$ ganache-cli --deterministic

# Run the app
$ python .\deploy.py
```

If you want to use Rinkeby set [this](#specification-for-using-rinkeby-testnet-within-deploy-file) configuration and type the below command.

```bash
# Run the app
$ python .\deploy.py
```
