#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - the infinite loop
 *
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - fxn to creates five zombie processes
 *
 * Return: Always 0
 */
int main(void)
{
	pid_t p_id;
	char count = 0;

	while (count < 5)
	{
		p_id = fork();
		if (p_id > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			count++;
		}
		else
			exit(0);
	}

	infinite_while();
	return (0);
}
