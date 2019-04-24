#pragma once

#ifdef TEST_SHARED
#ifdef TEST_EXPORT
#define TEST_API __declspec(dllexport)
#else
#define TEST_API __declspec(dllimport)
#endif
#else
#define TEST_API
#endif

inline int add(int a, int b)
{
    return a + b;
}

int mul(int a, int b);