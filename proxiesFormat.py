#!/usr/bin/python3

def readProxies(filename="ProxyList.txt"):
	print("[+] Reading proxies...")
	proxies = ""
	with open(filename) as file:
		for line in file:
			proxies += "socks5 " + line
		proxies = proxies.replace(":", " ")
		return proxies

def writeProxyFile(proxies, filename="proxy_proxychains_format.txt"):
	print(f"[+] Writing proxies to {filename}...")
	with open(filename, "w") as file:
		file.write(proxies)
		file.close()
def main():
	ProxyListFile = input("[+] Enter the path of your proxy file : ")
	ProxyFormattedList = readProxies(ProxyListFile)
	writeProxyFile(ProxyFormattedList)
	print("[+] Done ! Copy the output in your proxychains.conf file and you're ready to go.")
main()
