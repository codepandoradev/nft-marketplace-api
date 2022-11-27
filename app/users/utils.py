import struct

import coincurve
from Crypto.Hash import keccak

ALL_BYTES = tuple(struct.pack('B', i) for i in range(256))


# noinspection SpellCheckingInspection
def zpad(x, l):  # noqa: E741
    """Left zero pad value `x` at least to length `l`.

    >>> zpad('', 1)
    '\x00'
    >>> zpad('\xca\xfe', 4)
    '\x00\x00\xca\xfe'
    >>> zpad('\xff', 1)
    '\xff'
    >>> zpad('\xca\xfe', 2)
    '\xca\xfe'
    """
    return b"\x00" * max(0, l - len(x)) + x


def int_to_32bytearray(i):
    o = [0] * 32
    for x in range(32):
        o[31 - x] = i & 0xFF
        i >>= 8
    return o


# noinspection SpellCheckingInspection
def ecrecover_to_pub(rawhash, v, r, s):
    # noinspection PyBroadException
    try:
        pk = coincurve.PublicKey.from_signature_and_message(
            zpad(bytes(int_to_32bytearray(r)), 32)
            + zpad(bytes(int_to_32bytearray(s)), 32)
            + ALL_BYTES[v - 27],
            rawhash,
            hasher=None,
        )
        pub = pk.format(compressed=False)[1:]
    except Exception:
        pub = b"\x00" * 64
    assert len(pub) == 64
    return pub


def sig_to_vrs(sig):
    r = int(sig[2:66], 16)
    s = int(sig[66:130], 16)
    v = int(sig[130:], 16)
    return v, r, s


def hash_personal_message(msg):
    padded = "\x19Ethereum Signed Message:\n" + str(len(msg)) + msg
    return keccak.new(digest_bits=256, data=bytes(padded, 'utf8')).digest()


def recover_to_addr(msg, sig):
    msg_hash = hash_personal_message(msg)
    vrs = sig_to_vrs(sig)
    return (
        '0x'
        + keccak.new(
            digest_bits=256, data=ecrecover_to_pub(msg_hash, *vrs)
        ).hexdigest()[24:]
    )
