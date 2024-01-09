#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	int i;
	long int size = (PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python list = %d\n", size);
	printf("[*] Alloc = %d\n", obj->alloc);
	for (i = 0; i < size; i++)
	printf("Element %i: %s\n", i,py_TYPE(obj->ob_getitem)-[i])->tp_name);
}
