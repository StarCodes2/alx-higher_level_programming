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
	int size, i, e, rev;
	listint_t *temp = *head, *rev_temp, *keep;

	size = _len(&temp);
	rev = size - 1;
	temp = *head;
	if (size > 0)
	{
		if (size % 2 == 0)
			e = size / 2;
		else
			e = (size / 2) + 1;

		for (i = 0; i < e; i++)
			temp = temp->next;

		rev_temp = rev_list(&temp);
		keep = rev_temp;
		temp = *head;

		for (i = 0; i < rev; i++)
		{
			if (temp->n != rev_temp->n)
			{
				rev_list(&keep);
				return (0);
			}

			temp = temp->next;
			rev_temp = rev_temp->next;
			rev--;
		}
		rev_list(&keep);
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
