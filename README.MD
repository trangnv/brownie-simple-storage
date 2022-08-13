1. [Original repo](https://github.com/PatrickAlphaC/brownie_simple_storage)

2. Notes

- To use with Brownie's encrypted command line (MOST SECURE):
  - Add account from terminal, indexed 0: `brownie accounts new 0`
  - To load account 0 from script: `account = accounts.load("0")`
- [Solidity view function](https://docs.soliditylang.org/en/v0.8.16/contracts.html#view-functions)
  - the `retrieve` function if not declared as `view`, contract still get compiled
  - but error when deployed