class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        graph = defaultdict(list)
        email_to_name = {}

        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
                email_to_name[email] = name

        visited = set()
        result = []

        
        def dfs(email, emails):
            visited.add(email)
            emails.append(email)
            for nei in graph[email]:
                if nei not in visited:
                    dfs(nei, emails)

       
        for email in graph:
            if email not in visited:
                emails = []
                dfs(email, emails)
                result.append([email_to_name[email]] + sorted(emails))

        return result
