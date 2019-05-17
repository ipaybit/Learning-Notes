//DLinkList.c
#include <stdlib.h>  
#include <string.h>  
#include <stdio.h>  
#include "DLinkList.h"
 
//定义双向链表的头结点 双向链表头结点：表示链表中第一个节点,包含指向第一个数据元素的指针以及链表自身的一些信息
//这样能把所有结点串起来
typedef struct _tag_DLinkList
{
	DLinkListNode   header;  //要有个头指针---指向头结点的指针
	DLinkListNode  *slider;//在双向链表中可以定义一个“当前指针”，这个指针通常称为游标，可以通过游标来遍历链表中所有元素
	int             length;//链表的长度
}TDLinkList;
//创建并且返回一个空的双向链表
DLinkList* DLinkList_Create()
{
	//1 申请动态内存空间
	TDLinkList *tmp = (TDLinkList *)malloc(sizeof(TDLinkList));
	if (NULL == tmp)
	{
		printf("func err malloc: \n");
		return NULL;
	}
	//2 让开辟的内存 完成链式线性表初始化  
	memset(tmp, 0, sizeof(TDLinkList));
	//3 链表的初始化
	tmp->header.next = NULL;
	tmp->header.pre = NULL;
	tmp->slider = NULL;
	tmp->length = 0;
	return tmp;
}
 
//销毁一个双向链表list 
//由于数据元素节点的生命周期不是由链表算法管理的，所以只需要销毁申请的头节点元素即可
void DLinkList_Destroy(DLinkList* list)
{
	//1 缓存下来 进行操作
	TDLinkList *tmp = NULL;
	tmp = (TDLinkList *)list;
	if (NULL == list)
	{
		printf("func err DLinkList_Destroy()\n");
	}
	//2 释放头结点空间 
	if (tmp != NULL)
	{
		free(tmp);
	}
}
 
 
//将一个双向链表list中的所有元素清空, 双向链表回到创建时的初始状态  
void DLinkList_Clear(DLinkList* list)
{
	//1 缓存下来 进行操作
	TDLinkList *tmp = NULL;
	tmp = (TDLinkList *)list;
	if (NULL == list)
	{
		printf("func err DLinkList_Clear()\n");
	}
	//2 清空链表
	tmp->header.next = NULL;
	tmp->header.pre = NULL;
	tmp->slider = NULL;
	tmp->length = 0;
}
 
 
//返回一个双向链表list中的元素个数
int DLinkList_Length(DLinkList* list)
{
	int ret = 0;
	//1 缓存下来 进行操作
	TDLinkList *tmp = NULL;
	tmp = (TDLinkList *)list;
	if (NULL == list)
	{
		ret = -1;
		printf("func err DLinkList_Length():%d\n", ret);
		return ret;
	}
	ret = tmp->length;
	return ret;
}
 
 
//向一个双向链表list的pos位置处插入元素
int DLinkList_Insert(DLinkList* list, DLinkListNode* node, int pos)
{
	int ret = 0;
	//1 缓存下来 进行操作
	TDLinkList *tmp = NULL;
	tmp = (TDLinkList *)list;
	//辅助指针 用来遍历当前指针位置
	DLinkListNode *pCur = NULL;
	//辅助指针 用来缓存当前指针下移位置
	DLinkListNode *pNext = NULL;
	if (NULL == list || NULL == node || pos < 0)
	{
		ret = -1;
		printf("func err (NULL == list || NULL == node || pos < 0):%d\n", ret);
		return ret;
	}
	//注意：容错修正,假如链表当前长度为5,你插入pos位置是10,这个时候可以做容错修正,直接修正为尾插法  
	if (pos > tmp->length)
	{
		pos = tmp->length;
	}
	//1 当前指针 初始化 指向 头结点
	pCur = &(tmp->header);
	//2 进行遍历 找到插入位置
	for (int i = 0; i < pos; i++)
	{
		pCur = pCur->next;
	}
	//3 进行插入操作
	//进行缓存pCur next域
	pNext = pCur->next;
	//插入操作
	pCur->next = node;//1
	node->next = pNext;//2
 
	if (pNext != NULL)
	{
		pNext->pre = node;//3 若是尾插法,就不需要这部操作
	}
	node->pre = NULL;//若是头插法,需要这部操作,如图1  4
	if (pCur !=(DLinkListNode *)tmp)//若不是头插法,普通插入如图2 3情况 
	{
		node->pre = pCur;//4
	}
	//若第一次插入结点 让游标指向0号结点
	if (tmp->length == 0)
	{
		tmp->slider = node;
	}
 
	//4 链表长度++
	tmp->length++;
	return ret;
}
 
 
//获取一个双向链表list中pos位置处的元素
DLinkListNode* DLinkList_Get(DLinkList* list, int pos)
{
	//1 缓存下来 进行操作
	TDLinkList    *tmp = (TDLinkList *)list;
	//辅助指针 用来遍历当前指针位置
	DLinkListNode *pCur = NULL;
	if (NULL == list || pos < 0)
	{
		printf("func err DLinkList_Get\n");
		return NULL;
	}
	//2 当前指针 初始化 指向 头结点
	pCur = &(tmp->header);
	//3 搜索要获得的结点
	for (int i = 0; i < pos; i++)
	{
		pCur = pCur->next;
	}
	return pCur->next;
}
 
 
//删除一个循环链表list中pos位置处的元素,返回值为被删除的元素,NULL表示删除失败
DLinkListNode* DLinkList_Delete(DLinkList* list, int pos)
{
	//1 缓存下来 进行操作
	TDLinkList    *tmp = (TDLinkList *)list;
	//辅助指针 用来遍历当前指针位置
	DLinkListNode *pCur = NULL;
	//辅助指针 用来缓存删除结点下一元素
	DLinkListNode *pAfter = NULL;
	//辅助指针 用来缓存删除元素
	DLinkListNode *DeletNode = NULL;
	if (NULL == list || pos < 0)
	{
		printf("func err DLinkList_Delete\n");
		return NULL;
	}
	//删除位置的pos点不能大于链表长度  做一个容错修正 
	//当删除位置pos大于双向链表长度,就尾部删除
	if (pos > DLinkList_Length(tmp))
	{
		pos = tmp->length;
	}
	//2 当前指针 初始化 指向 头结点
	pCur = &(tmp->header);
	//3 搜索要获得的结点
	for (int i = 0; i < pos; i++)
	{
		pCur = pCur->next;
	}
	//4 缓存结点位置
	DeletNode = pCur->next;
	pAfter = DeletNode->next;
	//5 开启删除操作 分三种情况
	pCur->next = pAfter;//普通情况1
	if (pAfter !=NULL)
	{
		pAfter->pre = pCur;//普通情况2
	}
	DeletNode->pre = NULL;//第三种情况需要置空 第二种已经自己置空
 
	//6 链表长度--
	tmp->length--;
 
	//7 若删除元素为游标所指元素 需要后移
	if (tmp->slider == DeletNode)
	{
		tmp->slider = pAfter;
	}
 
	//8 若删除元素后链表长度为0  
	if (tmp->length == 0)
	{
		tmp->header.next = NULL;
		tmp->header.pre = NULL;
		tmp->slider = NULL;
	}
	return DeletNode;
}
 
 
//add
 
