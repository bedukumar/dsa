for _ in range(int(input())):
  n=int(input())
  height=list(map(int,input().split()))
  lm=height[0]
  rm=height[n-1]
  p1=0
  p2=n-1
  ans=0
  while p1!=p2:
    if lm<rm:
      ans+=lm-height[p1]
      p1+=1
      lm=max(lm,height[p1])
      
    else:
      ans+=rm-height[p2]
      p2-=1
      rm=max(rm,height[p2])
      
  print(ans)
