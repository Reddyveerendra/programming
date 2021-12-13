#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void main(){
int a[10][10],i,j,r,c;
printf("enter no of rows\n");
scanf("%d",&r);
printf("enter no of columns\n");
scanf("%d",&c);
for(i=0;i<c;i++){
    for(j=0;j<r;j++){
        scanf("%d",&a[i][j]);
    }
    printf("\n");
}
for(i=0;i<c;i++){
    for(j=0;j<r;j++){
        printf("%d\t",a[i][j]);
    }
    printf("\n");
}
for(j=0;j<r;j++){
    for(i=c-1;i>=0;i--){
        printf("%d\t",a[i][j]);
    }
    printf("\n");
}
}