import fwblock

with open('sshdlog', 'r') as f:
    f_contents = f.read()
    print(f_contents)
   
        
    import ipaddress
    
    fwblock.block_ip('51.140.228.73')
    
#     def block_ip(ip):
#         '''
#         This function adds a rule to the firewall to block all traffic from
#         the given IP address.
#         ip: IP address to block traffic from.
#         '''
#         global blocked
#         
#         try:
# 
# 
#             ipaddress.ip_address(ip) # this will fail if an invalid IP address is passed
#         except ValueError:
#                 validip = False
#         if validip:
#                 ipString = str(ip) + ''
#                 
#         if '142.93.141.126' in ipString:
#             blocked =blocked.add(ip)   
# 
#         if ip in blocked:
#                     raise RuntimeError('You\'re making the firewall slow! IP Address %s '
#                     'has already been blocked' % ip)
#                 
#         def print_blocked():
#             print (blocked)
#             f.write("test")
#             f.close()
            
            
                
                
         

            

