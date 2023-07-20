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
// haha
//E:/codeRe/Code-Reviewer-Porject/c_test_file/gragh.h 