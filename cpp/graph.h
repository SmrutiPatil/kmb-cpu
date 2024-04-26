#ifndef GRAPH_H
#define GRAPH_H

#include "edge.h"
#include <vector>
#include <map>
#include <iostream>

using namespace std;

class Graph
{
public:
  vector<vector<Edge>> adjacency_list;
  map<pair<int, int>, int> weights;

  Graph(vector<vector<Edge>> adj_list, map<pair<int, int>, int> w);

  void printAdjList()
  {
    int i = 0;
    for (auto vec : adjacency_list)
    {

      cout << i << ": ";
      for (auto e : vec)
      {
        cout << e.to << " ";
      }
      i++;
      cout << endl;
    }
  }

  void printEdgeList(bool withWeight = false, bool isViz = false)
  {
    for (int i = 0, endI = adjacency_list.size(); i < endI; i++)
    {
      for (int j = 0, endJ = adjacency_list[i].size(); j < endJ; j++)
      {
        if (i < adjacency_list[i][j].to)
        {
          //~ cout << i << " -- "<< e.to << ": " << e.length << endl;
          if (withWeight)
          {
            cout << adjacency_list[i][j].from << " " << adjacency_list[i][j].to << " : " << adjacency_list[i][j].length << endl;
          }
          else if (isViz)
          {
            cout << i << " -- " << adjacency_list[i][j].to << "[label=" << adjacency_list[i][j].length << ",weight=" << adjacency_list[i][j].length << ",color=red, penwidth=2]" << endl;
          }
          else
          {
            cout << adjacency_list[i][j].from << " " << adjacency_list[i][j].to << endl;
          }
        }
      }
    }
  }

  int getGraphWeight()
  {
    int mstVal = 0;

    for (int i = 0, endI = adjacency_list.size(); i < endI; i++)
    {
      for (int j = 0, endJ = adjacency_list[i].size(); j < endJ; j++)
      {
        if (i < adjacency_list[i][j].to)
          mstVal += adjacency_list[i][j].length;
      }
    }

    return mstVal;
  }
};

#endif // GRAPH_H
