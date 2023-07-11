#pragma once
#define EleType void*
typedef struct node {
	EleType value;
	struct node* next;
}node;
#define node_len sizeof(node) 