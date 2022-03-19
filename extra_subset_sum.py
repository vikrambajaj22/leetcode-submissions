''' return all subsets that sum to target '''


def subset_sum(nums, target):
    sol = []

    def backtrack(index, k, subset, res):
        ''' finding combinations of length k '''
        if k == 0 and sum(subset) == target:
            res.append(subset)
        for i in range(index, len(nums)):
            backtrack(i+1, k-1, subset+[nums[i]], res)

    # find combinations of all lengths [0, n]
    for k in range(0, len(nums)+1):
        k_len_subsets = []
        backtrack(0, k, [], k_len_subsets)
        sol.extend(k_len_subsets)

    return sol
