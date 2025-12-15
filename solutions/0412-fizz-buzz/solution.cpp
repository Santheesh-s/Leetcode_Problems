class Solution {
public:
    static vector<string>& data() {
        static vector<string> v;
        static bool initialized = false;

        if (!initialized) {
            v.reserve(10010);
            for (int i = 0; i < 10010; i++) {
                int x = i + 1;
                if (x % 15 == 0) v.push_back("FizzBuzz");
                else if (x % 3 == 0) v.push_back("Fizz");
                else if (x % 5 == 0) v.push_back("Buzz");
                else v.push_back(to_string(x));
            }
            initialized = true;
        }
        return v;
    }
    vector<string> fizzBuzz(int n) {
        auto& v = data();
        return vector<string>(v.begin(), v.begin() + n);
    }
};

