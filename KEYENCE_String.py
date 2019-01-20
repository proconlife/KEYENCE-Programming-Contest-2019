import re
s = input()
 
r1 = '^.*keyence$'
r2 = '^k.*eyence$'
r3 = '^ke.*yence$'
r4 = '^key.*ence$'
r5 = '^keye.*nce$'
r6 = '^keyen.*ce$'
r7 = '^keyenc.*e$'
r8 = '^keyence.*$'
 
if re.match(r1, s) or re.match(r2, s) or re.match(r3, s) or re.match(r4, s) or re.match(r5, s) or re.match(r6, s) or re.match(r7, s) or re.match(r8, s):
    print("YES")
else :
    print("NO")
