#include "lists.h"
#include <stdio.h>
#include <stdlib>
#include <unistd.h>
/**
 * insert_node - insert a number into a sorted singly linked list.
 * @head: into a  link list
 * @number: number to be inserted
 * Return: pointer to the head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint *temp = *head;
	listint_t *new = NULL;
	listint_t *current = NULL;

	if (!h)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*h || (*h)->n > number)
	{
		new->next = *head;
		return (*head = new);

	}
	else
	{
		while (temp && temp->n < number)
		{
			ccurrent = temp;
			temp = temp->next;
		}

		current->next = new;
		new->next = current;
	}
	return (new);
}
