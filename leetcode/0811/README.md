# 811. Subdomain Visit Count

## Problem

- [811. Subdomain Visit Count](https://leetcode.com/problems/subdomain-visit-count)

## Solution

### 1. Using Hash Map

```Python
class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        domains = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            subdomains = domain.split(".")
            for idx in range(len(subdomains)):
                key = ".".join(subdomains[idx:])
                domains[key] = domains.get(key, 0) + int(count)

        answer = []
        for domain, count in domains.items():
            answer.append(f"{count} {domain}")

        return answer

```

- Time complexity is O(N^2).
- Space complexity is O(N^2).
