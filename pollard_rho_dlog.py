""" TODO  d) IMPLEMENT FUNCTIONS
def next_s(s,A,alpha,p):

def derive_x(x,p,s):

def derive_y(y,p,s):

def pollard(A,p,alpha):

"""


def next_s(p_s, p_A, p_alpha, p_p):
    if p_s % 3 == 0:
        return (p_s * p_alpha) % p_p
    elif p_s % 3 == 1:
        return (p_A * p_s) % p_p
    else:
        return pow(p_s, 2, p_p)


def derive_x(p_x, p_p, p_s):
    if p_s % 3 == 0:
        return (p_x + 1) % (p_p - 1)
    elif p_s % 3 == 1:
        return p_x
    else:
        return (2 * p_x) % (p_p - 1)


def derive_y(p_y, p_p, p_s):
    if p_s % 3 == 0:
        return p_y
    elif p_s % 3 == 1:
        return (p_y + 1) % (p_p - 1)
    else:
        return (2 * p_y) % (p_p - 1)


# TODO e) IMPLEMENT POLLARD RHO

def pollard(p_A, p_p, p_alpha):
    si = s2i = 1
    xi = yi = x2i = y2i = 0
    for i in range(1, p_p):
        # turtle
        xi = derive_x(xi, p_p, si)
        yi = derive_y(yi, p_p, si)
        si = next_s(si, p_A, p_alpha, p_p)

        # rabbit first step
        x2i = derive_x(x2i, p_p, s2i)
        y2i = derive_y(y2i, p_p, s2i)
        s2i = next_s(s2i, p_A, p_alpha, p_p)

        # hare second step
        x2i = derive_x(x2i, p_p, s2i)
        y2i = derive_y(y2i, p_p, s2i)
        s2i = next_s(s2i, p_A, p_alpha, p_p)

        if si == s2i:
            break
    else:
        return "no collision found...dafuq ?"
    return ((xi - x2i) * pow(y2i - yi, -1, p_p - 1)) % (p_p - 1)


# TODO g) IMPLEMENT FIX

def pollard(p_A, p_p, p_alpha):
    si = s2i = 1
    xi = yi = x2i = y2i = 0
    # search until we find a collision and the result (y2i - yi) is invertible mod p-1
    while True:
        # turtle
        xi = derive_x(xi, p_p, si)
        yi = derive_y(yi, p_p, si)
        si = next_s(si, p_A, p_alpha, p_p)

        # hare first step
        x2i = derive_x(x2i, p_p, s2i)
        y2i = derive_y(y2i, p_p, s2i)
        s2i = next_s(s2i, p_A, p_alpha, p_p)

        # hare second step
        x2i = derive_x(x2i, p_p, s2i)
        y2i = derive_y(y2i, p_p, s2i)
        s2i = next_s(s2i, p_A, p_alpha, p_p)

        # collision found ?
        if si == s2i:
            try:
                # (y2i - yi) is inveritble mod p-1 ?
                return ((xi - x2i) * pow(y2i - yi, -1, p_p - 1)) % (p_p - 1)
            except ValueError:
                # (y2i - yi) is inveritble mod p-1 !!
                #
                # create new pseudo random starting points using properties of generators in zyclic groups.
                # [any kind of PRNG should work as well]
                # and find a new collision
                xi = yi = x2i = y2i = pow(p_alpha, yi, p-1)
                si = s2i = (pow(p_alpha, xi, p_p) * pow(p_A, yi, p_p)) % p_p




A = 28098
p = 46307
alpha = 2

print(" e) secret key:", pollard(A, p, alpha))

A = 4211

print(" g) secret key:", pollard(A, p, alpha))
