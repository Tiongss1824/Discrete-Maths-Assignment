MOD = 10**9

def compute_amoeba_arrangements(N):
    # DP array to store the number of configurations
    dp = [0] * (N + 1)
    dp[0] = 1  # Initial configuration with no divisions

    for i in range(1, N + 1):
        dp[i] = (dp[i - 1] * 2) % MOD

    return dp[N]

N = 10000
result = compute_amoeba_arrangements(N)
print(f"The last nine digits of D({N}) are: {result:09d}")
