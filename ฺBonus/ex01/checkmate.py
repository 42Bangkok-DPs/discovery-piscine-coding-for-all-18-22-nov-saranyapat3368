
def checkmate(board):
    """
    ตรวจสอบว่า King ถูกคุกคาม (in check) หรือไม่
    """
    rows = board.strip().split('\n')

    # ตรวจสอบขนาดกระดาน
    if len(rows) != 4 or any(len(row) != 4 for row in rows):
        print("Chessboard must be 4x4")
        return False

    # ค้นหาตำแหน่ง King
    kings = [(i, j) for i in range(4) for j in range(4) if rows[i][j] == 'K']
    if not kings:
        print("King not found")
        return False

    # กำหนดทิศทางการเดินของหมากแต่ละตัว
    moves = {
        'P': [(1, -1), (1, 1)],  # Pawn
        'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],  # Rook
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],  # Bishop
        'Q': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # Queen
    }

    def is_in_bounds(x, y):
        return 0 <= x < 4 and 0 <= y < 4

    # ตรวจสอบการคุกคามของ King
    for king_x, king_y in kings:
        for i in range(4):
            for j in range(4):
                piece = rows[i][j]
                if piece in moves:  # เช็คหมากที่สามารถคุกคาม
                    for dx, dy in moves[piece]:
                        x, y = i, j
                        while is_in_bounds(x + dx, y + dy):
                            x, y = x + dx, y + dy
                            if (x, y) == (king_x, king_y):
                                print("Checkmate detected")
                                return True
                            if rows[x][y] != '.':
                                break
    print("No checkmate detected")
    return False


def suggest_best_move(board):
    """
    แนะนำการเดินหมากที่ดีที่สุดเพื่อป้องกันหรือโจมตี King
    """
    rows = board.strip().split('\n')

    # ค้นหาตำแหน่งของ King และหมากที่เหลือ
    pieces = {}
    king_position = None
    for i in range(4):
        for j in range(4):
            piece = rows[i][j]
            if piece == 'K':
                king_position = (i, j)
            elif piece != '.':
                pieces[(i, j)] = piece

    if not king_position:
        print("King not found")
        return

    # หาท่าทางที่ปลอดภัยที่ King สามารถเดินได้
    safe_moves = [(king_position[0] + dx, king_position[1] + dy) 
                  for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
                  if 0 <= king_position[0] + dx < 4 and 0 <= king_position[1] + dy < 4 and rows[king_position[0] + dx][king_position[1] + dy] == '.']

    # ตรวจสอบว่าแต่ละท่าทางปลอดภัยหรือไม่
    for move in safe_moves:
        if not is_threatened(move, pieces, rows):
            print(f"Safe move for King: {move}")
            return

    print("No safe move available")


def is_threatened(position, pieces, rows):
    """
    ตรวจสอบว่าตำแหน่งที่ต้องการ (position) ถูกโจมตีหรือไม่
    """
    x, y = position
    for (px, py), piece in pieces.items():
        moves = {
            'P': [(1, -1), (1, 1)],
            'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],
            'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            'Q': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],
        }.get(piece, [])

        for dx, dy in moves:
            nx, ny = px, py
            while 0 <= nx < 4 and 0 <= ny < 4:
                nx += dx
                ny += dy
                if (nx, ny) == (x, y):  # ถ้าหมากเดินมาถึงตำแหน่งที่ตรวจสอบ
                    return True
                if rows[nx][ny] != '.':  # ถ้าพบหมากตัวอื่นขวางทาง
                    break
    return False


if __name__ == "__main__":
    board = """\
..K.
PP..
..P.
...."""
    
    if not checkmate(board):  # ตรวจสอบว่า King ถูกคุกคามหรือไม่
        suggest_best_move(board)  # แนะนำการเดินหมากที่ปลอดภัย
