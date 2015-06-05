#include <iostream>

template <class T> class range{
  private:
  T _start;
  T _end;
  public:
    range (T start, T end) : _start(start), _end(end) {}

    const range& begin() { return *this; }
    const range& end() {return *this; }

    void operator++(int) { ++_start;}
    void operator++ () { ++_start; }
    bool operator!=(const range&) { return _start!=_end; }
    T operator* () {return _start;} 
};

int main() {
  range<int> r (5,10);
  for (auto it = r.begin(); it!=r.end(); ++it)
    std::cout << *it << std::endl;
  
  range<double> r2(50.0, 55.0);
  for (auto it = r2.begin(); it!=r2.end(); it++)
    std::cout << *it << std::endl;
}
