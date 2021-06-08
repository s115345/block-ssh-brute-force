import os
import argparse
import fwblock


def parse_arguments():
    parser = argparse.ArgumentParser("Lees het logbestand van de sshd-service uit het bestand ./sshdlog"
                                     "En blokkeer Ip met teveel pogignen")
    # Required arguments
    parser.add_argument("filenames", nargs="*", help="Filenames to analyze")
    # Optional flag arguments
    parser.add_argument("-v", action="store_true", help="Verbose mode", required=False)
    parser.add_argument("-n", action="store_true", help="Test mode", required=False)

    return parser.parse_args()


def get_ip(st):
    """Retourneer IP van de string set van de sshd log file"""
    return st.split('from ')[-1].split(" ")[0]


def get_ip_to_block(filenames, threshold=3):
    """
    :param filenames: lijst van filenames om te analyseren
    :param threshold: limiteer of invalid login pogingen
    :return: list van Ip's die moeten blokeerd worden
    """
    #dictionary waar je IP opslaagd die niet aanvaard zijn
    rejected_ip = {}
    #itereren door bestandsnamen van argumenten
    for filename in filenames:
        #open file in read mode
        with open(filename, "r") as f: 
            for line in f: #iterereren door lines in een file
                if "Invalid user" in line: #indien invalid user in line ga verder
                    ip = get_ip(line) # vind ip-adress van de lijn
                    rejected_ip[ip] = rejected_ip.get(ip, 0) + 1
                    #rejected_ip.get(ip, 0) - get de waarde van de counter door key=ip
                    #als er geen is dan is de default waarde 0
                    #als er al een key is vermeerder het met 1
                    
    return [ip[0] for ip in rejected_ip.items() if ip[1] > threshold]
    #ik heb een dictionary met IPS en een counter gemaakt
    #Bijvoorbeeld : {"192.168.1.1":4 , "88.12.123.23": 2}
    #dan ga ik door deze items itereren van mijn dictionary en alleen de key gebruiken
    #als de vaulue groter is dan de limiet 3(default)

def main():
    blocked_ip = set()
    args = parse_arguments()

    for filename in args.filenames:
        if not os.path.exists(filename):
            raise FileNotFoundError("Verkeerde bestandsnaam in argumenten:", filename)

    ip_list = get_ip_to_block(args.filenames)

    for ip in ip_list:
        if ip not in blocked_ip:
            if args.v:
                print(f"Blocking IP {ip}")
            if not args.n:
                fwblock.block_ip(ip)
            blocked_ip.add(ip)


if __name__ == "__main__":
    main()
