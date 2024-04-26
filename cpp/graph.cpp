#include "graph.h"

using namespace std;

Graph::Graph(vector<vector<Edge>> adj_list, map<pair<int, int>, int> w) : adjacency_list(adj_list), weights(w) {}
