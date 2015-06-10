#include <iostream>
#include <memory>
#include <string>

//make_unique function declaration (doesn't exist in C++11, only in C++14)
template <class T, class... Ts> std::unique_ptr<T> make_unique (Ts&&... params) {
  return std::unique_ptr<T> (new T(std::forward<Ts>(params)...));
}


//range template
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

//Template specialization (not very usefull in this case)
template<> class range<std::string> {
  private:
    std::string _st;
    int pos;
  public:
    range(std::string s):_st(s), pos(0) {}
    const range& begin() { return *this; }
    const range& end() { return *this; }
    
    void operator++ (int) {++pos;}
    void operator++ () {++pos;}
    bool operator!=(const range &) { return pos!=_st.length(); }
    char operator* () { return _st[pos];}
};

int main() {
  range<std::string> r_s ("this is a string");
  for (auto it=r_s.begin(); it!=r_s.end(); ++it) {
    std::cout << *it;
  }
  std::cout << std::endl;

  std::unique_ptr<range<int>> r_u = make_unique<range<int>> (10,16) ;
  for (auto it=r_u->begin(); it!=r_u->end(); ++it)
    std::cout << *it << std::endl;

  range<int> r (5,10);
  for (auto it = r.begin(); it!=r.end(); ++it)
    std::cout << *it << std::endl;
  
  range<double> r2(50.0, 55.0);
  for (auto it = r2.begin(); it!=r2.end(); it++)
    std::cout << *it << std::endl;
}
