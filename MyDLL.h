#include <stdio.h>

// cross_platform_macro.h
#ifdef _WIN32
    #ifdef MYDLL_EXPORTS
        #define MYDLL_API __declspec(dllexport)
    #else
        #define MYDLL_API __declspec(dllimport)
    #endif
#else
    #define MYDLL_API
#endif

#ifdef __cplusplus
extern "C" {
#endif

MYDLL_API int Fibo_C(int n);

#ifdef __cplusplus
}
#endif