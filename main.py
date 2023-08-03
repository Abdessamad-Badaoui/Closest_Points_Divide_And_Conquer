#!/usr/bin/env python3

import sys
from ast import arg
from tkinter.messagebox import NO
from turtle import distance
from geo.point import Point
from geo.tycat import tycat
from geo.segment import Segment
import math
from timeit import timeit
from sys import argv


def load_instance(filename):
    """
    loads .mnt file. 
    returns list of points.
    """
    with open(filename, "r") as instance_file:
        points = [Point((float(p[0]), float(p[1]))) for p in (l.split(',') for l in instance_file)]

    return points

# 1ère version
 
def plus_prochesv1(tab):
    dist = tab[0].distance_to(tab[1])
    idxpt1 = 0
    idxpt2 = 1
    for i in range(len(tab)):
        for j in range(i+1, len(tab)):
            if tab[i].distance_to(tab[j]) < dist:
                dist = tab[i].distance_to(tab[j])
                idxpt1 = i
                idxpt2 = j

    return (dist , tab[idxpt1],tab[idxpt2])

### Cout de cette fonction est O(n**2) avec n la taille du tableau 

# 2eme version

def parcours_bande(tab_bande ):
    if len(tab_bande)>1 :
        d_min = tab_bande[0].distance_to(tab_bande[1])
        idx1 = 0
        idx2 = 1
        for i in range(len(tab_bande)-1) :
            if len(tab_bande)-i > 7 :
                a = i+8
            else :
                a = len(tab_bande)
            for j in range(i+1,a):
                if tab_bande[i].distance_to(tab_bande[j]) < d_min :
                    d_min = tab_bande[i].distance_to(tab_bande[j])
                    idx1 = i
                    idx2 = j


        return (d_min,tab_bande[idx1],tab_bande[idx2])
    else :
        return None , None ,None

def plus_prochesv2(tableau):
    tx = sorted(tableau, key = lambda point : point.coordinates[0])
    ty = sorted(tableau, key = lambda point : point.coordinates[1])
    if len(tableau) < 4 :
        return plus_prochesv1(tableau)
    else :
        txg , txd = tx[:len(tx)//2] , tx[len(tx)//2:]
        dd ,pt1x ,pt1y = plus_prochesv2(txd)
        dg ,pt2x ,pt2y = plus_prochesv2(txg)
        if dd > dg :
            d_min , x , y = dg , pt2x , pt2y
        else :
            d_min , x , y = dd , pt1x , pt1y
        if len(tx)%2 == 1:
            borne = tx[len(tx)//2].coordinates[0]
        else:
            borne = (tx[len(tx)//2].coordinates[0] + tx[len(tx)//2 - 1].coordinates[0])/2
        bande = [elem for elem in ty if borne - d_min <= elem.coordinates[0] <= borne + d_min]
        dbande_min ,x_bande ,y_bande = parcours_bande(bande)
        if dbande_min is None :
            return d_min , x , y
        elif d_min < dbande_min :
            return d_min , x , y
        else :
            return dbande_min , x_bande ,y_bande


def print_solution(points):
    """
    calcul et affichage de la solution (a faire)
    """
    _, p1, p2 = plus_prochesv2(points)
    print(f"{p1}; {p2}")

def main():
    """
    ne pas modifier: on charge des instances donnees et affiches les solutions
    """
    for instance in argv[1:]:
        points = load_instance(instance)
        print_solution(points)

main()
