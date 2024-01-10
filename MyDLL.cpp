
#include "MyDLL.h"

int Fibo_C(int n)
{
	if (n < 2)
		return 1;
	else
		return Fibo_C(n - 1) + Fibo_C(n - 2);
}




