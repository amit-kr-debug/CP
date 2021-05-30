# include<stdio.h>
void
separate(char
str[],char
ipClass)
{
    char
network[12],host[12];

for (int k = 0; k < 12; k++)
network[k] = host[k] = '\0';

if (ipClass == 'A')
{
    int
i = 0,j = 0;

while (str[j] != '.')
    network[i + +] = str[j + +];

i = 0;
j + +;

while (str[j] != '\0')
    host[i + +] = str[j + +];

printf("Network ID is %s\n",network);
printf("Host ID is %s\n",host);
}

else if (ipClass == 'B')
{
int
i = 0,j = 0,dotCount = 0;

while (dotCount < 2)
    {
        network[i + +] = str[j + +];
    if (str[j] == '.')
    dotCount++;
    }

i = 0;
j + +;

while (str[j] != '\0')
    host[i + +] = str[j + +];

printf("Network ID is %s\n",network);
printf("Host ID is %s\n",host);
}

else if (ipClass == 'C')
{

int
i = 0,j = 0,dotCount = 0;

while (dotCount < 3)
    {
        network[i + +] = str[j + +];
    if (str[j] == '.')
    dotCount++;
    }

i = 0;
j + +;

while (str[j] != '\0')
    host[i + +] = str[j + +];

printf("Network ID is %s\n",network);
printf("Host ID is %s\n",host);
}

else
printf("In this Class, IP address is not" " divided into Network and Host ID\n");
}
int
main()
{
    int
a,b,c,d;
printf("Enter the ip address in dot format : ");
scanf("%d.%d.%d.%d", & a, & b, & c, & d);
// printf("%d.%d.%d.%d",a,b,c,d);
if (a > 255 | b > 255 | c > 255 | d > 255)
{
printf("Enter valid IP address!");

}
else {
if (a >= 0 & & a <= 127){
printf("Given IP belongs to Class A\n");
printf("NetId is %d\n",a);
printf("HostId is %d.%d.%d\n",b,c,d);
}
else if (a >= 128 & & a <= 191){
printf("Given IP belongs to Class B\n");
printf("NetId is : %d.%d\n",a,b);
printf("HostId is : %d.%d\n",c,d);

}
else if (a >= 192 & & a <= 223){
printf("Given IP belongs to Class C\n");
printf("NetId is : %d.%d.%d\n",a,b,c);
printf("HostId is : %d\n",d);

}
else if (a >= 224 & & a <= 239){
printf("Given IP belongs to Class D\n");
printf("Multicast adress: %d.%d.%d.%d\n",a,b,c,d);

}
else {
    printf("Enter valid IP address!\n");
}

}
printf("\n");
printf("Program is excuted by 4NI18IS009");
return 0;
}