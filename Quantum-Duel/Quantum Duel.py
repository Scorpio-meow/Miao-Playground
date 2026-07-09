#!/usr/bin/env python3
"""
量子猜拳 Quantum Duel

規則：
- 你和 AI 各有 12 HP
- 每回合可選：
  a = 斬擊（穩定傷害）
  b = 格擋（減傷、反制衝動打法）
  c = 蓄能（下回合強化）
  q = 離開
- 蓄能後下次斬擊會變成「量子斬」造成更高傷害
"""

import random
from dataclasses import dataclass


@dataclass
class Fighter:
    name: str
    hp: int = 12
    charged: bool = False


def resolve(player: Fighter, enemy: Fighter, p_move: str, e_move: str):
    log = []
    pdmg = 0
    edmg = 0

    if p_move == 'c':
        player.charged = True
        log.append('你開始蓄能，空氣變得不太科學。')
    if e_move == 'c':
        enemy.charged = True
        log.append('AI 正在蓄能，眼神逐漸發光。')

    if p_move == 'a':
        pdmg = 4 if player.charged else 2
        log.append('你使出量子斬！' if player.charged else '你使出普通斬擊。')
        player.charged = False
    if e_move == 'a':
        edmg = 4 if enemy.charged else 2
        log.append('AI 使出量子斬！' if enemy.charged else 'AI 發動普通斬擊。')
        enemy.charged = False

    if p_move == 'b' and e_move == 'a':
        edmg = max(0, edmg - 2)
        log.append('你成功格擋，卸掉大半攻勢。')
    if e_move == 'b' and p_move == 'a':
        pdmg = max(0, pdmg - 2)
        log.append('AI 格擋成功，你的斬擊被化開。')

    if p_move == 'b' and e_move == 'c':
        enemy.hp -= 1
        log.append('你看穿 AI 蓄能破綻，偷點 1 傷害。')
    if e_move == 'b' and p_move == 'c':
        player.hp -= 1
        log.append('AI 抓到你蓄能空檔，點了你 1 下。')

    enemy.hp -= pdmg
    player.hp -= edmg

    return log


def ai_move(enemy: Fighter, player: Fighter):
    choices = ['a', 'b', 'c']
    weights = [0.45, 0.25, 0.30]

    if enemy.charged:
        weights = [0.65, 0.25, 0.10]
    elif player.charged:
        weights = [0.30, 0.50, 0.20]
    elif enemy.hp <= 4:
        weights = [0.55, 0.30, 0.15]

    return random.choices(choices, weights=weights, k=1)[0]


def pretty(move: str):
    return {
        'a': '斬擊',
        'b': '格擋',
        'c': '蓄能',}[move]


def show(player: Fighter, enemy: Fighter, round_no: int):
    print('\n' + '=' * 30)
    print(f'       量 子 猜 拳  Round {round_no}')
    print('=' * 30)
    print(f"你  HP: {player.hp:2d}  狀態: {'蓄能中' if player.charged else '平穩'}")
    print(f"AI  HP: {enemy.hp:2d}  狀態: {'蓄能中' if enemy.charged else '平穩'}")
    print('-' * 30)
    print('a = 斬擊   b = 格擋   c = 蓄能   q = 離開')


def main():
    random.seed()
    player = Fighter('你')
    enemy = Fighter('AI')
    round_no = 1

    print('歡迎來到《量子猜拳》')
    print('重點不是拳，是你敢不敢在 AI 面前蓄能。')

    while player.hp > 0 and enemy.hp > 0:
        show(player, enemy, round_no)
        p_move = input('你的選擇 > ').strip().lower()
        if p_move == 'q':
            print('你選擇保留實力，先撤。')
            return
        if p_move not in {'a', 'b', 'c'}:
            print('請輸入 a / b / c / q')
            continue

        e_move = ai_move(enemy, player)
        print(f'AI 選了：{pretty(e_move)}')
        logs = resolve(player, enemy, p_move, e_move)
        for line in logs:
            print('- ' + line)

        if player.hp <= 0 and enemy.hp <= 0:
            print('\n雙方同時歸零，這是最有尊嚴的平手。')
            return
        if enemy.hp <= 0:
            print('\n你贏了。AI 今天得回去重新訓練。')
            return
        if player.hp <= 0:
            print('\n你輸了。AI 很有禮貌地把你送出場外。')
            return

        round_no += 1


if __name__ == '__main__':
    main()