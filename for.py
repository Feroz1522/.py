y=[5,2,5,2,2]
for v in y:
  o=''
  for z in range(v):
    o +='x' # loop will be repeated itself like o =x,o=xx,o=xxx,till o=xxxxx,then break the loop then print xxxxx and so on..
  print(o)