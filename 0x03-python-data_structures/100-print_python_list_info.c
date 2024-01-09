#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Print basic info about a python list
 * @p: the pointer to a PyObject
 */
void print_python_list_info(PyObject *p)
{
	int i, alloc;
	long int size = (PyListObject *)p;
	alloc = (PyListObject *)p->alloc;

	printf("[*] Size of the Python list = %d\n", size);
	printf("[*] Alloc = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %i: %s\n",((PyList_item(p, i))->object_type)->tp_name);
	}
}
