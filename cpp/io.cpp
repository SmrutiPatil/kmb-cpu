#include "io.h"

#include "graph.h"
#include "kmb.h"

#include <sstream>
#include <algorithm>

using namespace std;

void readInput(vector<vector<Edge>> &graph, map<pair<int, int>, int> &W, vector<int> &terminals)
{
  string code, type, dummy;

  while (cin >> code >> type)
  {
    transform(code.begin(), code.end(), code.begin(), ::toupper);

    if (code == "SECTION" && type == "Graph")
    {
      long m, n;
      long u, v, w;
      cin >> dummy >> n;
      cin >> dummy >> m;

      graph.resize(n + 1);
      for (long i = 0; i < m; i++)
      {
        cin >> dummy >> u >> v >> w;
        graph[u].push_back(Edge(v, w, u));
        graph[v].push_back(Edge(u, w, v));
        W[make_pair(u, v)] = w;
        W[make_pair(v, u)] = w;
      }
      cin >> dummy;
    }
    else if (code == "SECTION" && type == "Terminals")
    {
      long t, u;
      cin >> dummy >> t;
      for (long i = 0; i < t; i++)
      {
        cin >> dummy >> u;
        terminals.push_back(u);
      }
      cin >> dummy;
    }
    else if (code == "SECTION" && type == "Tree")
    {
      cin >> dummy >> dummy >> dummy;
      long b, val;
      cin >> b;

      cin >> dummy >> dummy >> ws;

      for (long i = 0; i < b; i++)
      {
        string line;
        getline(cin, line);
        stringstream sstream(line);
        if (sstream >> dummy, dummy == "b")
        {
          while (sstream >> val)
          {
            // cout << val << " " ;
          }
          // cout << endl;
        }
      }
      long tu, tv;
      for (long i = 0; i < b - 1; i++)
      {
        cin >> tu >> tv;
      }
      cin >> dummy;
    }
    else
    {
      cout << "INVALID FORMAT\nErr in INPUT: " << code << endl;
      exit(1);
    }
  }
}
