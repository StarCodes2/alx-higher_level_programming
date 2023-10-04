#include "lists.h"

/**
 * insert_node - inserts a node into a list using the value in the node to
 *		determine its position
 * @head: points to a pointer that contains the address to the first node
 * @number: holds the value for the new node
 *
 * Return: address to the new node on success and NULL on fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *current, *new;

	if (head == NULL || *head == NULL)
		return (NULL);

	current = *head;
	while (current->n < number)
	{
		temp = current;
		current = temp->next;
	}

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = current;
	if (temp != NULL)
		temp->next = new;

	return (new);
}
