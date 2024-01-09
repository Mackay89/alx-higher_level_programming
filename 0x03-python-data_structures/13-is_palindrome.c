#include "lists.h"
#include <stdio.h>

listint_t *reverse_listint(listint_t **head);
int is palidrome(listint_t **head);

/**
 * is_palidrome - Checks if a singly linked list is a palidrome.
 * @head: Pointer to the head linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int i;
	listint_t *temp;
	listint_t *middle, rev;
	size_t size = 0,

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	middle = *head;

	while (temp)
	{
		size++;
		temp = temp->next;
	}

	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;
	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next;
	rev = reverse_listint(&temp);
	middle = rev;

	temp = *head;
	while (rev)
	{
		if (temp-> != rev->n)
			return (0);
		temp = tem->next;
		rev = rev->next;
	}
	reverse_listint(&middle);

	return (1);
}

/**
 * reverse_listint - Reverses a singly linked listint_t list
 * @head: Pointer to the starting node of the list to reverse
 * Return: Pointer to the head  of reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *current = NULL

	while (node)
	{
		next = node->next;
		node->next = current;
		current = node;
		node = next;
	}

	*head = current;
	return (*head);
}
