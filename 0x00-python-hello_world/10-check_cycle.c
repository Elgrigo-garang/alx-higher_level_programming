#include "lists.h"
/**
 * check_cycle-checks if a linked list has a cycle
 * @list:linked list to check
 * Return: 1 if has cycle otherwise 0
 */
int check_cycle(listint_t *list)
{
        listint_t *slow = list;
        listint_t *fast = list;

        if (!list)
                return (0);
        while (slow && fast && fast->next)
        {
                slow = slow->next;
                fast = fast->next->next;
                if (slow == fast)
                        return (1);
        }
        return (0);