//根据结点 直接指定删除链表中的某个数据元素
DLinkListNode* DLinkList_DeleteNode(DLinkList* list, DLinkListNode* node)
{
	//1 缓存下来 进行操作
	TDLinkList    *tmp = (TDLinkList *)list;
	//辅助指针 用来遍历当前指针位置
	DLinkListNode *pCur = NULL;
	//辅助指针 用来缓存删除元素
	DLinkListNode *DeletNode = NULL;
	if (NULL == list || 0  == node)
	{
		printf("func err DLinkList_DeleteNode\n");
		return NULL;
	}
	//2 当前指针 初始化 指向 头结点
	pCur = &(tmp->header);
	//3 搜索要获得的结点
	int i;
	for ( i = 0; i < tmp->length; i++)
	{
		if (pCur->next == node)//根据删除结点搜索到要删除位置
		{
			DeletNode = pCur->next;//缓存删除元素
			break;//这里搜索到要删除的结点,结束循环,否则会报错
		}
		pCur = pCur->next;
	}
	//4 根据pos位置删除元素
	if (DeletNode != NULL)
	{
		DLinkList_Delete(tmp,i);
	}
	return DeletNode;
}
 
 
//将游标重置指向链表中的第一个数据元素
DLinkListNode* DLinkList_SliderReset(DLinkList* list)
{
	//1 缓存下来 进行操作
	TDLinkList    *tmp = (TDLinkList *)list;
	//辅助指针 用来缓存重置游标位置
	DLinkListNode *tmpReset = NULL;
	if (NULL == list)
	{
		printf("func err DLinkList_SliderReset\n");
		return NULL;
	}
	if (tmp!=NULL)
	{
		tmp->slider = tmp->header.next;//重置指向第一个数据元素
		tmpReset = tmp->slider;//缓存游标位置
	}
	return tmpReset;
}
 
 
//获取当前游标指向的数据元素
DLinkListNode* DLinkList_SliderCurrent(DLinkList* list)
{
	//1 缓存下来 进行操作
	TDLinkList    *tmp = (TDLinkList *)list;
	//辅助指针 用来缓存当前游标位置
	DLinkListNode *tmpCur = NULL;
	if (NULL == list)
	{
		printf("func err DLinkList_SliderCurrent\n");
		return NULL;
	}
	if (tmp!=NULL)
	{
		tmpCur = tmp->slider;//缓存当前游标位置
	}
	return tmpCur;
}
 
 
//将游标移动指向到链表中的下一个数据元素
DLinkListNode* DLinkList_SliderNext(DLinkList* list)
{
	//1 缓存下来 进行操作
	TDLinkList    *tmp = (TDLinkList *)list;
	//辅助指针 用来缓存游标位置
	DLinkListNode *tmpNext = NULL;
	if (NULL == list)
	{
		printf("func err DLinkList_SliderNext\n");
		return NULL;
	}
	if (tmp != NULL)
	{
		tmpNext = tmp->slider;//缓存当前游标位置
		tmp->slider = tmpNext->next;//将游标下移
	}
	return tmpNext;
}
 
//将游标移动指向双向链表中的前一个数据元素
DLinkListNode* DLinkList_SliderPre(DLinkList *list)
{
	//1 缓存下来 进行操作
	TDLinkList    *tmp = (TDLinkList *)list;
	//辅助指针 用来缓存游标位置
	DLinkListNode *tmpPre = NULL;
	if (NULL == list)
	{
		printf("func err DLinkList_SliderPre\n");
		return NULL;
	}
	if (tmp != NULL)
	{
		tmpPre = tmp->slider;//缓存当前游标位置
		tmp->slider = tmpPre->pre;//将游标上移
	}
	return tmpPre;
}
