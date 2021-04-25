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


res = 0
IpCounter=dict(SshOutPut)
K=IpAdress
for key in IpCounter:
    if IpCounter[key] == K:
        res = res + 1
        
        
# IpCounter=dict(IpAdress)
# 
# for i in IpAdress:
#     IpCounter[i] = IpCounter.get(i, 0) + 1
   

    if res>=3:
    
        raise RuntimeError('The Ip has been dedected 3 times already' % ip)
        
    fwblock.block_ip(key)       
        
            

fwblock.block_ip('45.85.90.17')


    