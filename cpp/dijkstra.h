#ifndef DIJKSTRA_H
#define DIJKSTRA_H

#include "graph.h"
#include <vector>

using namespace std;

class Dijkstra
{
public:
  vector<int> dist;
  vector<int> prev;

  Dijkstra();

  void find_shortest_path(Graph &graph, int start, int end, vector<int> &path, vector<Edge> &edges);
  void find_shortest_path_parallel(Graph &graph, int start, int end, vector<int> &path, vector<Edge> &edges);

  int get_shortest_distance(int node);

  vector<int> get_shortest_path(int end);
};

#endif // DIJKSTRA_H
