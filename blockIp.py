


with open('sshdlog', 'r') as f:
    f_contents = f.read()
    print(f_contents)
    
import ipaddress

def block_ip(ip):
    '''
    This function adds a rule to the firewall to block all traffic from
    the given IP address.
    ip: IP address to block traffic from.
    '''
    global blocked

def isValid(ip):
    ip = ip.split(".")
    
    for number in ip:
        if not number.isnumeric() or int(number)> 255:
            return False
    return ipaddress.ip_address(ip)  
    
# 
# while True:
#     try:
#         
#         ipaddress.ip_address(ip) # this will fail if an invalid IP address is passed
#         break
#     except ValueError:
#         continue
      
    
    

    if ip in blocked:
        raise RuntimeError('You\'re making the firewall slow! IP Address %s '
                'has already been blocked' % ip)

    blocked.add(ip)