#include "graph.h"
#include "kmb.h"
#include "io.h"
#include <algorithm>
#include <iostream>
#include <chrono>
#include <getopt.h>
#include <omp.h>

using namespace std;
using namespace chrono;

int main(int argc, char *argv[])
{
  const char *short_options = "sibo";

  omp_set_num_threads(omp_get_max_threads());

  int opt;
  int mode = 0;
  while ((opt = getopt(argc, argv, short_options)) != -1)
  {
    switch (opt)
    {
    case 's':
      mode = 1;
      break;
    case 'i':
      mode = 2;
      break;
    case 'o':
      mode = 3;
      break;
    case 'b':
      mode = 4;
      break;
    default:
      break;
    }
  }

  vector<vector<Edge>> adjacency_list;
  map<pair<int, int>, int> W;
  vector<int> terminals;

  readInput(adjacency_list, W, terminals);

  time_point<system_clock> start, end;
  start = system_clock::now();

  Graph graph(adjacency_list, W);

  KMB kmb(graph, terminals);

  switch (mode)
  {
  case 1:
    kmb.sequential();
    break;
  case 2:
    kmb.innerParallel();
    break;
  case 3:
    kmb.outerParallel();
    break;
  case 4:
    kmb.bothParallel();
    break;
  default:
    cout << "Invalid mode" << endl;
    break;
  }

  end = system_clock::now();
  duration<double> elapsed_seconds = end - start;
  cout << "time: " << elapsed_seconds.count() << "s\n";

  return 0;
}
