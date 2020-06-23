# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class PriorityQ:
    def __init__(self, n=0):
        self.data = [[0, i] for i in range(n)]
    
    def siftDown(self, i):
        assert len(self.data) > 0
        n = len(self.data)
        while True:
            if ((2 * i) + 1) >= n:
                break
            if ((2 * i) + 2) < n:
                l, r = (2 * i) + 1, (2 * i) + 2
                if self.data[i] < self.data[l] and self.data[i] < self.data[r]:
                    break
                if self.data[r] < self.data[l]:
                    temp = r
                else:
                    temp = l
                self.data[i], self.data[temp] = self.data[temp], self.data[i]
                i = temp
            else:
                l = (2 * i) + 1
                if self.data[i] < self.data[l]:
                    break
                self.data[i], self.data[l] = self.data[l], self.data[i]
                break

    def getMin(self):
        assert len(self.data) > 0
        return self.data[0]
    
    def changePriority(self, p):
        assert len(self.data) > 0
        self.data[0][0] += p 
        self.siftDown(0)

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = PriorityQ(n_workers)

    for job in jobs:
        next_worker = next_free_time.getMin()
        # print("next_worker:", next_worker)
        result.append(AssignedJob(next_worker[1], next_worker[0]))
        next_free_time.changePriority(job)

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
