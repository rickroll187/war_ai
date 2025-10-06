# blockchain/ethereum.py
import os
from web3 import Web3
from typing import Any, Dict

ETH_RPC = os.getenv("ETH_RPC", "http://127.0.0.1:8545")
w3 = Web3(Web3.HTTPProvider(ETH_RPC))

def build_log_tx(contract_abi: Dict, contract_addr: str, account: str, ipfs_cid: str, severity: str, summary: str):
    contract = w3.eth.contract(address=contract_addr, abi=contract_abi)
    nonce = w3.eth.get_transaction_count(account)
    tx = contract.functions.logThreat(ipfs_cid, severity, summary).buildTransaction({
        "from": account,
        "nonce": nonce,
        "gas": 300000,
        "gasPrice": w3.toWei('2', 'gwei')
    })
    return tx
