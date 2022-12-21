#include <bits/stdc++.h>
using namespace std;
const int inf = 1e7;
int main()
{
    int n, m; // n -> no. of vertex ,m-> no. of edges
    cin >> n >> m;
    vector<int> dist(n + 1, inf);                //
    vector<vector<pair<int, int>>> graph(n + 1); //{v,cost}
    for (int i = 0; i < m; i++)                  // for each edges   [[{},{},...],[{},{},...],[],[]]
    {
        int u, v, w;
        cin >> u >> v >> w; // w (wt betn u,v)
        graph[u].push_back({v, w});
        graph[v].push_back({u, w});
    }
    int source;
    cin >> source;
    dist[source] = 0;
    set<pair<int, int>> s; //{wt,vertex} or {cost,vertex} so we could be able to get less cost causing vertex
    s.insert({0, source});
    while (!s.empty())
    {
        auto x = *(s.begin()); // x={0,source}
        s.erase(x);
        // updating dist values all adjacent Vs of x.second
        for (auto it : graph[x.second]) // g[source]= [{v,cost},{},{},...] ->it={v,cost}
        {

            /*
               *minimisation
               if d(u)+c(u,v)<c(v) then
               d(v)=d(u)+c(u,v)
            */
            /* d[v] > d[source or u] + cost_of_utov */
            if (dist[it.first] > dist[x.second] + it.second)
            {
                s.erase({dist[it.first], it.first});         // {d[v],v} or old {cost,v} // it wont show any error if el is not found
                dist[it.first] = dist[x.second] + it.second; // new cost updated in dist
                s.insert({dist[it.first], it.first});        // also updated in set {wt,v}
            }
        }
    }
    for (int i = 1; i <= n; i++)
    {
        if (dist[i] < inf)
        {
            cout << dist[i] << " ";
        }
        else
        {
            cout << -1 << " ";
        }
    }
}

/*
  a set required for minimum distance from source which will get updated in process
  also provides the minimum distance

  [ v:0 []
    v:1 [{},{},{}]  // |5|->{4,(2)}->{3,(1)} ,{v,wt}
    v:2 [{},{},{}]
    v:3 [{},{},{}]  ]
  //adjacency list of graph

  dist[cost,cost,cost,cost,cost,cost,cost,cost,cost]
        0  , inf,inf ,inf ,inf ,inf ,inf ,inf ,inf

  set = [{wt,vertex},{wt,vertex},{wt,vertex},{wt,vertex}]

  this set helps to choose minimum cost causing vertex( among connected vertex)
  from current source vertex.
*/

/*
    g -> s -> dist
*/

/*
input:
4 4
1 2 24
1 4 20
3 1 3
4 3 12
1
op:
0 24 3 15
*/

/*
tracing

dist[4]=[*,*,*,*]
({0,1})
x={0,1}
()
g[x.s]=[{},{}]
g[x.s]=[{2,24},{4,20},{3,3}]
[0,*,*,*]
dist[2]>dist[1]+20=0+20
dist[2]=20
[0,20,*,*]
({20,2})
dist[4]>dist[1]+24=0+24
dist[4]=24
[0,20,*,4]
({20,2},{24,4})

and vertex 3 will enter with its new distance in the set, then it ends for loop
any adjacent vertex source with min distance will be selected again will be
removed from set as x then all adjacent vertices of x.second will be checked for
minimisation . each time vertex with min distance will be selected,considering
3,(unknown value)
gets selected then all adjacent vertices will enter the set,which we re looking
for a path of min distance upto adjacent vertices of 3 from 1 or source,after all
updation & looping,algo will encounter situations every adjacent vertex has been
minimised then no entry will be done in the set,and one by one all el of set will
be erased and set will be empty while loop ends here. finally dist vector will be
printed out

*/

/*
 [
 {},
 {},
 {},
 ]

 [[],
  [],
  [],
  []]

*/