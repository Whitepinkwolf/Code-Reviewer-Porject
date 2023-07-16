#include<limits.h>
#define MaxValue INT_MAX
#include <stdio.h>
#include <stdlib.h>
#include "gragh.h"
void graph_create_array(int a[][100], int n, int e) {
	/*
	 @description:�Գ�����洢���ڽӱ�
	 @return : none
	*/
	int i, j, k, weigth;
	for(i=0;i<n;i++)
		for (j = 0; j < n; j++) {
			a[i][j] = MaxValue; /*�����ֵ*/
		}
	for (k = 0; k < e; k++) {
		scanf_s("%d %d %d \n", &i, &j, &weigth);
		a[i][j] = weigth;
		a[j][i] = weigth;
	}
}
void graph_create_link(ver G[],int n,int e,int edata[][3]) {
	/*
	 @description:����洢���ڽӱ�
	 @return : none
	*/
	int i, begin, end,weight;
	edge *p,*q;

	for (i = 0; i < n; i++) {
		G[i].data = i + 1; //�ڵ�洢����Ϣ��������
		G[i].next = NULL;
	}
	for (i = 0; i < e; i++) {
		begin = edata[i][0];
		end = edata[i][1];
		weight= edata[i][2];
		p = (edge*)malloc(sizeof(edge));
		p->loaction = end - 1;
		p->next = NULL;
		p->weight = weight;
		if (!G[begin - 1].next)
			G[begin - 1].next = p;
		else {
			q = G[begin - 1].next;
			while (q->next)  q = q->next;
			q->next = p;
		}
	}
}
void graph_link_print(ver G[],int n) {
	/*
	 @description:��ӡ����洢��ͼ
	 @return : none
	*/
	int i;
	int ver_data;
	edge* p;
	for (i = 0; i < n; i++) {
		ver_data = G[i].data;
		printf("���㣺%d����·�����յ������", ver_data);
		p = G[i].next;
		while (p) {
			printf("--%d", p->loaction + 1);
			p = p->next;
		}
		printf("\n");
	}
}

void visit_ver(ver node) {
	printf("���ʽڵ㣺%d\n", node.data);
}
/*
 @description: ������ȱ���
 @param : GΪ����洢���ڽӱ�vΪ�����Ķ��㣬visited��¼�ڵ������Ϣ
*/
void DFS(ver G[], int v, int visited[]) {
	if (visited[v] == 1)
		return;
	edge* p;
	visit_ver(G[v]);
	visited[v] = 1;
	p = G[v].next;
	while(p) {
		DFS(G, p->loaction, visited);
		p = p->next;
	}
}
void graph_dfs(ver G[], int n) {
	int i;
	int* visits = (int*)calloc(sizeof(int),n);
	//calloc���� �����ڴ沢��ֵΪ0�����������Ϊ   ��С������
	for (i = 0; i < n; i++)
		if (visits[i] == 0)
			DFS(G, i, visits);
}
/*
 @description: �������ʹ�õݹ��㷨
 @return : none
*/
void BFS(ver G[], int v, int visited[]) {
	if (visited[v] == 1)
		return;
	edge* p = G[v].next;
	//ͨ��ջʵ������ �߽ڵ�Ĵ洢
	int queue[100];
	int front = -1, rear = -1,temp;
	//���ʵ�ǰ�ڵ�
	visit_ver(G[v]);
	visited[v] = 1;
	while (p) {
		//���ʱ߽ڵ�
		temp = p->loaction;
		if (visited[temp] == 0) {
			queue[++rear] = temp;
			visit_ver(G[temp]);
			visited[temp] = 1;
		}
		p = p->next;
	}
	//�ݹ����ʣ��ջ
	while (front != rear) {
		BFS(G, queue[++front],visited);
	}
}
/*
 @description:��ʹ�õݹ��㷨
 @return : none
*/
void BFS2(ver G[], int v, int visited[]) {
	edge* p;
	ver node;
	//����vָ��Ķ���,��ʵ��ֻ�г�ʼ�ڵ���Ҫ��ѭ���ⲿ����
	visit_ver(G[v]);
	visited[v] = 1;
	//ͨ��ջʵ������ �߽ڵ�Ĵ洢
	int queue[100];
	int front = -1, rear = -1, temp;

	queue[++rear] = v;
	while (front != rear) {
		//��ȡ��ǰ����(��ǰ�ڵ�һ���Ѿ������ʹ���)
		node = G[queue[++front]];
		//�������ڵ�
		p = node.next;
		while (p != NULL) {
			temp = p->loaction;
			if (visited[temp] == 0) {
				visit_ver(G[temp]); 
				visited[temp] = 1;
				queue[++rear] = temp;//��ջ
			}
			p = p->next;			
		}
	}
}
void graph_bfs(ver G[], int n) {
	char str[50];
	fgets(str);
	int i;
	int* visits = (int*)calloc(sizeof(int), n);
	//calloc���� �����ڴ沢��ֵΪ0�����������Ϊ   ��С������
	for (i = 0; i < n; i++)
		if (visits[i] == 0)
			BFS2(G, i, visits);
}
int main() {
	int edata[][3] = {
		{1,2,1},{1,3,1},{1,4,1},
		{2,1,1},{2,4,1},
		{3,1,1},{3,4,1},{3,5,1},
		{4,1,1},{4,2,1},{4,3,1},{4,5,1},
		{5,3,1},{5,4,1},
		{6,7,1},{6,9,1},
		{7,6,1},{7,8,1},
		{8,7,1},{8,9,1},
		{9,6,1},{9,8,1},
	};
	ver G[9];
	graph_create_link(G, 9, 22,edata);
	graph_link_print(G, 9);
	printf("---------DFS\n");
	graph_dfs(G, 9);
	printf("---------BFS\n");
	graph_bfs(G, 9);
}
//E:/codeRe/Code-Reviewer-Porject/c_test_file/graph.c 