#ifndef PRIM_MST_H
#define PRIM_MST_H

#include "graph.h"

using namespace std;

class PrimMST
{
public:
  vector<vector<Edge>> adjacency_list;

  PrimMST();

  Graph find_mst(Graph &graph, int start_vertex);
  Graph find_mst_parallel(Graph &graph, int start_vertex);
};

#endif // PRIM_MST_H
