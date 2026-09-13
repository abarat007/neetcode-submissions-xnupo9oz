class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        accounts_map = {} # email: list of account indices
        map2 = {} # account_idx: list of emails

        # fill in accounts_map
        for i in range(n):
            emails = accounts[i][1:]
            for email in emails:
                if email not in accounts_map:
                    accounts_map[email] = [i]
                else:
                    accounts_map[email].append(i)
        
        # fill in map2
        for i in range(n):
            emails = accounts[i][1:]
            map2[i] = emails
        
        # make graph, connecting nodes (account index) to edges (shared emails)
        graph = {}

        for i in range(n):
            graph[i] = []
        
        for email, account_indices_list in accounts_map.items():
            first = account_indices_list[0]
            for idx in account_indices_list[1:]:
                graph[first].append(idx)
                graph[idx].append(first)
        
        visited = set()
        def dfs(account_idx, email_set):
            if account_idx in visited:
                return
            
            visited.add(account_idx)

            # collect emails
            for email in map2[account_idx]:
                email_set.add(email)
            
            for neighbor in graph[account_idx]:
                dfs(neighbor, email_set)

        res = []
        for i in range(n):
            if i not in visited:
                email_set = set()
                dfs(i, email_set)

                name = accounts[i][0]
                res.append([name]+sorted(email_set))
        
        return res

        

        
       





        
        
                
                



        
            






            
        