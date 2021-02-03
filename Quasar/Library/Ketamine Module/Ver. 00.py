# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:14:07 2021

@author: Lunaérosol
"""

import os
from distutils.dir_util import copy_tree
from pathlib import Path

def d(c):
    u=["c0"+str(i)for i in range(8)]
    r=[]
    d=os.getcwd()+"/mods/"
    l=next(os.walk(d))[1]
    t=[]
    for i in l:
        try:
            try:
                if c in os.listdir(d+i+"/fighter"):
                    y=[]
                    for j in u:
                        if j in next(os.walk(d+i+"/fighter/"+c+"/model/body/"))[1]:
                            y.append(j)
                    if 0<len(y):
                        r.append(y)
                    t.append(i)
            except:
                for y in next(os.walk(d+i))[1]:
                    if c in next(os.walk(d+i+"/"+y+"/fighter/"))[1]:
                        y=[]
                        for j in u:
                            y=[]
                            if j in next(os.walk(d+i+"/"+y+"/fighter/"+c+"/model/body/"))[1]:
                                y.append(j)
                        if 0<len(y):
                            r.append(y)
                        t.append(i+"/"+y)
        except:
                try:
                    if c in os.listdir(d+i):
                        y=[]
                        for j in u:
                            if j in next(os.walk(d+i+"/"+c+"/model/body/"))[1]:
                                y.append(j)
                        if 0<len(y):
                            r.append(y)
                        t.append(i)
                except:
                    os.remove(l+i)
    return t,r
            
f=["c0"+str(i) for i in range(0,8)]
r=["mario","donkey","link","samus","yoshi","kirby","fox","pikachu","luigi","ness","captain","purin","peach","koopa","popo","sheik","zelda","mariod","pichu","falco","marth","younglink","ganon","mewtwo","roy","gamewatch","metaknight","pit","szerosuit","wario","snake","ike","pzenigame","pfushigisou","plizardon","diddy","lucas","sonic","dedede","pikmin","lucario","robot","toonlink","wolf","murabito","rockman","wiifit","rosetta","littlemac","gekkouga","miifighter","miiswordsman","miigunner","palutena","pacman","reflet","shulk","koopajr","duckhunt","ryu","cloud","kamui","bayonetta","inkling","ridley","simon","krool","shizue","gaogaen","packun","jack","brave","buddy","dolly","master","tantan","pickel","edge "]
a={"samusd":"04e","daisy":"13e","koopag":"14b","nana":"15p","lucina":"21e","chrom":"25e","pitb":"28e","ptrainer":"33p","ken":"60e","richter":"63e"}

command=input("Input a command to execute or a character's codename/number : ")

while command!="end":
    try:
        command=int(command)
        if command<0:
            raise ValueError
        command=r[command+1]
    except:
        if command in a.values():
            for key,value in a.items():
                if value==command:
                    command==key
    if command=="extend":
        p=input("Enter the CCN to add : ")
        a[p]=input("Enter the corresponding alternative numbered value : ")
        try:
            a[p]=int(a[p])
            raise ValueError
        except:
            print("\nSuccessfully added the variant "+p+", numbered "+a[p]+".")
    if command=="update":
        r.append(input("What's the CCN of the character you want to add ? : "))
    if command in r or a:
        for i in range(len(d(command)[0])):
            print("\n"+d(command)[0][i]+"\n    Replaces these slots : ",end="")
            for y in range(len(d(command)[1][i])):
                print(d(command)[1][i][y],end=" ")
    if command=="list"or command=="charlist":
        for i in range(len(r)):
            i+=1
            if i<=9:
                i="0"+str(i)
            print(i,r[int(i)-1])
        if command=="list":
            for i in a:
                print(a[i],i)
    if command=="varialist":
        for i in a:
            print(a[i],i)
    if command=="extract":
        d=str(Path(os.getcwd()).parent)+"/Mods/SmashUltimate/Skins/"
        l=next(os.walk(d))[1]
        for i in l:
            print("Importing "+next(os.walk(d+i))[1][0]+"...")
            copy_tree(d+i,os.getcwd()+"/mods")
        print("\nDone !")
    command=input("\nYou may use other commands or another codename/number : ")
