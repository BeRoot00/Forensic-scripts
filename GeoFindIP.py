import dpkt
import socket
import pygeoip
import optparse

gi = pygeoip.GeoIP('GeoLiteCity.dat')

def locate(ip):
    try:
        rec = gi.record_by_name(ip)
        city = rec['city']
        country = rec['country_code3']
        if city != '':
            location = city + ', ' + country
        else:
            location = country
        return location
    except:
        # address not in the GeoLiteCity database or private IP address
        return "the address is unregistered"

def showPcap(pcapFile):
    for (ts, buf) in pcapFile:
        try:
            ethernet = dpkt.ethernet.Ethernet(buf)
            ip = ethernet.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)

            print("[+] Source: " + src + ' ----> Dst: ' + dst)
            print("[+] Source: " + locate(src) + ' ----> Dst: ' + locate(dst))
        except:
            print("there is a problem")

def run():
    parser = optparse.OptionParser()
    parser.add_option('-p', dest='pcapFile', type='string', help="specify the pcap file")
    (options, args) = parser.parse_args()
    if options.pcapFile is None:
        print("Usage: python3 GeoFindIP.py -p <pcap file>")
        exit(0)
    pcapFile = options.pcapFile
    with open(pcapFile, 'rb') as f:
        ReadPcap = dpkt.pcap.Reader(f)
        showPcap(ReadPcap)

if __name__ == '__main__':
    run()