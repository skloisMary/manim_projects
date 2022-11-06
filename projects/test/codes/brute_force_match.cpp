// 主串为T, 子串为P
// 蛮力模式匹配
int match(char* T, char* P){
    size_t n = strlen(T), i=0; //主串长度、当前接受比对字符的位置
    size_t m = strlen(P), j =0;//子串长度、当前接受比对字符的位置
    while(i<n && j<m){ // 从左向右逐个比对字符
        if(T[i] == P[j]){ // 若匹配
            i++;j++; //则转到下一个字符
        }else{
            i -= j -1; j=0; //主串回退, 子串复位
        }
    }
    return i - j; //返回值
}