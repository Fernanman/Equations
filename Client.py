import pygame
from Network import Network

def main():
    run = True
    n = Network()

    while run:
        x = input()
        n.send(x)

if __name__ == "__main__":
    main()