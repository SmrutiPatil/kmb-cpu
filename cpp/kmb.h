#ifndef KMB_H
#define KMB_H

#include "graph.h"
#include <vector>

using namespace std;

class KMB
{
public:
  Graph graph;
  vector<int> terminals;

  KMB(Graph g, std::vector<int> t);

  void sequential();
  void innerParallel();
  void outerParallel();
  void bothParallel();
};

#endif // KMB_H
