class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        vector<int> arr(graph.size(), -1);   // color array
        vector<bool> brr(graph.size(), false); // visited

        for(int start = 0; start < graph.size(); start++) {
            if(arr[start] != -1) continue;

            arr[start] = 0;
            queue<int> q;
            q.push(start);
            brr[start] = true;

            while(!q.empty()) {
                int ind = q.front();
                q.pop();

                for(int i : graph[ind]) {
                    if(arr[i] == -1)
                        arr[i] = 1 - arr[ind];   // opposite color
                    else if(arr[i] == arr[ind])
                        return false;

                    if(!brr[i]) {
                        q.push(i);
                        brr[i] = true;
                    }
                }
            }
        }
        return true;
    }
};

