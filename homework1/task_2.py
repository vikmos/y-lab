import ipaddress


def int32_to_ip(int32: int)->str:
    """Convert int number to IPv4-adress"""
    result = ipaddress.IPv4Address(int32)
    return str(result)

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"

