# Note

## max和max_element

max(a,b)，返回a,b两者之间的较大值  
max\_element(r, r+6),返回数组r中\[0, 6)之间的最大值的**迭代器**，  

```c++
#include <algorithm>
using namespace std;
int main(void)
{
    int a[6] = {5, 3, 2, 6, 1, 4};
    int b = a[0];
    int c = a[1];
    cout<<max(b, c)<<" "<<min(b,c)<<endl; //输出为5 3
    cout<<max_element(a, a+6) - a<<endl;// 输出为3
    cout<<*max_element(a, a+6)<<endl;//输出为 6
    cout<<min_element(a, a+6) - a<<endl;// 输出为4
    cout<<*min_element(a, a+6)<<endl; //输出为1
    return 0;
}

```
