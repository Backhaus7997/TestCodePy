
import time
from dataclasses import dataclass

def unique_username(prefix="qa"):
    ts = int(time.time() * 1000)
    return f"{prefix}_{ts}"

@dataclass
class User:
    username: str
    password: str
