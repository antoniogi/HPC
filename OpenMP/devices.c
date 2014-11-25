#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define N 10

int main(int argc, char* argv[])
{
  int i;
  int *a, *b;
  a = (int *) malloc(sizeof(int)*N);
  b = (int *) malloc(sizeof(int)*N);
  for (i=0; i<N; ++i) {
    a[i] = i;
    b[i] = 0;
  }
#pragma omp target data device(0) map(to: a[0: N]) map(from: b[0: N])
  {
#pragma omp target device(0)
    {
      memcpy(&b , &a, N);
      for (i=0; i<N; ++i) {
        printf ("Remote a[%d] = %d -- Remote b[%d] = %d\n", i, a[i], i, b[i]);
      }
    }
  }
  for (i=0; i<N; ++i)
    printf("Local a[%d] = %d -- Local b[%d] = %d\n", i, a[i], i, b[i]);
  return 0;
}

