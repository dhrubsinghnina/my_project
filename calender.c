#include<stdio.h>
void main()
{
    int d,m,yr,cen,dec,lyr,dw;
    printf("Enter date");
    printf("\nEnter day number:");
    scanf("%d",&d);
    printf("Enter month number number:");
    scanf("%d",&m);
    printf("Enter year :");
    scanf("%d",&yr);
    d=d%7;
    if(yr%4==0 && yr%100!=0 || yr%400==0){
        switch (m)
        {
        case 1:
        m=1;
        break;
        case 2:
        m=4;
        break;
        case 3:
        m=4;
        break;
        case 4:
        m=0;
        break;
        case 5:
        m=2;
        break;
        case 6:
        m=5;
        break;
        case 7:
        m=0;
        break;
        case 8:
        m=3;
        break;
        case 9:
        m=6;
        break;
        case 10:
        m=1;
        break;
        case 11:
        m=4;
        break;
        case 12:
        m=6;
        break;
        default:
            break;
        }  
    }
    else
    {
        switch (m)
        {
        case 1:
        m=0;
        break;
        case 2:
        m=3;
        break;
        case 3:
        m=4;
        break;
        case 4:
        m=0;
        break;
        case 5:
        m=2;
        break;
        case 6:
        m=5;
        break;
        case 7:
        m=0;
        break;
        case 8:
        m=3;
        break;
        case 9:
        m=6;
        break;
        case 10:
        m=1;
        break;
        case 11:
        m=4;
        break;
        case 12:
        m=6;
        break;
        default:
            break;
        }
    }
    cen=yr/100;
    cen=cen%7;

    dec=yr%100;
    lyr=dec/4;
    dec=dec%7;

    dw=d+m+cen+dec+lyr;
    dw=dw%7;
    switch(dw) {
        case 1:
            printf("Entered day of the week is :Sunday\n");
            break;
        case 2:
            printf("Entered day of the week is :Monday\n");
            break;
        case 3:
            printf("Entered day of the week is :Tuesday\n");
            break;
        case 4:
            printf("Entered day of the week is :Wednesday\n");
            break;
        case 5:
            printf("Entered day of the week is :Thursday\n");
            break;
        case 6:
            printf("Entered day of the week is :Friday\n");
            break;
        case 0:
            printf("Entered day of the week is :Saturday\n");
            break;
        default:
            printf("Invalid input! Please enter a number between 1 and 7.\n");
    }
}