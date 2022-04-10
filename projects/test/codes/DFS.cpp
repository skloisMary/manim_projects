// 递归实现DFS
// 从结点begin开始深度优先搜索遍历图
void DFS(int begin){
    visited[begin] = true; //标记，已被访问
    for(int w=0;w<G.nums,w++){ // 遍历每个节点
        // 如果节点w和begin相连，且节点w未被访问，
        if(G[v][w]!=0 && !visited[w]){
            DFS(w); // 则递归调用w
        }
    }
}
// 图G为邻接矩形
void DFSTraverse(Graph G)
{
    int n = G.nums; // 节点个数
    // 初始化，所有节点都未被访问。
    for(int i=0;i<n;i++) visited[i] = false; 
	//遍历所有顶点
	for (int i = 0; i < G.nums; i++)
	{
        //如果节点没有被访问，则深入搜索
        if(!visited[i]) DFS(i); 
	}
}