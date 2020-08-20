#!/usr/bin/env python3


#######################
# DxDiag Files Reader #
# By                  #
# Mosaab Alzoubi      #
#######################



## Import Libraries:
import sys
import os

## General Args:
ver = "0.1"


## Args Analysis:
def help():
    print("\n -=-= Welcome to DxDiag Files Reader DDFR %s =-=-\n\n \
    DDFR reads files extracted by DxDiag and extract Data from \n \
    them to CSV files. \n\n \
    To start Just enter the containing folder.\n \
    -h to print this message.\n \
    -v to print version.\n \
    " % ver)
    
args = sys.argv[1:]
if args == [] or args == ["-h"] : help() ; exit()
if args == ["-v"] : print(ver) ; exit()


if len(args) > 1 :
    print("ERROR 01: This Version of DDFR support only one folder every time."); exit()

folder = args[0]

if not os.path.isdir(folder):
    print("ERROR 02: This Version of DDFR support only one folder every time."); exit()


## Opening
files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
out = open("DDFR_OUTPUT.CSV","w")



## Variables:
firstline = '"File Name","Report Time","Machine Name","Machine ID","Operating System","Language","System Manufacture","System Model","BIOS","Processor","Memory","Available Memory","Windows Dir","DirectX Ver","Display Device #1 Name","Manufacturer","Chip Type","DAC Type","Memory","Display Device #2 Name","Manufacturer","Chip Type","DAC Type","Memory","Drive C:","Free Space","Total Space","File System","Model","Drive D:","Free Space","Total Space","File System","Model","Drive E:","Free Space","Total Space","File System","Model","Drive F:","Free Space","Total Space","File System","Model","Drive G:","Free Space","Total Space","File System","Model","Drive H:","Free Space","Total Space","File System","Model" \n'
out.write(firstline)


def initial():
    global FILENAME
    FILENAME = "NONE"
    global TIME
    TIME = "NONE"
    global NAME
    NAME = "NONE"
    global ID
    ID = "NONE"
    global OS
    OS = "NONE"
    global LANG
    LANG = "NONE"
    global MANUF
    MANUF = "NONE"
    global MODEL
    MODEL = "NONE"
    global BIOS
    BIOS = "NONE"
    global CPU
    CPU = "NONE"
    global RAM
    RAM = "NONE"
    global ARAM
    ARAM = "NONE"
    global DIR
    DIR = "NONE"
    global DVER
    DVER = "NONE"

    global VGA1
    VGA1 = "NONE"
    global V1MANUF
    V1MANUF = "NONE"
    global V1CHIP
    V1CHIP = "NONE"
    global V1DAC
    V1DAC = "NONE"
    global V1RAM
    V1RAM = "NONE"
    global VGA2
    VGA2 = "NONE"
    global V2MANUF
    V2MANUF = "NONE"
    global V2CHIP
    V2CHIP = "NONE"
    global V2DAC
    V2DAC = "NONE"
    global V2RAM
    V2RAM = "NONE"

    global C
    C = "NONE"
    global CFREE
    CFREE = "NONE"
    global CTOTAL
    CTOTAL = "NONE"
    global CFS
    CFS = "NONE"
    global CMODEL
    CMODEL = "NONE"
    global D
    D = "NONE"
    global DFREE
    DFREE = "NONE"
    global DTOTAL
    DTOTAL = "NONE"
    global DFS
    DFS = "NONE"
    global DMODEL
    DMODEL = "NONE"
    global E
    E = "NONE"
    global EFREE
    EFREE = "NONE"
    global ETOTAL
    ETOTAL = "NONE"
    global EFS
    EFS = "NONE"
    global EMODEL
    EMODEL = "NONE"
    global F
    F = "NONE"
    global FFREE
    FFREE = "NONE"
    global FTOTAL
    FTOTAL = "NONE"
    global FFS
    FFS = "NONE"
    global FMODEL
    FMODEL = "NONE"
    global G
    G = "NONE"
    global GFREE
    GFREE = "NONE"
    global GTOTAL
    GTOTAL = "NONE"
    global GFS
    GFS = "NONE"
    global GMODEL
    GMODEL = "NONE"
    global H
    H = "NONE"
    global HFREE
    HFREE = "NONE"
    global HTOTAL
    HTOTAL = "NONE"
    global HFS
    HFS = "NONE"
    global HMODEL
    HMODEL = "NONE"



