class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)
        
        for cpdomain in cpdomains:

            count, domain = cpdomain.split()
            count = int(count)
            parts = domain.split('.')
            
            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                counts[subdomain] += count
        
        result = [f"{count} {subdomain}" for subdomain, count in counts.items()]
        return result