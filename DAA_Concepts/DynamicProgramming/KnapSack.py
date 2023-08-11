def __init__(self):
  self.t=[[-1]*(1002) for i in range(1002)]
def knapSack(self,W, wt, val, n):
  if W==0 or n==0:
    return 0
  if self.t[W][n]!=-1:
    return self.t[W][n]
  elif wt[n-1]<=W:
    self.t[W][n]=max(val[n-1]+self.knapSack(W-wt[n-1],wt,val,n-1),self.knapSack(W,wt,val,n-1))
    return self.t[W][n]
  self.t[W][n]=self.knapSack(W,wt,val,n-1)
  return self.t[W][n]
