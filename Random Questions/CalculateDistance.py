res = [1,2,4,5,5,3,2]

print(' '.join(res))



def queen_may_attack(qx, qy, px, py):
    if qx == px or qy == py:
        return True
    elif abs(qx - px) == abs(qy - py):
        return True
    else:
        return False

# Write python function that given an input IPv4 address as a string. Check whether the IPv4 address is valid.

def check_ip(ip):
    octets = ip.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if int(octet) < 0 or int(octet) > 255:
            return False
    return True