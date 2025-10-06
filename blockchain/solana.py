# blockchain/solana.py
import os
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from solana.publickey import PublicKey

RPC = os.getenv("SOLANA_RPC", "https://api.devnet.solana.com")
client = Client(RPC)

def build_transfer_tx(from_pub: str, to_pub: str, lamports: int):
    tx = Transaction()
    tx.add(transfer(TransferParams(from_pubkey=PublicKey(from_pub), to_pubkey=PublicKey(to_pub), lamports=lamports)))
    return tx
