// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        int cur = 0;
        int k = 0;
        while(cur < n) {
            k = read4(buf+cur);
            cur += k;
            if(k < 4) break;
        }
        return cur > n ? n:cur;
    }
};