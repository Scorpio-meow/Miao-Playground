#!/usr/bin/env python3
"""
星塵迷宮 - 終端小遊戲

玩法：
- 你是 @
- 蒐集全部 * 星塵就獲勝
- 避開 G 幽靈，被碰到就輸
- 使用 WASD 移動，q 離開
"""

from dataclasses import dataclass

RAW_MAP = [
    '###########',
    '#@..#....*#',
    '#.#.#.##..#',
    '#.#...#...#',
    '#.###.#.#.#',
    '#...#...#.#',
    '#.#.###.#.#',
    '#.#...#...#',
    '#..##.#.#G#',
    '#*....#..*#',
    '###########',
]

DIRS = {
    'w': (-1, 0),
    'a': (0, -1),
    's': (1, 0),
    'd': (0, 1),
}


@dataclass
class Game:
    board: list
    player: tuple
    ghost: tuple
    stars_left: int
    turns: int = 0

    @classmethod
    def from_map(cls, raw):
        board = [list(row) for row in raw]
        player = ghost = None
        stars = 0
        for r, row in enumerate(board):
            for c, ch in enumerate(row):
                if ch == '@':
                    player = (r, c)
                    board[r][c] = '.'
                elif ch == 'G':
                    ghost = (r, c)
                    board[r][c] = '.'
                elif ch == '*':
                    stars += 1
        return cls(board=board, player=player, ghost=ghost, stars_left=stars)

    def draw(self):
        print('\n' + '=' * 28)
        print('        星 塵 迷 宮')
        print('=' * 28)
        print(f'回合：{self.turns}   剩餘星塵：{self.stars_left}')
        print('操作：WASD 移動，q 離開')
        print('-' * 28)
        for r, row in enumerate(self.board):
            line = ''
            for c, ch in enumerate(row):
                if (r, c) == self.player:
                    line += '@'
                elif (r, c) == self.ghost:
                    line += 'G'
                else:
                    line += ch
            print(line)
        print('-' * 28)

    def step_player(self, move):
        dr, dc = DIRS[move]
        nr = self.player[0] + dr
        nc = self.player[1] + dc
        target = self.board[nr][nc]
        if target == '#':
            print('你撞上牆了。')
            return
        self.player = (nr, nc)
        if target == '*':
            self.stars_left -= 1
            self.board[nr][nc] = '.'
            print('你撿到一顆星塵！')

    def step_ghost(self):
        gr, gc = self.ghost
        pr, pc = self.player
        candidates = []
        for dr, dc in DIRS.values():
            nr, nc = gr + dr, gc + dc
            if self.board[nr][nc] != '#':
                dist = abs(pr - nr) + abs(pc - nc)
                candidates.append((dist, nr, nc))
        candidates.sort(key=lambda x: (x[0], x[1], x[2]))
        _, nr, nc = candidates[0]
        self.ghost = (nr, nc)

    def player_caught(self):
        return self.player == self.ghost


def main():
    game = Game.from_map(RAW_MAP)

    print('歡迎來到《星塵迷宮》！')
    print('目標：在幽靈追上你之前，撿完全部星塵。')

    while True:
        game.draw()

        if game.player_caught():
            print('幽靈碰到你了，你輸了。')
            break
        if game.stars_left == 0:
            print('你蒐集了全部星塵，宇宙為你鼓掌。你贏了！')
            break

        move = input('你的移動 > ').strip().lower()
        if move == 'q':
            print('你選擇離開迷宮。')
            break
        if move not in DIRS:
            print('請輸入 w / a / s / d / q')
            continue

        game.step_player(move)
        game.turns += 1

        if game.stars_left == 0:
            game.draw()
            print('你蒐集了全部星塵，宇宙為你鼓掌。你贏了！')
            break

        game.step_ghost()

        if game.player_caught():
            game.draw()
            print('幽靈在你身後現身——你輸了。')
            break


if __name__ == '__main__':
    main()