class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total_time = 0
        k_bought_all_tickets = False

        while True:
            current_pass_time = 0
            
            for i in range(len(tickets)):
                if tickets[i] == 0:
                    continue

                tickets[i] -= 1
                current_pass_time += 1

                if i == k and tickets[i] == 0:
                    k_bought_all_tickets = True
                    break
            
            total_time += current_pass_time

            if k_bought_all_tickets:
                break

        return total_time
