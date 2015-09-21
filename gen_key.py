import struct

def generate_key(seed):
    v2 = transform(seed | (seed << 8), 1)
    v3 = transform(v2, 2)
    v4 = transform(v3, 3)
    v5 = transform(v4, 4)
    v6 = transform(v5, 5)
    key = struct.pack("IIII", v6, v3, v4, v5)

    return key


def transform(val1, loops):
    val1 = val1 & 0xffffffff
    val2 = (2 * val1) & 0xffffffff

    for i in range(loops):
        val1 = (val1 >> 1) | ((~(val1 ^ ((val1 ^ ((val1 ^ (val1 >> 1)) >> 4)) >> 2)) & 0xffffffff) << 31) & 0xffffffff
        val2 = (2 * val2 | (((~(2 * (val2 ^ (2 * (val2 ^ ((2 * ((val1 ^ 2 * val2) & 0xffffffff)) & 0xffffffff)))))) & 0xffffffff) >> 31) & 0xffffffff) & 0xffffffff

    return val1 ^ val2


if __name__ == "__main__":
    seed = 0x635aef5f

    key = generate_key(seed)
    print "".join(key).encode("hex")
