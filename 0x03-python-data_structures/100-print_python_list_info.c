#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	int i;
	long int size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*} Size of the Python List = %lu\n", PyList_Size);
	printf("[*] Allocated = %lu\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %d: %s\n", i, Py_TYPE(obj->ob__item[i])->tp_name);
}
