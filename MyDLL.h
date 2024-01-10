#include <stdio.h>
#include <windows.h>

#ifdef MYDLL_EXPORTS
#define MYDLL_API __declspec(dllexport)
#else
#define MYDLL_API __declspec(dllimport)
#endif

#ifdef __cplusplus
extern "C" {
#endif

MYDLL_API int Fibo_C(int n);

#ifdef __cplusplus
}
#endif