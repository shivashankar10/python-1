main()
{
    int a=10;
    int *b=&a;
    int **c=&b;
    int ***d=&c;
    printf("a=%\n",a);
    printf("a=\n",b);
    printf("a=\n",a);
}