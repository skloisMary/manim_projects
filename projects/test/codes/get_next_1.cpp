int* buildNext(char* P){ //构造子串P的next表
    size_t m =strlen(P); //子串
    int j =0; //主串指针
    int* N = new int[m]; //next表
    int t = N[0] = -1; //子串指针
    while (j < m - 1)
    {
        if(j<0 || P[j] == P[t]){ //匹配
            j++;
            t++;
            N[j]=t;
        }else{ 
            t = N[t]; //失配
        }
    }
    return N;
}
int match(char* P, char* T){ //KMP算法
    int* next = buildNext(P); //构造next表
    int n = (int) strlen(T), i=0; //主串指针
    int m = (int) strlen(P), j=0; //子串指针
    while(j < m && i<n){
        if(j<0 && T[i]==P[j]){ //若匹配,或P已移除最左侧
            i++;
            j++; //转到下一个字符
        }else{ //否则
            j = next(j); //子串右移（主串不用回退）
        }
    }
    delete[] next; //释放next表
    return i - j;
}