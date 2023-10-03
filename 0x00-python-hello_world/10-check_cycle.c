#include "lists.h"

/**
 * check_cycle - check if a singly linked list is a circular linked list
 * @list: points to the list
 *
 * Return: 0 if there is no circle, 1 if there is a circle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	while (temp)
	{
		temp = temp->next;
		if (temp == list)
			return (1);
	}

	return (0);
}
