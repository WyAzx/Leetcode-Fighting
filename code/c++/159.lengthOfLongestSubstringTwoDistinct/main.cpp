#include <unordered_map>
#include <string>
#include <iostream>

using namespace std;
class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        unordered_map<char, int> indices;
        int l = 0;
        int k = 0;
        int maxl = 0;
        for(int r = 0; r < s.size(); r++){
            k += indices.count(s[r]) == 0 || indices[s[r]] < l;
            if(k > 2){
                while(indices[s[l]] > l) ++l;
                ++l;
                --k;
            }
            indices[s[r]] = r;
            maxl = max(maxl, r-l+1);
        }
        return maxl;
    }
};

int main(int argc, char const *argv[])
{
    cout << Solution().lengthOfLongestSubstringTwoDistinct("eceba");
    return 0;
}
