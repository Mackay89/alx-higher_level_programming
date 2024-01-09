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
	long int size = (PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python list = %d\n", size);
	printf("[*] Alloc = %d\n", obj->alloc);
	for (i = 0; i < size; i++)
	printf("Element %i: %s\n", ((PyList_item[i])->obj_type)->tp_name);
}
