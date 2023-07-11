#pragma once

#include<stdlib.h>
#include<stdio.h>
#include"node.h"

node* create_node(EleType value, node* next);
/*创建空node*/
node* create_e_node();
/*
链表操作
*/
node* create(EleType item);
int length(node* linklist);
int length2(node* linklist);
int empty(node* linklist);
node* find(node* linklist, EleType item);
void insert(node** linklist, EleType item, int index);
EleType delete(node** linklist, int index);
void deleteAll(node* linklist);
void reverse(node** linklist);