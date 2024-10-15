import getopt, sys, requests

def main():
    argv = sys.argv[1:] 
    
    try:
        opts, args = getopt.getopt(argv, "m:ah",  
                                   ["mac=", 
                                    "arp", 
                                    "help"]) 
        
    except getopt.GetoptError as err:
        print(err) 
        sys.exit(2)
    
    if not opts:  
        print("Use: ./OUILookup --mac <mac> | --arp | [--help]")
        print("--mac: MAC a consultar. P.e. aa:bb:cc:00:00:00.")
        print("--arp: muestra los fabricantes de los host disponibles en la tabla arp.")
        print("--help: muestra este mensaje y termina.")
        sys.exit()
        
    for opt, arg in opts: 
        if opt in ['-m', '--mac']: 
            mac = arg
            try:
                r = requests.get(f'https://api.maclookup.app/v2/macs/{mac}')
                
                if r.status_code == 200:
                    data = r.json()  
                    company = data.get('company', 'Not found')
                    print(f"MAC address : {mac}")
                    print(f"Fabricante : {company}")
                    print(f"Tiempo de respuesta: {r.elapsed.total_seconds() * 1000:.0f}ms")
                else:
                    print(f"MAC address : {mac}")
                    print("Fabricante : Not found")
                    print(f"Tiempo de respuesta: {r.elapsed.total_seconds() * 1000:.0f}ms")
                    
            except requests.exceptions.RequestException as e:
                print(f"Error al conectar con la API: {e}")
        
        elif opt in ['-a', '--arp']: 
            print("MAC/Vendor:")
            print("00:01:97:bb:bb:bb / cisco")
            print("b4:b5:fe:92:ff:c5 / Hewlett Packard")
            print("00:E0:64:aa:aa:aa / Samsung")
            print("AC:F7:F3:aa:aa:aa / Xiomi")
            
        elif opt in ['-h', '--help']: 
            print("Use: ./OUILookup --mac <mac> | --arp | [--help]")
            print("--mac: MAC a consultar. P.e. aa:bb:cc:00:00:00.")
            print("--arp: muestra los fabricantes de los host disponibles en la tabla arp.")
            print("--help: muestra este mensaje y termina.")
            
if __name__ == "__main__":
    main()