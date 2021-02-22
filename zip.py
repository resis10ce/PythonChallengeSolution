s="90052"
while(s.isnumeric()):
 with open("channel/"+s+".txt") as fp:
 	rec=fp.read()
 	print(rec)
 	res=rec.split(" ")
 	print(res[-1])
 	s=res[-1]
