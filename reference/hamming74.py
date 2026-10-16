"""Documentation companion: even-parity Hamming(7,4), positions left to right.

This is a newly written mathematical reference, not prototype firmware.
Correction assumes no more than one flipped bit per codeword.
"""
import argparse

def bits(value, length):
    if len(value) != length or any(x not in "01" for x in value):
        raise ValueError(f"Expected exactly {length} binary digits")
    return [int(x) for x in value]

def encode(data):
    d1, d2, d3, d4 = bits(data, 4)
    return ''.join(map(str, [d1 ^ d2 ^ d4, d1 ^ d3 ^ d4, d1,
                            d2 ^ d3 ^ d4, d2, d3, d4]))

def syndrome(word):
    r = [0] + bits(word, 7)
    s1 = r[1] ^ r[3] ^ r[5] ^ r[7]
    s2 = r[2] ^ r[3] ^ r[6] ^ r[7]
    s4 = r[4] ^ r[5] ^ r[6] ^ r[7]
    return s1 + 2*s2 + 4*s4

def decode(word):
    corrected = bits(word, 7)
    position = syndrome(word)
    if position:
        corrected[position-1] ^= 1
    code = ''.join(map(str, corrected))
    return ''.join(code[i] for i in (2, 4, 5, 6)), position, code

def self_test():
    clean = flipped = 0
    for n in range(16):
        data = f"{n:04b}"
        code = encode(data)
        assert decode(code) == (data, 0, code)
        clean += 1
        for position in range(1, 8):
            received = list(code)
            received[position-1] = str(1-int(received[position-1]))
            assert decode(''.join(received)) == (data, position, code)
            flipped += 1
    # A two-bit error can mimic a different single-bit error.
    assert decode("1111001")[0] != "1001"
    print(f"PASS: {clean} clean + {flipped} single-bit cases = {clean+flipped} cases")
    print("Two-bit ambiguity confirmed; these are software checks, not hardware tests.")

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--data', default='1001')
    p.add_argument('--flip', type=int, choices=range(1, 8))
    p.add_argument('--self-test', action='store_true')
    a = p.parse_args()
    if a.self_test:
        self_test()
        return
    try:
        code = encode(a.data)
    except ValueError as exc:
        p.error(str(exc))
    received = list(code)
    if a.flip:
        received[a.flip-1] = str(1-int(received[a.flip-1]))
    received = ''.join(received)
    data, position, corrected = decode(received)
    print(f"Input: {a.data} | Transmitted: {code} | Received: {received}")
    print(f"Syndrome: {position:03b} | Assumed error position: {position}")
    print(f"Corrected: {corrected} | Recovered: {data}")
    print("Reference model only; assumes at most one flipped bit.")

if __name__ == '__main__':
    main()
