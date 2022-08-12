from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())
    print(simple_storage.address)


def main():
    read_contract()
