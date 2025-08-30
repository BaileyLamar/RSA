from random import randint


def check_a(d, r, n):
    a = randint(1, n - 1)
    a_pow_d = pow(a, d, n)
    if a_pow_d == n - 1:
        return True
    if a_pow_d == 1:
        return True
    for _ in range(1, r):
        a_pow_d = pow(a_pow_d, 2, n)
        if a_pow_d == n - 1:
            return True
        elif a_pow_d == 1:
            return False
    return False


def primality_test(n) -> bool:
    if n % 2 == 0:
        return False
    nm1 = n - 1
    r = 0
    d = 0
    while True:
        if nm1 % 2 == 0:
            nm1 = nm1 // 2
            r += 1
        else:
            d = nm1
            break
    as_checked = 0
    while as_checked <= 129:
        as_checked += 1
        check = check_a(d, r, n)
        if check:
            pass
        elif check is False:
            return False
    return True


def binary_to_decimal(binary_list: list[int]):
    decimal = 0
    for index, i in enumerate(reversed(binary_list)):
        if i == 1:
            decimal += pow(2, index)
    return decimal


def binary_to_decimal_str(binary_str: str) -> int:
    decimal = 0
    for index, i in enumerate(reversed(binary_str)):
        if i == "1":
            decimal += pow(2, index)
    return decimal


def create_prime(num_of_bits):
    while True:
        binary_str = "1"
        for _ in range(num_of_bits - 2):
            binary_str += str(randint(0, 1))
        binary_str += "1"
        binary_list = []
        for bit in reversed(list(binary_str)):
            binary_list.append(int(bit))
        possible_prime = binary_to_decimal(binary_list)
        if primality_test(possible_prime):
            return possible_prime


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def xgcd(a, b):
    if a < b:
        a, b = b, a
    # Initialize the values
    rkm1 = a
    rk = b
    mkm1 = 1
    mk = 0
    nkm1 = 0
    nk = 1
    rkp1 = rkm1 % rk
    c = (rkm1 - rkp1) // rk
    while rkp1 != 0:
        # Redefining new remainder, coefficient, m, n
        rkp1 = rkm1 % rk
        c = (rkm1 - rkp1) // rk
        mkp1 = mkm1 - c * mk
        nkp1 = nkm1 - c * nk
        # Swap out old values
        rkm1 = rk 
        rk = rkp1
        mkm1 = mk
        mk = mkp1
        nkm1 = nk
        nk = nkp1
    return rkm1, mkm1, nkm1


def encrypt(message: str):
    bit_size = 2048
    p = create_prime(bit_size)
    q = create_prime(bit_size)
    if p == q:
        print("p = q")
        exit()
    n = p * q
    phi = (p - 1) * (q - 1)
    if phi > 65537 and gcd(65537, phi) == 1:
        e = 65537
    else:
        while True:
            e = randint(3, phi - 1)
            if gcd(e, phi) == 1:
                break

    _, co_1, co_2 = xgcd(e, phi)
    if co_1 * e % phi == 1:
        d = co_1 % phi
    elif co_2 * e % phi == 1:
        d = co_2 % phi
    else:
        print("ERROR")


    
    cipher = pow(binary_to_decimal_str(message), e, n)
    cipher = bin(cipher)[2:]
    
    private_key = d
    public_key = n
    return cipher, private_key, public_key

def decrypt(cipher: str, private_key: int, public_key: int):
    return bin(pow(binary_to_decimal_str(cipher), private_key, public_key))[2:]
