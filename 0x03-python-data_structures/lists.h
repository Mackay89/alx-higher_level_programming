#ifndef LISTS_H_
#define LISTS_H_

#include <stdlib.h>
#include <stdio.h>

/**
 * structlistint_t - singly link list
 * @n: integer
 * @next: The points to the next node
 * Description: singly linked list node structurew
 */
typedef struct listint_t
{
	int n;
	struct listint_t *next;
} listint_t;

void free_listint(listint_t *head);
listint_t *add_nodeint_end(listint_t **head, const int n);
int is_palindrome(listint_t **head);
size_t print_listint(const listint_t *h);

#endif /* LISTS_H_ */
