#ifndef LIST_H
#define LIST_H

#include <stdlib.h>
/**
 * struct listint_t - single linked list
 * @n: integer
 * @next: the pointer to the next node
 *
 * Description: simply linked list node structure
 */
typedef strct listint_t
{
	int n;
	struct listint_t *next;
} listint_t;

listint_t *add_nodeint(listint_t *head, const int n);
int check_cyclone(listint_t *list);
void free_listint(listint_t * head);
size_t print_listint(const listint_t *h);

#endif 
