#include <stdio.h>

#define MYDLL_API __declspec(dllimport)

#ifdef __cplusplus
extern "C" {
#endif

MYDLL_API int Fibo_C(int n);

#ifdef __cplusplus
}
#endif