#include <iostream>
#include <immintrin.h>

using namespace std;
typedef union _m{
  double index[4];
  __m256d intrinc;
} m256d;

int main()
{
  m256d varx;
  varx.intrinc= _mm256_set_pd(13,12,11,10);
  cout << varx.index[3] << "\n";
}
