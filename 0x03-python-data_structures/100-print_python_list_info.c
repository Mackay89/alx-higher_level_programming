#include <python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic info about  Python Lists
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int i;
	long int size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*} Size of the Python List = %d\n", PyList_Size);
	printf("[*] Allocated = %d\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %d: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
