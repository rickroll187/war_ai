# crypto_monitoring/wallet_tracker.py
from web3 import Web3
import os
RPC = os.getenv("ETH_RPC","http://127.0.0.1:8545")
w3 = Web3(Web3.HTTPProvider(RPC))

def score_wallet(addr):
    try:
        bal = w3.eth.get_balance(addr)
    except Exception as e:
        return {"addr":addr,"score":None,"err":str(e)}
    score = 0
    if bal > w3.toWei(1, "ether"): score += 5
    return {"addr":addr,"balance":bal,"score":score}
