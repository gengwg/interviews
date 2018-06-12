"""
Write a script that outputs the network interfaces on a system with the corresponding IP addresses in CIDR format.
Bonus points for including IPv6 addresses.
"""
$ ip -o addr | awk '{print $2, $4}'
