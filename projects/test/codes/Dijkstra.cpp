void ShortestPath_Dijstra()
{
    // arcs: 邻接矩阵
    // D: 保存最短路径长度
    // final: 若final[i] = 1则说明 顶点vi已在集合S中
    // n: 顶点个数
    // v0: 源点
    // MAX: 设置的最大值
    for (int v = 0; v < n; v++) //循环 初始化
    {
        final[v] = 0; D[v] = arcs[v0][v];
    }
    D[v0] = 0; final[v0]=1; //初始化 v0顶点属于集合S
    //开始主循环 每次求得v0到某个顶点v的最短路径 并加v到集合S中
    for (int i = 1; i < n; i++)
    {
        int min = MAX;
        for (int w = 0; w < n; w++)
        {
            //我认为的核心过程--选点
            if (!final[w]) //如果w顶点在V-S中
            {
                    //这个过程最终选出的点 应该是选出当前V-S中与S有关联边
                    //且权值最小的顶点 书上描述为 当前离V0最近的点
                    if (D[w] < min) {v = w; min = D[w];}
            }
        }
        final[v] = 1; //选出该点后加入到合集S中
        for (int w = 0; w < n; w++)//更新当前最短路径和距离
        {
            /*在此循环中 v为当前刚选入集合S中的点
            则以点V为中间点 考察 d0v+dvw 是否小于 D[w] 如果小于 则更新
            比如加进点 3 则若要考察 D[5] 是否要更新 就 判断 d(v0-v3) + d(v3-v5) 的和是否小于D[5]
            */
            if (!final[w] && (min+arcs[v][w]<D[w]))
            {
                    D[w] = min + arcs[v][w];
            }
        }
    }
}
