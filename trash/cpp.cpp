#include <stdio.h>
int main()
{
    int N, a;
    scanf("%d", &N);
    for (a = 1; a <= N; a++)
    {
        if (a % 2 == 0)
            printf("%d\n", a);
    }

    return 0;
}