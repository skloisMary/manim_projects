int n; //顶点个数
int vst[MAXN], cnt[MAXN]; int Q[MAXN*MAXN]; //队列
int SPFA(int s0) 
{ 
    int i, p, q; struct Edge *pp; 
    memset(vst, 0, sizeof(vst)); //初始化各顶点都未被访问
    memset(cnt, 0, sizeof(cnt)); //初始化顶点入队列的次数
    for (i=0; i<=n; i++) 
        dis[i] = INF; 
    dis[s0] = 0; 
    Q[0] = s0; p = 0; q = 1; //p是队列的起始index, q是队列的最后index
    vst[s0] = 1; cnt[s0]++; 
    while (p < q) // 队列不为空
    { 
        pp = node[Q[p]].head; 
        while (pp) 
        { 
            if (relax(Q[p], pp->e, pp->v) && !vst[pp->e]) 
            { 
                Q[q++] = pp->e; //入队列且队列长度加1
                vst[pp->e] = 1; // 已被访问
                cnt[pp->e]++; // 记录此顶点被访问的次数
                if (cnt[pp->e] > n) //有负权回路 
                    return 0; 
            } 
            pp = pp->nxt; 
        } 
        vst[Q[p]] = 0; // 将此顶点重新设为未被访问状态
        p++; //取下一个元素
    } 
    return 1; 
} 