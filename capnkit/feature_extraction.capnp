# file ID
@0xc0f3fb718abd90b9;

struct NgramRange {
    min @0 :UInt16;
    max @1 :UInt16;
}

struct NgramVectorizer {
    tokenPattern @0 :Text;
    ngramRange @1 :NgramRange;
    vocabulary @2 :List(Text);
    stopWords @3 :List(Text);
}

struct TfidfTransformer {
    idf @0 :List(Float64);
}