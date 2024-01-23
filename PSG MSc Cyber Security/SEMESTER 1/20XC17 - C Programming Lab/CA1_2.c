#include<stdio.h>
void main()
{
    int No_Of_Users, Salary, i;
    float Tax;
    char Marital_Status;

    printf("Enter Number of Users : ");
    scanf("%d", &No_Of_Users);

    for(i=1 ; i<=No_Of_Users ; i++)
    {
        printf("Enter Martial Status S / M : ");
        scanf(" %c", &Marital_Status);
        printf("Enter Gross Salary : ");
        scanf("%d", &Salary);

        if(Marital_Status == 'S')
            Salary = Salary - 4000;
        else
            Salary = Salary - 7000;


        if(Salary >= 1000 && Salary <= 15000)
        {
            Tax = Salary*0.15;
            printf("Federal Tax : %f \n\n", Tax);
        }

        else if(Salary >= 15001 && Salary <= 40000)
        {
            Tax = (Salary*0.25 + 2250);
            printf("Federal Tax : %f \n\n", Tax);

        }
        else if(Salary > 40000)
        {
            Tax = (Salary*0.35 + 8460);
            printf("Federal Tax : %f \n\n", Tax);
        }

    }

}
