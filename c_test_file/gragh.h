#pragma once
typedef struct edge {
	/*边界点定义*/
	int loaction; //该节点位于数组中的位置
	int weight;
	struct edge* next;
}edge;
typedef struct ver {
	int data; //顶点存储的信息
	edge* next;//第一个边界点
}ver;