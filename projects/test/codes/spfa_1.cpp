/*  SPFA有负权回路返回0,否则返回1并且最短路径保存在dis[]  */ 
/* ------- 邻接表存储 ----------- */ 
struct Edge 
{ 
    int e;  //终点 
    int v;  //边权 
    struct Edge *nxt; 
}; 
struct 
{ 
    struct Edge *head, *last; 
} node[MAXN]; 
/*  松弛函数，成功返回1，否则0  */ 
int relax(int s,int e,int v) 
{ 
    if (dis[s]+v < dis[e]) 
    { 
        dis[e] = dis[s]+v; 
        return 1; 
    } 
    return 0; 
}