from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_id = {}
        email_to_name = {}
        n = len(accounts)
        parent = [i for i in range(10001)]  # Enough size
        rank = [1] * 10001

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        id_counter = 0

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = id_counter
                    email_to_name[email] = name
                    id_counter += 1
                union(email_to_id[account[1]], email_to_id[email])  # Union first email with all others

        # Group emails by their root
        roots = defaultdict(list)
        for email, idx in email_to_id.items():
            root_id = find(idx)
            roots[root_id].append(email)

        # Build result
        result = []
        for emails in roots.values():
            name = email_to_name[emails[0]]
            result.append([name] + sorted(emails))

        return result
