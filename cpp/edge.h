#ifndef EDGE_H
#define EDGE_H

class Edge
{
public:
  int to;
  int length;
  int from;

  Edge();
  ~Edge();
  Edge(int t, int l, int f);
  bool operator<(const Edge &e) const;
};

#endif // EDGE_H
