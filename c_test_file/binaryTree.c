#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include"binaryTree.h"
//A(B(c,D),E(F))
/*
 @description: 接受广义表(嵌套括号定义)的输入，输出二叉树
 @return : none
*/
btnode* case7_1() {
	btnode* stack[stack_size], * p=NULL, * t = NULL;
	char cmdc[] = "A(B(D,E(G)),C(F(,H)))@";
	char c;
	int flag=1, top = -1;
	for (size_t i = 0;i<strlen(cmdc);i++){
		/*scanf_s("%c", &c);*/
		c = cmdc[i];
		switch (c)
		{
		case '@':return(t);
		case '(':
			stack[++top] = p; //对于左括号上一个字母进行入栈,栈的top存储的为当前子树根节点
			flag = 1;
			break;
		case ',':
			flag = 2;
			break;
		case ')'://右括号弹出栈，
			top--;
			break;

		default: /*取到字母*/
			p = (btnode*)malloc(sizeof(btnode));
			p->value = c;
			p->left = NULL;
			p->right = NULL;
			if (t == NULL)
				t = p;
			else if(flag==1) {
				stack[top]->left = p;
			}
			else {
				stack[top]->right = p;
			}
		}
	}
}


void preorder(btnode* tree) {
	// 非-递归前序遍历二叉树
	btnode* stack[stack_size], * node;
	int k = -1;
	if (tree == NULL) {
		printf("tree is empty-- \n");
		return;
	}
	else {
		stack[++k] = tree; // 将根节点入栈
		while (k > -1) {
			//出栈
			node = stack[k--];
			printf("%c\n", node->value);
			// 先把右子树放进去，栈是先进去后出，所以下面的左子树先出
			if (node->right != NULL) {
				stack[++k] = node->right;
			}
			if (node->left != NULL) {
				stack[++k] = node->left;
			}
		}
	}
}
/*非递归算法中序遍历*/
void inorder(btnode* tree) {
	if (tree == NULL) {
		printf("tree is empty-- \n");
		return;
	}
	btnode* stack[stack_size],*p=tree;
	int top = -1;
	while (!(p == NULL && top == -1)) {
		//找到当前树最左端元素
		while (p != NULL) {
			stack[++top] = p;
			p = p->left;
		}
		p=stack[top--];//获取当前栈顶，并获取元素
		printf("%c\n", p->value);
		p = p->right;
	}

}
/*非递归的后续遍历：单栈写法*/
void postorder(btnode* tree) {
	if (tree == NULL) {
		printf("tree is empty-- \n");
		return;
	}
	btnode* stack[stack_size];
	int top = -1;
	btnode* p = tree,*r=NULL;
	while (p != NULL || top != -1) {
		//寻找树的最左端
		if(p != NULL) {
			stack[++top] = p;
			p = p->left;
		}
		else {
			p = stack[top];
			if (p->right != NULL && p->right!=r) //当前节点不为空，且没有访问过右边节点
				p = p->right;
			else {
				top--;   //top弹出，注意此时p已经存储了弹出node的信息
				printf("%c\n", p->value);
				r = p;      //记录最近访问过的节点
				p = NULL;  //必须重新赋值,否则最后无法判断主循环结束条件 p != NULL || top != -1
			}
		}
		
	}
}
/*双栈实现，flag会记录当前的节点否被访问*/
void postorder2(btnode* tree) {
	if (tree == NULL) {
		printf("tree is empty-- \n");
		return;
	}
	btnode* node_stack[stack_size],*p=tree;
	int top=-1,flag=0;
	int* flag_stack[stack_size];
	while (p != NULL || top != -1) {
		//遍历左边节点
		while (p != NULL) {
			node_stack[++top] = p;
			flag_stack[top] = 0; //将值置为1表示没有访问
			p = p->left;
		}
		p = node_stack[top];
		//判断是否能够访问右边节点
		flag = flag_stack[top--];
		if (flag == 0) {
			node_stack[++top] = p;
			flag_stack[top] = 1;
			p = p->right;
		}
		else {
			printf("%c\n", p->value);
			p = NULL;
		}
	}
}
void layerorder(btnode* tree) {
/*
 @description: 层次分析法
 @return : none
*/
	if (tree == NULL) {
		printf("tree is empty-- \n");
		return;
	}
	btnode* queue[stack_size],*p=tree;
	int front=-1, rear=0;
	queue[0] = p;
	while (front < rear) {
		p = queue[++front];
		printf("%c\n", p->value);
		//队列需要先进入
		if (p->left != NULL) queue[++rear] = p->left;
		if (p->right != NULL) queue[++rear] = p->right;
	};
}
int similar(btnode* a, btnode* b) {
	/*
 @description: 判断两个树是否相似
 @return : none
*/
	if (a == NULL && b == NULL)
		return 1;
	else {
		if (similar(a->left, b->left) && similar(a->right, b->right))
			return 1;
		else return 0;
	}
}

void sortTree_insert(btnode **ptree,char item) {
	/*
	 @description: 二叉排序树的插入非递归算法
	 @return : none
	*/
	btnode* q = *ptree,*p=*ptree;
	/*创建该节点*/
	p = (btnode*)malloc(sizeof(btnode));
	p->value = item;
	p->left = NULL;
	p->right = NULL;

	if (q == NULL) {
		*ptree = p;
		return;
	}
	else {
		while (1) {
			if (item < q->value) {
				if (q->left != NULL)
					q = q->left;
				else {
					q->left = p;
					break;
				}
			}
			else{
				if(q->right!=NULL)
					q = q->right;
				else {
					q->right = p;
					break;
				}
			}
		}
		
	}
}

void sortTree_insert2(btnode** ptree, char item) {
	/*
	 @description: 二叉排序树的插入递归算法
	 @return : none
	*/
	btnode* q = *ptree, * p = *ptree;
	/*创建该节点*/
	p = (btnode*)malloc(sizeof(btnode));
	p->value = item;
	p->left = NULL;
	p->right = NULL;

	if (q == NULL) {
		*ptree = p;
		return;
	}
	else {
		if (item < q->value) 
			sortTree_insert2(q->left, item);
		else 
			sortTree_insert2(q->right, item);

	}
}
btnode* sortTree_create(char item[], int n) {
	btnode* tree = NULL;
	int i;
	if (n > 0)
		for (i = 0; i < n; i++)
			sortTree_insert(&tree, item[i]);
	return tree;
}
btnode* sortTree_search(btnode* tree, char item) {
	while (tree != NULL) {
		if (item == tree->value)
			return tree;
		else if (item < tree->value)
			tree = tree->left;
		else
			tree = tree->right;
	}
	return NULL;
}
btnode* sortTree_search2(btnode* tree, char item) {
	if (tree == NULL)
		return NULL;
	if (item == tree->value)
		return tree;
	else if (item < tree->value)
		sortTree_search2(tree->left,item);
	else
		sortTree_search2(tree->right, item);
}
//
//int main() {
//	char* a = "45126";
//	btnode* tree=case7_1();
//	tree = sortTree_create(a, strlen(a));
//	printf("前序遍历：\n");
//	preorder(tree);
//	btnode *item=sortTree_search(tree, '1');
//	printf("the find result:%c", item->value);
//
//	/*printf("中序遍历：\n");
//	inorder(tree);
//	printf("后序遍历：\n");
//	postorder(tree);
//	printf("后序遍历：\n");
//	postorder2(tree);
//	printf("层次遍历：\n");
//	layerorder(tree);*/
//
//
//}