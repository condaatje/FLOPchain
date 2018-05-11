# FLOPchain

The codebase for Jason Huang and Christian Ondaatje's CS262 final project.

## Overview

Our primary goal was to implement a basic cryptocurrency/blockchain simulation
using only the Bitcoin whitepaper as a guideline. This was a fun and challenging
exercise, and one we would highly reccommend to anyone looking to learn more 
about how blockchains work.

Our secondary goal was to see whether we could leverage the mining power in our
simulation towards useful computation as a part of the block creation process.
This is an open problem in the crypto space, and we recognized that there would
be some techonomic challenges in having our simulated chain represent a 
cryptocurrency that would survive in the wild. This informed the discussion
section of the project paper, and it is our belief that the collusion problem
we present there is unsolveable without homomorphic encryption.


## Installation & Testing

```pip install pycrypto```

```python tests.py```

```python tests_user.py```

## Simulation

```python simulation.py```

