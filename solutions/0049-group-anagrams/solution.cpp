class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string,vector<string>>mp;

        for(string s:strs)
        {
            string ss=s;
            sort(s.begin(),s.end());
            mp[s].push_back(ss);
        }
        vector<vector<string>>res;
        for(pair<string,vector<string>>p:mp)
            res.push_back(p.second);
        return res;
        
    }
};
