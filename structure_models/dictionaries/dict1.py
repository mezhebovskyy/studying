variousinfo = raw_input("Type in some bullshit (like you always do): ")
bla = dict()
for i in range(0, len(variousinfo)):
    if bla.has_key(variousinfo[i]):
        bla[variousinfo[i]] += 1
    else:
        bla[variousinfo[i]] = 1

maxvalue = 0
maxkey = ""
for key, value in bla.iteritems():
    if value > maxvalue:
        maxvalue = value
        maxkey = key
        
print maxvalue, maxkey
print bla