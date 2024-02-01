#include <Python.h>

/**
 * print_python_string - Prints python strings information.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int len;

	fflush(stdout);

	print("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf(" [ERROR] Invalid String Object\n");
		return;
	}

	len = ((PyASCIIObject *)(p))->len;

	if (PyUnicode_IS_COMPACT_ASCII(P))
		printf(" type: compact ascii\n");
	else
		printf(" type: compact unicode object\n");
	printf(" len: %ld\n", len);
	printf(" value %ls\n", PyUnicode_AsWideCharString(p, &len));
}
