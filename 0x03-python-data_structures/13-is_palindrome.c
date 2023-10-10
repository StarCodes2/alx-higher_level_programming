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
	int size, i, rev;
	listint_t *temp, *rev_temp;

	size = _len(head);
	rev = size - 1;
	temp = *head;
	if (size > 0)
	{
		rev_temp = rev_list(head);

		for (i = 0; i < rev; i++)
		{
			if (temp->n != rev_temp->n)
				return (0);

			temp = temp->next;
			rev_temp = rev_temp->next;
			rev--;
		}
	}
	return (1);
}

/**
 * rev_list - reverse the order of a singly linked list
 * @head: holds the address of a pointer to the first node
 *
 * Return: the new list
 */

listint_t *rev_list(listint_t **head)
{
	listint_t *temp = *head, *prev = NULL, *next;

	while (temp)
	{
		next = temp->next;
		temp->next = prev;
		prev = temp;
		temp = next;
	}

	temp = prev;
	return (temp);
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
