class SmartAI(object):
    def __init__(self):
        # 評価マップ: 角が高得点、中央が低得点
        self.evaluation_map = [
            [100, -20, 10, 10, -20, 100],
            [-20, -50, -2, -2, -50, -20],
            [10, -2, 0, 0, -2, 10],
            [10, -2, 0, 0, -2, 10],
            [-20, -50, -2, -2, -50, -20],
            [100, -20, 10, 10, -20, 100]
        ]

    def face(self):
        return "🧠"

    def evaluate_board(self, board, stone):
        """
        現在のボードのスコアを計算する関数。
        """
        score = 0
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == stone:
                    score += self.evaluation_map[y][x]
                elif board[y][x] == 3 - stone:
                    score -= self.evaluation_map[y][x]
        return score

    def place(self, board, stone):
        """
        最適な場所を選んで石を置く。
        """
        best_score = float('-inf')
        best_move = None

        for y in range(len(board)):
            for x in range(len(board[0])):
                if can_place_x_y(board, stone, x, y):
                    # 仮想的に石を置いて評価
                    temp_board = copy(board)
                    move_stone(temp_board, stone, x, y)
                    score = self.evaluate_board(temp_board, stone)

                    if score > best_score:
                        best_score = score
                        best_move = (x, y)

        if best_move is None:
            # 置ける場所がない場合ランダムに置く
            return random_place(board, stone)

        return best_move
