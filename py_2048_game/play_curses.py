import curses
from curses.textpad import rectangle
import argparse

from py_2048_game.core import Game

KEYS = {
    curses.KEY_LEFT: 0,
    curses.KEY_UP: 1,
    curses.KEY_RIGHT: 2,
    curses.KEY_DOWN: 3,
}

def main(stdscr, seed=None):
    stdscr.clear()

    game = Game(seed=seed)
    rectangle(stdscr, 0, 0, 2+3, 2+8)

    while 1:
        for i, (a, b, c, d) in enumerate(game._state):
            stdscr.addstr(i+1, 2, '%s %s %s %s' % (a, b, c, d))
        stdscr.addstr(6, 0, 'Round: %s' % game.move_count)
        stdscr.addstr(7, 0, 'Score: %s' % game.score)

        while 1:
            key = stdscr.getch()
            if key in KEYS:
                break
        action = KEYS[key]

        reward = game.do_action(action)
        if reward:
            stdscr.addstr(8, 6, '+%d' % reward)
        else:
            stdscr.addstr(8, 6, ' '*10)

        if game.game_over():
            stdscr.addstr(9, 0, 'GAME OVER')
            stdscr.getch()
            break

        stdscr.refresh()

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--seed', type=int)


if __name__ == '__main__':
    args = parser.parse_args()
    try:
        curses.wrapper(
            main,
            seed=args.seed,
        )
    except KeyboardInterrupt:
        pass