for ofile in files:
    
    ## Detect number of Lines
    file = folder + "/" + ofile
    initial()
    data = open(file,"r",encoding='latin-1')
    nol = data.read().count("\n")
    data.close()



    ## Detect FILENAME
    FILENAME = ofile.rstrip(".txt")

    ## Detect TIME
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Time of this report") != -1 :
            TIME = temp.split("report: ")[1].replace(","," ")
            break
    data.close()

    ## Detect NAME
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Machine name:") != -1 :
            NAME = temp.split("name: ")[1].replace(","," ")
            break
    data.close()

    ## Detect ID
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Machine Id:") != -1 :
            ID = temp.split("Machine Id: ")[1].replace(","," ")
            break
    data.close()

    ## Detect OS
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Operating System:") != -1 :
            OS = temp.split("Operating System: ")[1].replace(","," ")
            break
    data.close()

    ## Detect LANG
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Language:") != -1 :
            LANG = temp.split("Language: ")[1].replace(","," ")
            break
    data.close()

    ## Detect MANUF
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("System Manufacturer:") != -1 :
            MANUF = temp.split("System Manufacturer: ")[1].replace(","," ")
            break
    data.close()

    ## Detect MODEL
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("System Model:") != -1 :
            MODEL = temp.split("System Model: ")[1].replace(","," ")
            break
    data.close()

    ## Detect BIOS
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("BIOS:") != -1 :
            BIOS = temp.split("BIOS: ")[1].replace(","," ")
            break
    data.close()

    ## Detect CPU
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Processor:") != -1 :
            CPU = temp.split("Processor: ")[1].replace(","," ")
            break
    data.close()

    ## Detect RAM
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Memory:") != -1 :
            RAM = temp.split("Memory: ")[1].replace(","," ").rstrip(" RAM")
            break
    data.close()

    ## Detect ARAM
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Available OS Memory:") != -1 :
            ARAM = temp.split("Available OS Memory: ")[1].replace(","," ").rstrip(" RAM")
            break
    data.close()

    ## Detect DIR
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Windows Dir:") != -1 :
            DIR = temp.split("Windows Dir: ")[1].replace(","," ")
            break
    data.close()

    ## Detect DVER
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("DirectX Version:") != -1 :
            DVER = temp.split("DirectX Version: ")[1].replace(","," ")
            break
    data.close()

    ## Detect VGAs
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Display Devices") != -1 :
            break

    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Card name:") != -1 :
            VGA1 = temp.split("Card name: ")[1].replace(","," ")
            break

    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Manufacturer:") != -1 :
            V1MANUF = temp.split("Manufacturer: ")[1].replace(","," ")
            break

    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Chip type:") != -1 :
            V1CHIP = temp.split("Chip type: ")[1].replace(","," ")
            break

    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("DAC type:") != -1 :
            V1DAC = temp.split("DAC type: ")[1].replace(","," ")
            break

    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Display Memory:") != -1 :
            V1RAM = temp.split("Display Memory: ")[1].replace(","," ")
            break

    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Card name:") != -1 :
            VGA2 = temp.split("Card name: ")[1].replace(","," ")
            break

    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Manufacturer:") != -1 :
            V2MANUF = temp.split("Manufacturer: ")[1].replace(","," ")
            break

    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Chip type:") != -1 :
            V2CHIP = temp.split("Chip type: ")[1].replace(","," ")
            break

    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("DAC type:") != -1 :
            V2DAC = temp.split("DAC type: ")[1].replace(","," ")
            break

    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Display Memory:") != -1 :
            V2RAM = temp.split("Display Memory: ")[1].replace(","," ")
            break

    data.close()


    ## Detect C
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Drive: C:") != -1 :
            C = "YES"
            break
    if C == "YES":    
        temp0 = data.readline().rstrip("\n")
        if temp0.find("Model") == -1:
            CFREE = temp0.split("Free Space: ")[1].replace(","," ")
            CTOTAL = data.readline().rstrip("\n").split("Total Space: ")[1].replace(","," ")
            CFS = data.readline().rstrip("\n").split("File System: ")[1].replace(","," ")
            CMODEL = data.readline().rstrip("\n").split("Model: ")[1].replace(","," ")
        else:
            CMODEL = temp0.split("Model: ")[1].replace(","," ")
    data.close()


    ## Detect D
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Drive: D:") != -1 :
            D = "YES"
            break
    if D == "YES":
        temp0 = data.readline().rstrip("\n")
        if temp0.find("Model") == -1:
            DFREE = temp0.split("Free Space: ")[1].replace(","," ")
            DTOTAL = data.readline().rstrip("\n").split("Total Space: ")[1].replace(","," ")
            DFS = data.readline().rstrip("\n").split("File System: ")[1].replace(","," ")
            DMODEL = data.readline().rstrip("\n").split("Model: ")[1].replace(","," ")
        else:
            DMODEL = temp0.split("Model: ")[1].replace(","," ")
    data.close()


    ## Detect E
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Drive: E:") != -1 :
            E = "YES"
            break
    if E == "YES":
        temp0 = data.readline().rstrip("\n")
        if temp0.find("Model") == -1:
            EFREE = temp0.split("Free Space: ")[1].replace(","," ")
            ETOTAL = data.readline().rstrip("\n").split("Total Space: ")[1].replace(","," ")
            EFS = data.readline().rstrip("\n").split("File System: ")[1].replace(","," ")
            EMODEL = data.readline().rstrip("\n").split("Model: ")[1].replace(","," ")
        else:
            EMODEL = temp0.split("Model: ")[1].replace(","," ")
    data.close()

    ## Detect F
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Drive: F:") != -1 :
            F = "YES"
            break
    if F == "YES":
        temp0 = data.readline().rstrip("\n")
        if temp0.find("Model") == -1:
            FFREE = temp0.split("Free Space: ")[1].replace(","," ")
            FTOTAL = data.readline().rstrip("\n").split("Total Space: ")[1].replace(","," ")
            FFS = data.readline().rstrip("\n").split("File System: ")[1].replace(","," ")
            FMODEL = data.readline().rstrip("\n").split("Model: ")[1].replace(","," ")
        else:
            FMODEL = temp0.split("Model: ")[1].replace(","," ")
    data.close()

    ## Detect G
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Drive: G:") != -1 :
            G = "YES"
            break
    if G == "YES":
        temp0 = data.readline().rstrip("\n")
        if temp0.find("Model") == -1:
            GFREE = temp0.split("Free Space: ")[1].replace(","," ")
            GTOTAL = data.readline().rstrip("\n").split("Total Space: ")[1].replace(","," ")
            GFS = data.readline().rstrip("\n").split("File System: ")[1].replace(","," ")
            GMODEL = data.readline().rstrip("\n").split("Model: ")[1].replace(","," ")
        else:
            GMODEL = temp0.split("Model: ")[1].replace(","," ")
    data.close()

    ## Detect H
    data = open(file,"r",encoding='latin-1')
    for anol in range(0,nol):
        temp = data.readline().rstrip("\n")
        if temp.find("Drive: H:") != -1 :
            H = "YES"
            break
    if H == "YES":
        temp0 = data.readline().rstrip("\n")
        if temp0.find("Model") == -1:
            HFREE = temp0.split("Free Space: ")[1].replace(","," ")
            HTOTAL = data.readline().rstrip("\n").split("Total Space: ")[1].replace(","," ")
            HFS = data.readline().rstrip("\n").split("File System: ")[1].replace(","," ")
            HMODEL = data.readline().rstrip("\n").split("Model: ")[1].replace(","," ")
        else:
            HMODEL = temp0.split("Model: ")[1].replace(","," ")
    data.close()

    newline = '"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s" \n' % (FILENAME,TIME,NAME,ID,OS,LANG,MANUF,MODEL,BIOS,CPU,RAM,ARAM,DIR,DVER,VGA1,V1MANUF,V1CHIP,V1DAC,V1RAM,VGA2,V2MANUF,V2CHIP,V2DAC,V2RAM,C,CFREE,CTOTAL,CFS,CMODEL,D,DFREE,DTOTAL,DFS,DMODEL,E,EFREE,ETOTAL,EFS,EMODEL,F,FFREE,FTOTAL,FFS,FMODEL,G,GFREE,GTOTAL,GFS,GMODEL,H,HFREE,HTOTAL,HFS,HMODEL)

    out.write(newline)

out.close()
