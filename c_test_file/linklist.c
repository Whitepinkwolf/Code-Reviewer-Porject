#include"linklist.h"
#include<stdlib.h>
#include<stdio.h>

#define node_len sizeof(node) 
node* create_node(EleType value, node* next) {
	node* p = (node*)malloc(node_len);
	p->value = value;
	p->next = next;
	return p;
}
/*创建空node*/
node* create_e_node() {
	node* p = (node*)malloc(node_len);
	return p;
}
/*
链表操作
*/
node* create(EleType item) {
	node* p = (node*)malloc(node_len);
	p->next = NULL;
	p->value = item;
	return p;
}

int length(node* linklist) {
	node* p = linklist;
	int length = 0;

	while (p != NULL) {
		length++;
		p = p->next;
	}
	return length;
}
/*
 @description:计算长度的递归算法
 @return : none
*/
int length2(node* linklist) {
	if (linklist == NULL)
		return 0;
	else 
		return length2(linklist->next);
}

int empty(node* linklist) {
	return linklist == NULL;
}

node* find(node * linklist,EleType item) {
	node* p = linklist;
	while (p->value != item && p!=NULL) {
		p = p->next;
	}
	return p;
}
/*
 @description: 在index的位置插入item元素，inde从0开始计算
 @return : none
*/
void insert(node** linklist, EleType item, int index) {
	int i;
	node* r = *linklist;
	if (index<0 || index>length(*linklist))
		return;
	if (index == 0) {
		r = (node*)malloc(node_len);
		r = create_node(item, *linklist);
		*linklist = r;
		return;
	}
	else {
		for (i = 0; i < index-1; i++) {
			r = r->next;
		}
		//此时r指向要插入的位置 
		r->next = create_node(item, r->next);
		return;
	}
	
}
EleType delete(node** linklist, int index) {
	EleType result;
	node* p = *linklist;
	if (index<0 || index>length(*linklist)) {
		printf("the index is illegal");
		return NULL;
	}
	if (index == 0) {
		*linklist = (*linklist)->next;
		result = p->value;
		free(p);
		return result;		
	}
	for (int i = 0; i < index-1; i++) {
		p = p->next;
	}
	//p指向要删除的前一个节点
	node* q = p->next;
	p->next = q->next;
	result = q->value;
	free(q);
	return result;
}
void deleteAll(node* linklist) {
	node* p;
	while (linklist != NULL) {
		p = linklist;
		linklist = linklist->next;
		free(p);
	}
}
void reverse(node** linklist) {
	node* p,*q,*r;
	q = *linklist;
	p = NULL;
	while (q != NULL) {
		// r   p  q  舒徐
		r = p;
		p = q;
		q = q->next;//存储正常情况下p的下一个节点，之后会进行修改导致丢失
		p->next = r; //逆转操作
	}
	*linklist = p;//注意最后r p q=NULL
}
//int main() {
//	
//	int a=0,b=1;
//	int* p = &a;
//	node* linklist = create((EleType)p);
//	p = &b;
//	insert(&linklist, (EleType)p, 1);
//	printf("the length is %d\n",length(linklist));
//	reverse(&linklist);
//	while (!empty(linklist)) {
//		int* q=(int*)delete(&linklist, 0);
//		printf("the delete element is %d\n", *q);
//	}
//	
//	
//}