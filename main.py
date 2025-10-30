ip = input("Please enter the ip you want to convert: ")
ipList = ip.split('.')
nrs = [128 , 64 , 32 , 16 , 8 , 4, 2 , 1] # Lista cu valori binare
binaryIp = []

if len(ipList) != 4:
    print("The ip is invalid!")
    exit()

for octet in ipList:
    nrRemained = int(octet)
    if not 0 <= nrRemained <= 255:
        print("Invalid octet detected!")
        exit()
    binaryNrs = ''
    for nr in nrs:
        abstraction = nrRemained - nr
        if abstraction < 0:
            binaryNrs += '0'
        else:
            binaryNrs += '1'
            nrRemained = abstraction
    binaryIp.append(binaryNrs)

print(*binaryIp , sep='.')