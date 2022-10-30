"""
给定一个许可密钥字符串 s，仅由字母、数字字符和破折号组成。
字符串由 n 个破折号分成 n + 1 组。你也会得到一个整数 k 。
我们想要重新格式化字符串s，使每一组包含 k 个字符，除了第一组，它可以比 k 短，但仍然必须包含至少一个字符。
此外，两组之间必须插入破折号，并且应该将所有小写字母转换为大写字母。
返回 重新格式化的许可密钥 。
"""


def license_key_formatting(s: str, k: int) -> str:
    s = s.replace("-", "").upper()
    n = len(s)
    s_front, s = s[:n % k:], s[n % k:]
    ans = "-".join([s[i*k:i*k+k] for i in range(n // k)])
    if s_front and ans:
        return s_front + "-" + ans
    elif s_front:
        return s_front
    return ans


print(license_key_formatting(s="5F3Z-2e-9-w", k=4))  # ->"5F3Z-2E9W"
print(license_key_formatting(s="2-5g-3-J", k=2))  # ->"2-5G-3J"
print(license_key_formatting("2", 2))  # ->"2"
print(license_key_formatting("a0001afds-", 4))  # ->"A-0001-AFDS"