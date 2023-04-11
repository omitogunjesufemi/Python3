#include <stdio.h>
#include "Python.h"

void hello(void)
{
	printf("Hello, World!\n");
}

void print_list(PyObject *l)
{
	PyListObject *ll;
	int i;

	ll = (PyListObject *)l;
	printf("[*] allocated = %ld\n", ll->allocated);
	printf("[*] numbers of items in the variable part = %ld\n",
	       ll->ob_base.ob_size);
	printf("[*] my tp_name is %s\n", ll->ob_base.ob_base.ob_type->tp_name);

	for (i = 0; i < ll->ob_base.ob_size; i++)
	{
		printf("-- Element [%i] : %s\n", i,
		       ll->ob_item[i]->ob_type->tp_name);
	}
	printf("\n");
}
