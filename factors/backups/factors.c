#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * get_factors - finds the factors of a number
 * @num: number
 * Return: pointer to a 2 length array of the factors
 */
unsigned long long  *get_factors(unsigned long long  num)
{
	unsigned long long  mod, dividend, divisor;
	unsigned long long  *factors;

	factors = malloc(sizeof(unsigned long long ) * 2);
	if (factors == NULL)
		return (NULL);

	divisor = 2;
	while (1)
	{
		mod = num % divisor;

		if (mod == 0)
		{
			factors[0] = num / divisor;
			factors[1] = divisor;
			return (factors);
		}
		divisor++;
	}
	return (NULL);
}

/**
 * main - entry point
 * @argc: number of arguments passed
 * @argv: array of pointer to the arguments
 *
 * Return: 0 (SUCCESS)
 *
 * Description:
 * Factorize as many numbers as possible into a product of two
 * smaller numbers
 */
int main(int argc, char **argv)
{
	FILE *file;
	char *buffer;
	size_t bufsize;
	ssize_t line_len;
	unsigned long long  *factors;

	if (argc != 2)
	{
		fprintf(stderr, "Usage: factors <file>\n");
		exit(EXIT_FAILURE);
	}

	file = fopen(argv[1], "r");
	if (file == NULL)
	{
		perror("Failed to open file\n");
		exit(EXIT_FAILURE);
	}

	bufsize = 0;
	buffer = NULL;
	while ((line_len = getline(&buffer, &bufsize, file)) != -1)
	{
		factors = get_factors(atoll(buffer));
		if (factors == NULL)
		{
			fprintf(stderr, "An error occured\n");
			exit(EXIT_FAILURE);
		}
		printf("%lld=%lld*%lld\n", atoll(buffer), factors[0], factors[1]);
		free(factors);
	}

	free(buffer);
	fclose(file);
	return (0);
}
