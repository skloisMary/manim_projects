// 非递归方式-用队列实现BFS
void BFS(vector<vector<int>>& G, int begin){
    int n = G[0].size(); //节点数量
    // 初始化，所有节点都未被访问。
    for(int i=0;i<n;i++) visited[i] = false; 
    //无向图G是n*n大小的矩阵
    //节点v和节点w相邻，G[v][w]=G[w][v]=1，否则为0
    Queue<int> Q; // 初始队列
    Q.push(begin); //起始点入队列
    visited[begin]=true; // 标记已访问
    while (!Q.empty())
    {
        int front = Q.front(); // 取对首元素作为新的起始点
        Q.pop(); // 出队列
        for(int w=0;i<n;i++){
            // 节点w未被访问且与top节点相连接
            if(visited[w]&&G[top][w]){
                Q.push(w); // 节点w入队列
                visited[w] = false;// 标记已访问
            }
        }
    }
}