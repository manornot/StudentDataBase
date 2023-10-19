#include <stdio.h>

int main()
{
    int bffr[] = {1,2,3,4,5,6,7,8,9};
    FILE *fp = fopen("text.bin","wb+");
    fwrite(bffr,sizeof(bffr),1,fp);
    fclose(fp);
    fp = fopen("text.bin","rb+");
    int buffer[100];
    fread(buffer, sizeof(bffr), 1, fp);
    int i =0;
    for(i=0;i<sizeof(bffr)/sizeof(int);i++)
    {
        printf("%d",buffer[i]);
    }

}
