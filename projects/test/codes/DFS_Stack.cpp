// 非递归方式-用栈实现DFS
void DFS(vector<vector<int>>& G, int begin){
    int n = G[0].size(); //节点数量
    // 初始化，所有节点都未被访问。
    for(int i=0;i<n;i++) visited[i] = false; 
    //无向图G是n*n大小的矩阵
    //节点v和节点w相邻，G[v][w]=G[w][v]=1，否则为0
    Stack<int> S; // 初始栈
    S.push_back(begin); //起始点入栈
    visited[begin]=true; // 标记已访问
    while (!S.empty())
    {
        int top = S.top(); // 取栈顶节点，作为新的起始点
        S.pop_back(); // 弹出栈
        for(int w=0;i<n;i++){
            // 节点w未被访问且与top节点相连接
            if(visited[w]&&G[top][w]){
                S.push_back(w); // 节点w入栈
                visited[w] = false;// 标记已访问
            }
        }
    }
}