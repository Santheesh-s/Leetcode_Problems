class Solution {
public:
    int ladderLength(string begin, string end, vector<string>& word) {
        set<string> words(word.begin(),word.end());
        int level=1;
        if(!words.contains(end)) return 0;
        queue<string>q;
        q.push(begin);
        while(!q.empty())
        {
            int size=q.size();
            while(size-->0)
            {
                string p=q.front();
                q.pop();
                if(p==end) return level;
                for(int i=0;i<p.size();i++)
                {
                    char temp=p[i];
                    for(char ch='a';ch<='z';ch++)
                    {
                        p[i]=ch;
                        if(words.contains(p))
                        {
                            words.erase(p);
                            q.push(p);
                        }
                    }
                    p[i]=temp;
                }
            }
            level++;
        }
        return 0;
    }
};
