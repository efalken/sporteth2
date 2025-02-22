from helperOracle import send_function
import json


def oddsPost():
    with open("odds.json", "r") as f:
        args = json.load(f)
    tx_hash = send_function("oddsPost", args["_probSpread2"], gas=200000)
    return tx_hash


if __name__ == "__main__":
    tx_hash = oddsPost()
    print(f"The transaction hash: {tx_hash.hex()}")
