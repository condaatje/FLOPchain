# FLOPchain

The codebase for Jason Huang and Christian Ondaatje's CS262 final project.

## Overview

Our primary goal was to implement a basic cryptocurrency/blockchain simulation using only the Bitcoin whitepaper as a guideline. This was a fun and challenging exercise, and one we would highly recommend to anyone looking to learn more  about how blockchains work.

Our secondary goal was to see whether we could leverage the mining power in our simulation towards useful computation as a part of the block creation process.
This is an open problem in the crypto space, and we recognized that there would be some techonomic challenges in having our simulated chain represent a
cryptocurrency that would survive in the wild. This informed the discussion section of the project paper, and it is our belief that the collusion problem we present there is unsolvable without homomorphic encryption.

## Technical Specifications

The software implementation of FLOPChain is written in `Python 2.7` and has been tested for MacOS, but should be platform-independent given the installation and testing procedures described in the following section.

Documentation in the form of `pydoc` is provided in the `doc` directory of this repository in addition to the thorough comments in the code. The Bitcoin whitepaper used as a reference for this implementation has also been included.


## Installation & Testing

The implementation makes use of the `pycrypto` module for cryptographic functionality, and may need to be installed by the following terminal command through the `pip` package manager.

```pip install pycrypto```

Tests were also written for the software, and can be run with the following commands.

```python2.7 tests.py```

```python2.7 tests_user.py```

## Simulation

A simulation is provided to demonstrate the performance and behavior of the implementation in live operating conditions. Interested parties may test this for themselves by modifying `simulation.py` as they would like, or just directly running the following command.

```python2.7 simulation.py```
