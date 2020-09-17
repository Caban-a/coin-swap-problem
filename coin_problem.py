# -*- coding: cp1252 -*-
#import re


##This program aims at solving the mathematical Coin Permutation Problem.
##
##In the initial position, there are X coins 'a' and X coins 'b' in a row, without space.
##X=5:
##        aaaaabbbbb
##        
##The goal is to end up in a configuration where all coins alternate, without space, in X moves or less:
##        ababababab
##        
##The authorized moves are: taking 2 adjacent coins, and move them close to another coin, in line, without removing the spaces.
##For X=5, there are 2 solutions, one of them is:
##        aaaaabbbbb
##        a  aabbbbbAA
##        aBBaabb  baa
##        abba  bABbaa
##        abbaBAbab  a
##          babababABa


def initialPos(nbPieces):
    """Returns the initial position, with spaces on the sides."""
    return ('a' * nbPieces + 'b' * nbPieces).join(['  ', '  '])

def finalPos(nbPieces):
    """Returns a list of all correct final positions, with spaces on the sides."""
    return [('ab' * nbPieces).join(['  ', '  ']), ('ba' * nbPieces).join(['  ', '  '])]

def movePair(currentPos, startMove, endMove):
    """takes a string with '  ' at the beginning and end,
    and returns the result of the move with exactly '  ' at the beginning and end""" 
    newPos = '  '.join([currentPos[:startMove], currentPos [startMove + 2:]])
    return (currentPos[startMove:startMove + 2].join([newPos[:endMove], newPos[endMove+2:]]).strip()).join(['  ', '  '])

def alternations(currentPos) :
    """The number of times 'a' and 'b' alternate in a position.
    For example 'babab' has 4 alternations."""
    gapless = ''.join(currentPos.split())
    return gapless.count('ab') + gapless.count('ba')

def findMoves(currentPos, goalPos, currentTree, nbMoves, maxMoves, nbSol) :
    """Stops when finds nbSol valid solution.
    if nbSol is not specified, finds all solutions"""
    if currentPos in goalPos :
        return [[currentTree + [currentPos.strip()], nbMoves]]
    elif (alternations(currentPos) - (2*nbMoves) < 0) :
        return []
    else :
        solutions = []
        for i in range(len(currentPos)) :
            if ' ' in currentPos[i:i+2] :
                continue
            for j in range(len(currentPos)) :
                if currentPos[j:j+2] != '  ' :
                    continue
                solutions += findMoves(movePair(currentPos, i, j), goalPos, currentTree+[currentPos.strip()], nbMoves+1, maxMoves, nbSol)
                if nbSol >= 0 and len(solutions) >= nbSol :
                    return solutions
        return solutions

def solveCoins(nbPieces, nbSol = -1) :
    """Solves the problem for nbPieces of each type.
    Optionally, nbSol ends the search when that many solutions have been found."""
    return findMoves(initialPos(nbPieces), finalPos(nbPieces), [], 0, nbPieces, nbSol)

def displaySol(solutions) :
    """Displays the result of solveCoins() in a more readable manner."""
    print '%d SOLUTIONS\n' % len(solutions)
    for i in range (len(solutions)) :
        print '\nSolution %d, %d moves' % (i+1, solutions[i][1])
        print '\n'.join(solutions[i][0])
    return
