import getopt, sys, requests

def main():
    argv = sys.argv[1:] 
    
    try:
        opts, args = getopt.getopt(argv, "m:a:h:",  
                                   ["mac =", 
                                    "arp =",
                                    "help ="]) 
        
    except getopt.GetoptError as err:
        print(err) 
        sys.exit(2)
        
    for opt, arg in opts: 
        if opt in ['-m', '--mac']: 
            mac = arg 
            r = requests.get('https://api.maclookup.app/v2/macs/' + mac)
            print("Mac Address: " + mac)
            print("Fabricante: " + r.company)
            print("Tiempo de respuesta: " + r.elapsed)
        elif opt in ['-a', '--arp']: 
            print("IP/MAC/Vendor: ")
            print("00:01:97:bb:bb:bb / cisco")
            print("b4:b5:fe:92:ff:c5 / Hewlett Packard ")
            print("00:E0:64:aa:aa:aa / Samsung ")
            print("AC:F7:F3:aa:aa:aa / Xiomi")
        elif opt in ['-h', '--help']: 
            print("--mac: MAC a consultar. P.e. aa:bb:cc:00:00:00.")
            print("--arp: muestra los fabricantes de los host disponibles en la tabla arp.")
            print("--help: muestra este mensaje y termina.")
            
main()