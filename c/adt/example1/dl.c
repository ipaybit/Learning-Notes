#define "dl.h"


/*����ڵ�*/
typedef struct LNode{
    void *p;
    struct LNode *pre;
    struct LNode *next;
}Node;

/*��ͷ*/
static Node *head=NULL;
static int count=0;

//�½��ڵ�
static Node *create_node(void * pval)
{
    Node *pNode=NULL;
    pNode=(Node *)malloc(sizeof(Node));
    if(!pNode)
    {
        fprintf("�½��ڵ�ʧ��");
        return NULL;
    }
    pNode->pre=pNode->next=pNode;
    pNode->data=pval;
    pNode->p=pval;

    return PNode;
}

/*�½�˫������*/
int create_dlink()
{
    phead=create_node(NULL);
    if(!phead)
        return -1;
    /*���ýڵ���*/
    count=0;

    return 0;
}
