// This is an example of how to run a random number generator in
// parallel with OpenMP. The default rand() function is executed
// in a critical section, so it's very bad in threaded codes
#include<random>
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main (int argc, char *argv[]) {

  double arrow_area_circle, pi;
  float xp, yp;
  int i, n;
  double pitg= atan(1.0)*4.0; //for pi error
  cout << "Number processors: " << omp_get_num_procs() << endl;

  //Number of divisions
  int iterations=atoi(argv[1]); 
  arrow_area_circle = 0.0;

#pragma omp parallel
  {
    std::uniform_int_distribution<int> distribution (1, RAND_MAX);
    static thread_local std::mt19937 generator;
    //Seed for the rand function
    //srandom(omp_get_thread_num());
#pragma omp for private(xp, yp) reduction(+:arrow_area_circle) 
    for (i = 0; i < iterations; i++) {
      //Rand function. Runs in a critical section, so it's bad
      //xp=rand()/(float)RAND_MAX;
      //yp=rand()/(float)RAND_MAX;
      xp = distribution(generator)/(float)RAND_MAX;
      yp = distribution(generator)/(float)RAND_MAX;
      if(((xp*xp)+(yp*yp))<=1) arrow_area_circle++;
    }
  }

  pi = 4*arrow_area_circle / iterations;
  cout << setprecision(18) << "PI = " << pi << endl << endl;
  cout << setprecision(18) << "Erro = " << pitg-pi << endl << endl;

  return 0;
}
