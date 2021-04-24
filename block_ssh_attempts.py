import fwblock

def readLogfiles():
    
    with open('sshdlog', 'r') as f:
        f_contents = f.read()
        print(f_contents)
        return f_contents
# als je functie wilt sluiten moet je minder whitespace gebruiken
def readLinesWithInvalid():
    SshOutput = list((""))
    for InvalidLines in f_contents():  #voor elke lijn in de logfile
        if "invalid user" in InvalidLines: SshOutput.append(InvalidLines) #als invalid user word gevonden in de lijn => in SshOutput list insteken
        return SshOutput

def readInvalidIpAdresses():
   
    InvalidUser = list((""))
    for lines in SshOutput: #lines doorlopen in variable SshOutput => Invalid Lines
        split_elements=lines.split("")#splitten in elementen
        ip=split_elements[-4]#van "invalid" element naar ip element gaan
        InvalidUser.append(ip)#Ip element toevoegen aan InvalidUser list
        return InvalidUser
        
def InvalidIpCount():

    Counter =list((""))#list aanmaken voor ip te tellen
    Counter = SshOutput.count("Invalid")#element invalid vinden in SshOutput via .count
    if Counter == 3: 
        fwblock.block_ip(InvalidUser)#ip blokkeren
        print(InvalidUser + " Ip has been found 3 times or more, Ip has been blocked")
        
                
        


    
    

    