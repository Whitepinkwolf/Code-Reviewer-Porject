#define  ElemType int
#define MaxSize 1000
int n;	/*数组长度*/
		/*定义*/

#include <stdio.h>
void insertarray(ElemType A[], int n,int i, ElemType item) {
	int j;
	if (n == MaxSize || i<1 || i>n + 1)
		printf("errot");
	return;
}

typedef struct node {
	ElemType data;
	struct node* link;
}node,*linklist;

linklist create(int n) {
	linklist p, r=NULL,list = NULL;
	ElemType a;
	int i;
	for (i = 0; i < n; i++) {
		scanf_s("%d", &a);
		p = (linklist)malloc(sizeof(node));
		p->data = a;
		p->link = NULL;
		if (list == NULL)
			list = p;
		else
			r->link = p;
		r = p;
	}
	return list;
}
int length(linklist list) {
	linklist p = list;
	int n = 0;
	while (p != NULL) {
		n++;
		p = p->link;
	}
	return n;
}

/*
 @description:长度为n的线性表A采用顺序存储结构，编写算法找出最小值 2.4 1
 @return : none
*/
int findMin(ElemType a[],int n) {
	int i;
	ElemType result = a[0];
	for (i = 0; i < n; i++) {
		if (a[i] < result)
			result = a[i];
	}
	return result;
}
