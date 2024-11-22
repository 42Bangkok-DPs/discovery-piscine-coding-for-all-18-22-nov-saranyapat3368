# ฟังก์ชันค้นหาตำแหน่งของราชา
def find_king(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 'K':
                return r, c  # คืนตำแหน่งแถวและคอลัมน์ของราชา
    raise ValueError("King not found on the board!")

# ฟังก์ชันตรวจสอบว่าอยู่ในขอบเขตของกระดานหรือไม่
def is_in_bounds(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

# ฟังก์ชันตรวจสอบว่าราชาถูกคุกคามหรือไม่
def is_king_under_threat(board, king_pos):
    rows, cols = len(board), len(board[0])
    
    # การเคลื่อนที่ของแต่ละชิ้นส่วน
    directions = {
        'P': [(-1, -1), (-1, 1)],  # เบี้ย
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],  # บิชอป
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],  # ปราการ
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)],  # ราชินี
    }
    
    king_r, king_c = king_pos

    # ตรวจสอบทุกชิ้นส่วนบนกระดาน
    for r in range(rows):
        for c in range(cols):
            piece = board[r][c]
            if piece == '.' or piece == 'K':
                continue  # ข้ามตำแหน่งว่างหรือราชา

            # เช็คเบี้ย
            if piece == 'P':
                for dr, dc in directions['P']:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) == (king_r, king_c):  # ถ้าเบี้ยสามารถจับราชา
                        return True

            # เช็คบิชอป, ปราการ, ราชินี
            if piece in ['B', 'R', 'Q']:
                for dr, dc in directions[piece]:
                    nr, nc = r, c
                    while True:
                        nr += dr
                        nc += dc
                        if not is_in_bounds(nr, nc, rows, cols):
                            break  # ถ้าเกินขอบเขตของกระดาน
                        if (nr, nc) == (king_r, king_c):  # ถ้าชิ้นส่วนสามารถจับราชา
                            return True
                        if board[nr][nc] != '.':  # ถ้าพบชิ้นส่วนอื่นขวาง
                            break

    return False  # หากไม่พบการคุกคาม

# ฟังก์ชันหลัก
def main():
    # ตัวอย่างกระดานหมากรุก
    board = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', 'P', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', 'Q', 'K', '.'],]

    try:
        # ค้นหาตำแหน่งราชา
        king_pos = find_king(board)

        # ตรวจสอบว่าราชาถูกคุกคามหรือไม่
        if is_king_under_threat(board, king_pos):
            print("Success")
        else:
            print("Fail")
    except ValueError:
        print("Error: King not found!")

if __name__ == "__main__":
    main()

