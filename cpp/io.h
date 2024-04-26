#ifndef INPUT_READER_H
#define INPUT_READER_H

#include "graph.h"
#include "kmb.h"
#include <iostream>
#include <map>
#include <vector>

using namespace std;

void readInput(vector<vector<Edge>> &graph, map<pair<int, int>, int> &W, vector<int> &terminals);

#endif // INPUT_READER_H
