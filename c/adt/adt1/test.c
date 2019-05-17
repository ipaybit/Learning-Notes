//双向链表的设计与实现测试框架
//text.c
#include <stdlib.h>  
#include <string.h>  
#include <stdio.h>  
#include "DLinkList.h"//c里面.h和.cpp没有差别 但是c++里如果模块化编程，两个头文件都必须包含进来
 
 
//业务结点
typedef struct _tag_Teacher
{
	DLinkListNode node;//包含底层结点
	//业务域
	int age;
 
}Teacher;
 
 
int main()
{
	int ret = 0;
	DLinkList *dlist = NULL;
	Teacher t1, t2, t3, t4;
	t1.age = 1;
	t2.age = 2;
	t3.age = 3;
	t4.age = 4;
	//1 创建并且返回一个空的双向链表
	dlist = DLinkList_Create();
	if (NULL == dlist)
	{
		ret = -1;
		printf("func err DLinkList_Create:%d\n", ret);
		return ret;
	}
	//2 向一个双向链表list的pos位置处插入元素
	ret = DLinkList_Insert(dlist, (DLinkListNode *)&t1, DLinkList_Length(dlist));
	if (ret != 0)
	{
		ret = -2;
		printf("func err DLinkList_Insert:%d\n", ret);
		return ret;
	}
	ret = DLinkList_Insert(dlist, (DLinkListNode *)&t2, DLinkList_Length(dlist));
	ret = DLinkList_Insert(dlist, (DLinkListNode *)&t3, DLinkList_Length(dlist));
	ret = DLinkList_Insert(dlist, (DLinkListNode *)&t4, DLinkList_Length(dlist));
 
	//返回一个双向链表list中的元素个数
	ret = DLinkList_Length(dlist);
	printf("%d ",ret);
	printf("\n========================我是分界线====================\n");
	//遍历双向链表
	for (int i = 0; i < DLinkList_Length(dlist); i++)
	{
		//获取游标所指元素,然后游标下移
		//双向链表 获取当前游标指向的数据元素
		Teacher *tmp = (Teacher *)DLinkList_SliderNext(dlist);
		if (NULL == tmp)
		{
			ret = -3;
			printf("func err DLinkList_SliderNext:%d\n", ret);
			return ret;
		}
		printf("%d ",tmp->age);
	}
	printf("\n========================我是分界线====================\n");
	////将一个双向链表list中的所有元素清空, 循环链表回到创建时的初始状态  
	//DLinkList_Clear(dlist);
	////返回一个双向链表list中的元素个数
	//ret = DLinkList_Length(dlist);
	//printf("%d ", ret);
 
	//再一次 遍历双向链表
	for (int i = 0; i < DLinkList_Length(dlist); i++)
	{
		//获取一个双向链表list中pos位置处的元素
		//DLinkListNode* DLinkList_Get(DLinkList* list, int pos);
		Teacher *tmp = (Teacher *)DLinkList_Get(dlist,i);
		if (NULL == tmp)
		{
			ret = -4;
			printf("func err DLinkList_SliderCurrent:%d\n", ret);
			return ret;
		}
		printf("%d ", tmp->age);
	}
	printf("\n========================我是分界线====================\n");
	//将游标重置指向双向链表中的第一个数据元素
	//DLinkListNode* DLinkList_SliderReset(DLinkList* list);
 
	Teacher *tmp1 = (Teacher *)DLinkList_SliderReset(dlist);
	printf("%d ", tmp1->age);
 
	Teacher *tmp2 = (Teacher *)DLinkList_SliderNext(dlist);
	printf("%d ", tmp2->age);
 
	//直接指定删除双向链表中的某个数据元素
	//DLinkListNode* DLinkList_DeleteNode(DLinkList* list, DLinkListNode* node);
	tmp2 = (Teacher *)DLinkList_DeleteNode(dlist, (DLinkListNode*)tmp2);
	printf("%d ", tmp2->age);
 
	//删除一个双向链表list中pos位置处的元素,返回值为被删除的元素,NULL表示删除失败
	//DLinkListNode* DLinkList_Delete(DLinkList* list, int pos);
	tmp2 = (Teacher *)DLinkList_Delete(dlist, 1);
	printf("%d ", tmp2->age);
 
 
	//将游标移动指向双向链表中的前一个数据元素
	//DLinkListNode* DLinkList_SliderPre(DLinkList *list);
	tmp2 = (Teacher *)DLinkList_SliderPre(dlist);
	printf("%d ", tmp2->age);
 
	DLinkList_Destroy(dlist);
 
	system("pause");
	return 0;
}
