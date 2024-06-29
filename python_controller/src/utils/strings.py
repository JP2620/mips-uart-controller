from binascii import hexlify


def bytes_to_hex_str(bytes: bytes) -> str:
    return "0x" + hexlify(bytes).decode('ascii').upper()