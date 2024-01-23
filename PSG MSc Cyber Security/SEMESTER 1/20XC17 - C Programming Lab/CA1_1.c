#include <stdio.h>

int main()
{
    int Number_1, Number_2;
    int Sum_Of_Number1_Divisors = 0, Sum_Of_Number2_Divisors = 0 ;

    printf("ENTER THE TWO NUMBERS : ");
    scanf("%d %d", &Number_1, &Number_2);

    for(int i=1 ; i<=Number_1 ; i++)
    {
        if(Number_1 % i == 0)
            Sum_Of_Number1_Divisors = Sum_Of_Number1_Divisors + i;
    }

    for(int i=1 ; i<=Number_2 ; i++)
    {
        if(Number_2 % i == 0)
            Sum_Of_Number2_Divisors = Sum_Of_Number2_Divisors + i;
    }

    if((Sum_Of_Number1_Divisors/Number_1) == (Sum_Of_Number2_Divisors/Number_2))
        {
            printf("%d and %d are friendly numbers", Number_1, Number_2);
        }
    else
        {
        printf("%d and %d are not friendly numbers", Number_1, Number_2);
        }

    return 0;
}

