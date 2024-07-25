import dns.resolver

rawurl = input('请输入来自h-ui的节点URL：')

domain = rawurl.split('@')[1].split(':')[0]
passwd = rawurl.split('://')[1].split('@')[0]
rawport = rawurl.split(':')[2].split('/?')[0]
ports = rawurl.split('mport=')[1].split('#')[0]
note = rawurl.split('#')[1]
cf = dns.resolver.Resolver()
cf.nameservers = ['1.1.1.1','1.0.0.1']

def domain2ip(domain,vtype):
    iplist = []
    ans = cf.resolve(domain, vtype,raise_on_no_answer=False)
    for ip in ans:
        iplist.append(str(ip))
    return iplist

def fixer(iplist,domain,passwd,rawport,ports,note):
    for ip in iplist:
        print('hy2://'+passwd+'@'+ip+':'+rawport+'/?mport='+ports+'&sni='+domain+'#'+note)

v4list = domain2ip(domain,'A')
v6list = domain2ip(domain,'AAAA')
if len(v4list) == 0 and len(v6list) == 0:
    print('无对应ip，请联系技术支持！')
    exit()
print('解析完成，将以下逐行复制入Nekoray即可使用：')
if len(v4list) != 0:
    fixer(v4list,domain,passwd,rawport,ports,note)
if len(v6list) != 0:
    fixer(v6list,domain,passwd,rawport,ports,note)
input('按任意键退出...')