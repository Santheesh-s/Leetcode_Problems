class Solution {
public:
    vector<vector<int>> mergeSimilarItems(vector<vector<int>>& items1, vector<vector<int>>& items2) {
        map<int,int>m;
        vector<vector<int>> ls;
        for(int i=0;i<items1.size();i++)
        {
            ls.push_back({items1[i][0],items1[i][1]});
            m[items1[i][0]]=i;
        }
        for(int i=0;i<items2.size();i++)
        {
            if(m.find(items2[i][0]) != m.end())
                ls[ m [ items2[i][0] ] ][1]+=items2[i][1];
            else
                ls.push_back({items2[i][0],items2[i][1]});
        }
        sort(ls.begin(),ls.end());
        return ls;
    }
};
