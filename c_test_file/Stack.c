/*
 @description: 栈实现，通过使用void*实现模板,获取值时需要使用强制类型转化
 @return : none
*/
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <string.h>
#include "stack.h"
/*
 @description: 栈的初始化
 @param: 需要传入头节点的地址 &(*node)
 @return: none
*/
void stack_initial(node** a) {
	*a = NULL;
}

/*
 @description: 判断栈是否为空
 @param: 栈的头节点
 @return: 若栈为空返回1，否则返回0
*/
int stack_empty(node* a) {
	return (a == NULL);
}

/*
 @description: 向栈中插入元素
 @param: 需要传入头节点的地址 &(*node) 和要插入的元素
 @return: 若插入成功返回1，否则返回0
*/
int stack_insert(node** a, EleType item) {
	node* temp;
	if ((temp = (node*)malloc(sizeof(node))) != NULL) {
		temp->next = *a;
		temp->value = item;
		*a = temp;
		return 1;
	}
	return 0;
}

/*
 @description: 从栈中删除元素并返回其值
 @param: 需要传入头节点的地址 &(*node)
 @return: 若栈为空返回NULL，否则返回栈顶元素的值
*/
EleType stack_delete(node** a) {
	EleType value;
	if (stack_empty(*a))
		return NULL;
	node* temp = *a;
	value = temp->value;
	*a = (*a)->next;
	free(temp);
	return value;
}

/*
 @description: 获取栈顶元素的值
 @param: 栈的头节点 和 用于存储栈顶值的指针
 @return: 若栈为空返回0，否则返回1
*/
int stack_gettop(node* a, EleType* result) {
	if (stack_empty(a))
		return 0;
	*result = a->value;
	return 1;
}


int convert_to_bin(int data) {
	node* stack = (node*)malloc(sizeof(node));
	stack_initial(&stack);
	int remain=0;
	int len = 0, result = 0;
	
	while (data != 0) {
		remain = data % 2;
		stack_insert(&stack, (EleType)remain);
		data = data / 2;
	}
	while (!stack_empty(stack)) {
		remain = (int)stack_delete(&stack);
		result += remain * pow(10, len++);
		printf("%d", remain);
	}
	return result;
}

int compare(char c, char d) {
	if (c == '+' || c == '-') {
		switch (d) {
		case '*':return 0;
		case '/':return 0;
		case '+':return 0;
		case '-':return 0;
		case '(':return 1;
		}
	}

	if (c == '*' || c == '/') {
		switch (d) {
		case '*':return 0;
		case '/':return 0;
		case '+':return 1;
		case '-':return 1;
		case '(':return 1;
		}
		return 1;
	}
	return 1;
}
	
char*  inffix_to_suffix(char* inffix) {
	size_t inffix_len = strlen(inffix);
	char* suffix = (char*)malloc(sizeof(char) * (inffix_len + 1));
	node* stack = (node*)malloc(sizeof(node));
	stack_initial(&stack);
	size_t i,len=0;
	char c;

	EleType temp;

	for (i = 0; i < inffix_len; i++) {
		c = inffix[i];
		if (isdigit(c))
			suffix[len++] = c;
		else if (c == '(')
			stack_insert(&stack, (EleType)c);
		else if (c == ')') {
			while (1) {
				stack_gettop(stack, &temp);
				char k = (char)temp;
				stack_delete(&stack);/*弹出*/
				if (k == '(') 
					break;
				else /*如果弹出的不是(就是运算符开始写入*/
					suffix[len++] = k;
			}
		}
		else {
			while (1) {
				if (stack_empty(stack))
					break;
				stack_gettop(stack, &temp);
				char k = (char)temp;
				if (compare(c, k)) /*c大于当前k才可以进栈*/
					break;
				else {
					suffix[len++] = k;
					stack_delete(&stack);
				}
			}
			stack_insert(&stack, (EleType)c);
		}
	}
	/*遍历结束，依次弹出栈中的计算*/
	while (!stack_empty(stack)) {
		stack_gettop(stack, &temp);
		char k = (char)temp;
		suffix[len++] = k;
		stack_delete(&stack);
	}
	suffix[len++] = '\0';/*截至符*/
	return suffix;
}

float eval_suffix(char* suffix) {
	size_t suffix_len = strlen(suffix);
	node* stack = (node*)malloc(sizeof(node));
	stack_initial(&stack);
	size_t i, len = 0;
	char c;
	EleType temp;
	for (i = 0; i < suffix_len; i++) {
		c = suffix[i];
		if (isdigit(c)) {
			float* k = (float*)malloc(sizeof(float));
			*k =(float)(c - '0');
			stack_insert(&stack,(EleType)k);
		}
			
		else {
			/*读取到运算符开始计算,注意mn的顺序问题， m c n 栈中存储：mn先读出的是n*/
			float m, n, result;
			temp= stack_delete(&stack);
			n = *(float*)temp;
			temp = stack_delete(&stack);
			m = *(float*)temp;

			if (c == '+')
				result=m + n;
			else if (c == '-')
				result = m - n;
			else if (c == '*')
				result = m * n;
			else if (c == '/') {
				if (n == 0) {
					printf("the n is 0");
					exit(0);
				}
				result = m / n;
			}
			float* k = (float*)malloc(sizeof(float));
			*k = result;
			stack_insert(&stack, (EleType)k);	
		}
	}
	stack_gettop(stack,&temp);
	float* a = (float*)temp;
	return *a;
}
//int main() {
//	//convert_to_bin(255);
//
//	char* a = "1+(2-3/4)*5";
//	char* b = inffix_to_suffix(a);
//	printf("%s\n", b);
//	printf("%.4f", eval_suffix(b));
//	
//	//node* stack;
//	//stack_initial(&stack);
//	//int a = 2;
//	//int* pa = &a;
//	//EleType top;
//
//	//stack_insert(&stack, (EleType)2);
//	///*存储指针类型*/
//	///*stack_gettop(stack, &top);
//	//int* pb = (int*)top;
//	//int b = *pb;*/
//	//stack_insert(&stack, (EleType)4);
//	//stack_insert(&stack, (EleType)6);
//	//
//	//if (stack_gettop(stack, &top)) {
//	//	printf("Stack top: %d\n", (int)top);
//	//}
//	//else {
//	//	printf("Stack is empty.\n");
//	//}
//	//while (!stack_empty(stack)) {
//	//	EleType value = stack_delete(&stack);
//	//	printf("Deleted value: %d\n", (int)value);
//	//}
//
//	//return 0;
//}