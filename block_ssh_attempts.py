import fwblock

SshOutPut = []


IpAdress =[]

    
with open('sshdlog', 'r') as f:
    f_contents =f.read()
for line in f_contents:
    if "invalid user" in line: SshOutPut.append(line)
    
        
for line in SshOutPut:
    listLines=line.split(" ")
    ip=listLines[-4]
    IpAdress.append(ip)


IpChecker=set(IpAdress)

for NieuweIp in IpChecker:
    counter=0
    for Iplijst in IpAdress:
        if NieuweIp==Iplijst:
            counter+=1

    if counter>=3:
      raise RuntimeError('The Ip has been dedected 3 times already' % ip)
    fwblock.block_ip(a)       
        
            

fwblock.block_ip('45.85.90.17')


    