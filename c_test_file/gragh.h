#pragma once
typedef struct edge {
	/*�߽�㶨��*/
	int loaction; //�ýڵ�λ�������е�λ��
	int weight;
	struct edge* next;
}edge;
typedef struct ver {
	int data; //����洢����Ϣ
	edge* next;//��һ���߽��
}ver;