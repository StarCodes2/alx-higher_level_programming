#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a list is a palindrome
 * @head: points to an address that holds a pointer to the first node
 *
 * Return: 1 if its a palindrome or 0 if its not
 */

int is_palindrome(listint_t **head)
{
	int size, *list, i, e;
	listint_t *temp;

	size = _len(head);
	e = size - 1;
	temp = *head;
	if (size > 0)
	{
		list = malloc(sizeof(int) * size);
		if (list == NULL)
			return (NULL);

		for (i = 0; temp; i++)
		{
			list[i] = temp->n;
			temp = temp->next;
		}

		for (i = 0; i < e; i++)
		{
			if (list[i] != list[e--])
				return (0);
		}
	}
	return (1);
}

/**
 * _len - Computes the length of a singly linked list
 * @head: points to an address that holds a pointer to the first node
 *
 * Return: the size of the list
 */

int _len(listint_t **head)
{
	listint_t *temp = *head;
	int i = 0;

	while (temp)
	{
		temp = temp->next;
		i++;
	}
	return (i);
}
