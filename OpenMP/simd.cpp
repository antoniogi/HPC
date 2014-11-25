#include <iostream>

#define N 256 
#define ALIGN 32

#pragma omp declare simd uniform(a) linear(i) simdlen(4)
void foo (int *a, int i) {
  std::cout << a[i] << "\n";
}

int main() {
  int * a = (int *) _mm_malloc(N*sizeof(int),ALIGN);
  for (int i =0; i<N; ++i)
    a[i] = i;
#pragma omp simd  
  for (int i=0; i<N; ++i){
    foo(a,i);
  }
  for (int i=0; i<N; ++i)
    a[i] = 0;
  _mm_free(a);
}
