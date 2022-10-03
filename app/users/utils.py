from _pysha3 import keccak_256
from ethereum.utils import ecrecover_to_pub


def sig_to_vrs(sig):
    r = int(sig[2:66], 16)
    s = int(sig[66:130], 16)
    v = int(sig[130:], 16)
    return v, r, s


def hash_personal_message(msg):
    padded = '\x19Ethereum Signed Message:\n' + str(len(msg)) + msg
    return keccak_256(bytes(padded, 'utf8')).digest()


def recover_to_addr(msg, sig):
    msg_hash = hash_personal_message(msg)
    vrs = sig_to_vrs(sig)
    return '0x' + keccak_256(ecrecover_to_pub(msg_hash, *vrs)).hexdigest()[24:]
