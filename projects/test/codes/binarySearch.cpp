// 闭区间[low, high]二分查找
int binarySearch(vector<int>& Array, int target){
    int n = Array.size();
    int low = 0, high = n-1, mid = 0; //[low, high]
    while(low <= high){
        mid = low + (high - low) / 2;
        if(Array[mid] == target) return mid; // 查找成功
        else if(Array[mid] > target) high = mid - 1; 
        else if(Array[mid] < target) low = mid + 1;
    }
    return -1; //target 不在Array中
}