#include "lists.h"

/**
 * check_cycle - check if a singly linked list contains a circular linked list
 * @list: points to the list
 *
 * Return: 0 if there is no circle, 1 if there is a circle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	while (temp && list)
	{
		temp = temp->next;
		list = list->next;
		list = list->next;
		if (temp == list)
			return (1);
	}

	return (0);
}
