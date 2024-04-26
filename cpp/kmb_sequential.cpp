#include "kmb.h"
#include "dijkstra.h"
#include "prim_mst.h"
#include <algorithm>
#include <set>

#include <omp.h>

using namespace std;

void KMB::sequential()
{

  // graph.printEdgeList();

  // S1
  cout << "S1" << endl;
  Graph graph1(vector<vector<Edge>>(graph.adjacency_list.size(), vector<Edge>()), {});

  // S2
  cout << "S2" << endl;

  set<pair<int, int>> added_edges;
  map<pair<int, int>, vector<Edge>> shortest_path_edges;

  for (int u : terminals)
  {
    for (int v : terminals)
    {

      if (u < 0 || u >= graph.adjacency_list.size())
      {
        cout << "Invalid terminal " << u << endl;
        continue;
      }
      if (u >= v)
      {
        continue;
        // save time
      }

      vector<int> path;
      vector<Edge> edges;

      Dijkstra dijkstra;
      dijkstra.find_shortest_path(graph, u, v, path, edges);

      shortest_path_edges[{u, v}] = edges;

      if (added_edges.find({u, v}) == added_edges.end() && added_edges.find({v, u}) == added_edges.end())
      {
        graph1.adjacency_list[u].push_back({v, dijkstra.dist[v], u});
        added_edges.insert({
            u,
            v,
        });
      }
    }
  }

  // graph1.printEdgeList();

  // S3
  cout << "S3" << endl;

  PrimMST prim;
  Graph T1 = prim.find_mst(graph1, terminals[0]);

  // T1.printEdgeList();

  // S4
  cout << "S4" << endl;
  set<int> vertices;
  for (auto &edge : shortest_path_edges)
  {
    for (Edge &vertex : edge.second)
    {
      vertices.insert(vertex.to);
    }
  }

  Graph graph2(vector<vector<Edge>>(graph.adjacency_list.size(), vector<Edge>()), {});
  for (auto &edge : shortest_path_edges)
  {
    for (Edge &vertex : edge.second)
    {
      graph2.adjacency_list[vertex.to].push_back({vertex.from, vertex.length, vertex.to});
    }
  }

  // graph2.printEdgeList(true);

  // S5
  cout << "S5" << endl;
  Graph steiner = prim.find_mst(graph2, terminals[0]);

  // steiner.printEdgeList();
  cout << "TREE WEIGHT: "
       << steiner.getGraphWeight() << endl;
}
