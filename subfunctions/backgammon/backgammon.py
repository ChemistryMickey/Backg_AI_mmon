import curses
from sys import path
import pathlib

from subfunctions.backgammon.backgammon_board import BackgammonBoard
path.append(f'{pathlib.Path( __file__ ).parent.resolve()}/../misc');
from MDCG_log import db_log, investigate

def backgammon(player1, player2):
    """
    Design:
        ASCII Backgammon game

        0) Generate board in default setup
        1) Allow user input to move pieces
    """

    board = BackgammonBoard();