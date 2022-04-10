class Solution {
public:
    int binarySearch(vector<int>& nums, int target, int lower){
        int n = nums.size();
        int low = 0;
        int high = n - 1;
        int index = n;
        while(low<=high){
            int mid = low + (high - low) / 2;
            // lower为True，寻找leftIdx;第一个等于target的元素的下标
            // lower为False，寻找rightIdx+1；第一个大于target元素的下标
            if(nums[mid] >  target || (lower && nums[mid] >= target)){
                high = mid - 1;
                index = mid; //记录下标
            }else{
                low = mid + 1;
            }
        }
        return index;
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        int n  = nums.size();
        int leftIdx = binarySearch(nums, target, 1); // leftIdx
        int rightIdx = binarySearch(nums, target, 0) - 1; //rightIdx还需要减一
        if(leftIdx<=rightIdx&&rightIdx<n&&nums[leftIdx]==target&&nums[rightIdx]==target){
            return vector<int> {leftIdx, rightIdx}; //返回
        }
        return vector<int>{-1,-1}; // taget不在数组nums中
    }
};