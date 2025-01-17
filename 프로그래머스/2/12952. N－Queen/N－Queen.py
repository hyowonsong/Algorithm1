def dfs(n, row, columns, diagonals1, diagonals2):
    if row == n:
        return 1
        
    count = 0
    for col in range(n):
        curr_diag1 = row - col
        curr_diag2 = row + col
        
        if columns[col] or diagonals1[curr_diag1] or diagonals2[curr_diag2]:
            continue
            
        columns[col] = 1
        diagonals1[curr_diag1] = 1
        diagonals2[curr_diag2] = 1
        
        count += dfs(n, row + 1, columns, diagonals1, diagonals2)
        
        columns[col] = 0
        diagonals1[curr_diag1] = 0
        diagonals2[curr_diag2] = 0
            
    return count

def solution(n):
    columns = [0] * n  # 세로 방향 체크
    diagonals1 = [0] * (2 * n - 1)  # / 방향 대각선 체크
    diagonals2 = [0] * (2 * n - 1)  # \ 방향 대각선 체크
    
    return dfs(n, 0, columns, diagonals1, diagonals2)