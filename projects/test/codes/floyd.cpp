
void ShortestPath_Dijstra(){
    // arcs: 邻接矩阵
    // n: 顶点个数
    for (int k = 0; k < n; ++k){
        for (int i = 0; i < n; ++i){
            for (int j = 0; j < n; ++j){
                arcs[i][j] = min(arcs[i][j], arcs[i][k] + arcs[k][j]);
            }
        }
    }
}