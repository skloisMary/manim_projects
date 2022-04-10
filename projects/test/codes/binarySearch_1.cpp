// 开区间[low, high)二分查找
int binarySearch(vector<int>& Array, int target){
    int n = Array.size();
    int low = 0, high = n, mid = 0; //[low, high)
    while(low < high){
        mid = low + (high - low) / 2;
        if(Array[mid] == target) return mid; // 查找成功
        else if(Array[mid] > target) high = mid;
        else if(Array[mid] < target) low = mid + 1;
    }
    return -1; //target不在Array中
}