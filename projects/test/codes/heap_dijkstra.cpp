struct edge {int to,cost;};
typedef pair<int,int> P; //first是最短距离，second是顶点的编号
int V;//顶点个数
vector<edge> G[MAXV];
int d[MAXV];

void dijkstra(int s){
    //默认对pair.first 的大小进行排序，greater<class>构成一个小顶堆
    priority_queue<P,vector<P>,greater<P> > que;
    //初始化距离
    memset(d,INF,sizeof d);
    d[s] = 0;
    que.push(P(0,s)); //把起点推入队列
    while(!que.empty())
    {
        P p = que.top(); que.pop();
        int v = p.second; //顶点的编号
        if (d[v] < p.first) continue;//d[v]可能经过松弛后变小了，原压入堆中的路径失去价值
        for(int i = 0; i < G[v].size(); i++){//利用最短边进行松弛
            edge e = G[v][i];
            if (d[e.to] > d[v] + e.cost){
                d[e.to] = d[v] + e.cost;
                que.push(P(d[e.to],e.to));
            }
        }
    }
}