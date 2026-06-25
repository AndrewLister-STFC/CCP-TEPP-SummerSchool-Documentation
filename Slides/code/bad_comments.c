double myfun(int arg1, int *arg2, int *arg3)
{
    double var1 = 0;
    for(int var2 = 0; var2 < arg1; var2++)
    {
        int var3 = arg2[var2] - arg3[var2];
        var1 += var3 * var3 / arg1;
    }
    return sqrt(var1);
}
