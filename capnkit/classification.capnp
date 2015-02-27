# file ID
@0xdca2471173b6c06c;

struct LogisticRegression {
    intercept @0 :Float64;
    coef @1 :List(List(Float64));
    classes @2 :List(Text);
}