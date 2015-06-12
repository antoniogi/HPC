#include <stdio.h>
#include <stdlib.h>
#include "mpi.h" 
#define MAX_NAME_LEN 128
#define MAX_DESC_LEN 1024

int main (int argc, char *argv[]) {
  int i, num_cvar, nameLen, verbosity, descLen, binding, vali;
  double vald;
  int required = MPI_THREAD_SINGLE, provided, err, scope;
  char name [MAX_NAME_LEN], desc[MAX_DESC_LEN];
  MPI_T_cvar_handle handle;
  int count;

  MPI_T_enum enumtype;
  MPI_Datatype datatype;

  MPI_Init_thread(0, 0, required, &provided);

  MPI_T_init_thread(required, &provided);
  MPI_T_cvar_get_num(&num_cvar);
  printf ("Number of MPI control variables: %d\n", num_cvar);
  for (i =0; i<num_cvar; ++i) {
    nameLen = sizeof(name);
    descLen = sizeof(desc);
    err = MPI_T_cvar_get_info (i, name, &nameLen, &verbosity, &datatype, &enumtype, desc, &descLen, &binding, &scope);
    MPI_T_cvar_handle_alloc (i, NULL, &handle, &count);
    if (datatype==MPI_INT) {
      MPI_T_cvar_read (handle, &vali);
      printf ("\t%-48s\t%d\t%-16s\n", name, vali, desc);
    }
    else if(datatype==MPI_DOUBLE) {
      MPI_T_cvar_read(handle, &vald);
      printf ("\t%-48s\t%f\t%-16s\n", name, vald, desc);
    }
    else if (datatype==MPI_CHAR) { //Don't care much about these ones right now
      printf ("\t%-58s\t%s\n", name, desc);
    }
    MPI_T_cvar_handle_free(&handle);
  }
  MPI_T_finalize();
  MPI_Finalize();
  return 0;

}
