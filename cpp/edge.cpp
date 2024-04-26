#include "edge.h"

Edge::Edge() {}
Edge::~Edge() {}
Edge::Edge(int t, int l, int f) : to(t), length(l), from(f) {}
bool Edge::operator<(const Edge &e) const
{
  return length < e.length;
}
