int* buildNext(char* P){ //构造子串P的next表
    size_t m =strlen(P); 
    int j =0; //主串指针
    int* N = new int[m]; //next表
    int t = N[0] = -1; //子串指针
    while (j < m - 1)
    {
        if(j<0 || P[j] == P[t]){ //匹配
            j++;
            t++;
            N[j] = (P[j] == P[t] ? j : N[t]); //改进
        }else{ 
            t = N[t]; //失配
        }
    }
    return N;
}