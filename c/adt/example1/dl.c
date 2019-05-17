#define "dl.h"


/*定义节点*/
typedef struct LNode{
    void *p;
    struct LNode *pre;
    struct LNode *next;
}Node;

/*表头*/
static Node *head=NULL;
static int count=0;

//新建节点
static Node *create_node(void * pval)
{
    Node *pNode=NULL;
    pNode=(Node *)malloc(sizeof(Node));
    if(!pNode)
    {
        fprintf("新建节点失败");
        return NULL;
    }
    pNode->pre=pNode->next=pNode;
    pNode->data=pval;
    pNode->p=pval;

    return PNode;
}

/*新建双向链表*/
int create_dlink()
{
    phead=create_node(NULL);
    if(!phead)
        return -1;
    /*设置节点数*/
    count=0;

    return 0;
}
