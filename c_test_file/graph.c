#include<limits.h>
#define MaxValue INT_MAX
#include <stdio.h>
#include <stdlib.h>
#include "gragh.h"
void graph_create_array(int a[][100], int n, int e) {
	/*
	 @description:对称数组存储的邻接表
	 @return : none
	*/
	int i, j, k, weigth;
	for(i=0;i<n;i++)
		for (j = 0; j < n; j++) {
			a[i][j] = MaxValue; /*赋最大值*/
		}
	for (k = 0; k < e; k++) {
		scanf_s("%d %d %d \n", &i, &j, &weigth);
		a[i][j] = weigth;
		a[j][i] = weigth;
	}
}
void graph_create_link(ver G[],int n,int e,int edata[][3]) {
	/*
	 @description:链表存储的邻接表
	 @return : none
	*/
	int i, begin, end,weight;
	edge *p,*q;

	for (i = 0; i < n; i++) {
		G[i].data = i + 1; //节点存储的信息就是索引
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
	 @description:打印链表存储的图
	 @return : none
	*/
	int i;
	int ver_data;
	edge* p;
	for (i = 0; i < n; i++) {
		ver_data = G[i].data;
		printf("顶点：%d，其路径的终点包括：", ver_data);
		p = G[i].next;
		while (p) {
			printf("--%d", p->loaction + 1);
			p = p->next;
		}
		printf("\n");
	}
}

void visit_ver(ver node) {
	printf("访问节点：%d\n", node.data);
}
/*
 @description: 深度优先遍历
 @param : G为链表存储的邻接表，v为遍历的顶点，visited记录节点访问信息
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
	//calloc函数 分配内存并赋值为0，此外其参数为   大小，数量
	for (i = 0; i < n; i++)
		if (visits[i] == 0)
			DFS(G, i, visits);
}
/*
 @description: 广度优先使用递归算法
 @return : none
*/
void BFS(ver G[], int v, int visited[]) {
	if (visited[v] == 1)
		return;
	edge* p = G[v].next;
	//通过栈实现所有 边节点的存储
	int queue[100];
	int front = -1, rear = -1,temp;
	//访问当前节点
	visit_ver(G[v]);
	visited[v] = 1;
	while (p) {
		//访问边节点
		temp = p->loaction;
		if (visited[temp] == 0) {
			queue[++rear] = temp;
			visit_ver(G[temp]);
			visited[temp] = 1;
		}
		p = p->next;
	}
	//递归调用剩余栈
	while (front != rear) {
		BFS(G, queue[++front],visited);
	}
}
/*
 @description:不使用递归算法
 @return : none
*/
void BFS2(ver G[], int v, int visited[]) {
	edge* p;
	ver node;
	//访问v指向的顶点,事实上只有初始节点需要在循环外部访问
	visit_ver(G[v]);
	visited[v] = 1;
	//通过栈实现所有 边节点的存储
	int queue[100];
	int front = -1, rear = -1, temp;

	queue[++rear] = v;
	while (front != rear) {
		//获取当前顶点(当前节点一定已经被访问过了)
		node = G[queue[++front]];
		//访问链节点
		p = node.next;
		while (p != NULL) {
			temp = p->loaction;
			if (visited[temp] == 0) {
				visit_ver(G[temp]); 
				visited[temp] = 1;
				queue[++rear] = temp;//进栈
			}
			p = p->next;			
		}
	}
}
void graph_bfs(ver G[], int n) {
	int i;
	int* visits = (int*)calloc(sizeof(int), n);
	//calloc函数 分配内存并赋值为0，此外其参数为   大小，数量
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