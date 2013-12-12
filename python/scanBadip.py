#!/usr/bin/python

all_badip=[]

txt = open('/home/badip.txt')
for line in txt.readlines():
	line = str(line.split()[0])
	
	all_badip.append(line)

lastip=all_badip[-1]
lastip = lastip[0:-2]


def writeTxt(content):
    output = open('/home/a.txt','a')
    output.write('%s \n' % content)
    output.close()

data = {}
def domainIP(email,domain,ipres):
#	print ipres	
	ipress = ipres.split('.')
	ipress = ipress[0]+'.'+ipress[1]+'.'+ipress[2]
	
	if ipres in all_badip or ipress ==lastip:
		#writeTxt('%s %s  %s '% (email,domain,ipres))
		if data.has_key(email):
			data[email] = data[email] +' ' +domain
		else:
			data[email] = domain
#	else:
#		if ipress == lastip:
#			writeTxt('%s %s  %s '% (email,domain,ipres))
txt=open('/home/ma.txt')
for line in txt.readlines():
	line = line.split()
	email = line[0]
	domain = line[1]
	ipres = line[3]
	domainIP(email,domain,ipres)
#writeTxt(data)
for k,v in data.items():
	writeTxt('%s %s' %(k,v))
