#!/usr/bin/python

import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

import towns_graph as tg



class GUI:

    def configureRootWindow(self):
        self.__root_window.geometry("890x380")

    def __init__(self):

        self.__root_window=tk.Tk()
        self.configureRootWindow()
        
        self.__main_frame=ttk.Frame(self.__root_window)
        self.__info_frame=ttk.Frame(self.__main_frame)

        self.__town_graph=tg.TownGraph(num_vertices=7)
        self.__town_graph.createGraph()
        self.__town_graph.printGraph()


        self.createGui()

        self.__main_frame.grid()
        self.__root_window.mainloop()

    def createGui(self):

        #Graph Image
        graph_image=Image.open("map.png")
        self.__tk_graph_image=ImageTk.PhotoImage(graph_image)

        #image label
        self.__graph_img_label=ttk.Label(self.__main_frame,image=self.__tk_graph_image,compound="image")

        #buttons for each algorithm
        self.__bfs_btn=ttk.Button(self.__main_frame,text="BFS",command=lambda: self.searchAlgorithm(algorithm="BFS"))
        self.__dfs_btn=ttk.Button(self.__main_frame,text="DFS",command=lambda: self.searchAlgorithm(algorithm="DFS"))
        self.__a_search=ttk.Button(self.__main_frame,text="A*S",command=lambda: self.searchAlgorithm(algorithm="A*S"))


        self.__start_town_label=ttk.Label(self.__main_frame,text="Start City")
        self.__destination_town_label=ttk.Label(self.__main_frame,text="Destination\nCity")

        #comboboxes for selecting the start town and the destination town
        self.__start_town=ttk.Combobox(self.__main_frame,state="readonly")
        self.__target_destination_town=ttk.Combobox(self.__main_frame,state="readonly")

        self.__start_town["values"]=("Nairobi","Nakuru","Garissa","Mombasa","Kisumu","Thika","Malindi")
        self.__target_destination_town["values"]=("Nairobi","Nakuru","Garissa","Mombasa","Kisumu","Thika","Malindi")

        self.__start_town_var=tk.StringVar()
        self.__target_town_var=tk.StringVar()

        self.__start_town_var.set("Nairobi")
        self.__target_town_var.set("Mombasa")

        self.__start_town.configure(textvariable=self.__start_town_var)
        self.__target_destination_town.configure(textvariable=self.__target_town_var)

        #info_frame widgets
        #clear button,
        self.__clear_btn=ttk.Button(self.__info_frame,text="Clear/Hide",command=lambda: self.__info_frame.grid_remove())
        #will be in the info frame to be able to toggle between showing the frame and hiding it
        self.__distance_var=tk.StringVar()
        self.__path_var=tk.StringVar()
        self.__info_var=tk.StringVar()

        self.__info_label=ttk.Label(self.__info_frame,textvariable=self.__info_var)
        self.__path_label=ttk.Label(self.__info_frame,textvariable=self.__path_var)
        self.__distance_label=ttk.Label(self.__info_frame,textvariable=self.__distance_var)

        #grid info_frame widgets
        self.__info_label.pack()
        self.__path_label.pack()
        self.__distance_label.pack()
        self.__clear_btn.pack()


        #grid widgets
        self.__graph_img_label.grid(row=0,column=0,rowspan=10,columnspan=8)

        self.__start_town_label.grid(row=0,column=8)
        self.__destination_town_label.grid(row=1,column=8)

        self.__start_town.grid(row=0,column=9)
        self.__target_destination_town.grid(row=1,column=9)

        self.__bfs_btn.grid(row=2,column=8)
        self.__dfs_btn.grid(row=2,column=9)
        self.__a_search.grid(row=2,column=10)

        self.__info_frame.grid(row=3,column=8,rowspan=4,columnspan=10)
        self.__info_frame.grid_remove()

    def searchAlgorithm(self,algorithm):
        self.__town_graph.setStartVertex(vertex_idx=(self.__town_graph.mapVertexIndex(self.__start_town_var.get()))-1)

        if algorithm=="BFS":
            self.__info_var.set("Breadth First Search Not Optimal")
            print("Using BFS")
            self.__town_graph.breadthFirstSearch()
        elif algorithm=="DFS":
            self.__info_var.set("Depth First Search Not Optimal")
            print("Using DFS")
            self.__town_graph.depthFirstSearch()
        elif algorithm=="A*S":
            self.__info_var.set("A* Search Optimal")
            print("Using A*S")
            self.__town_graph.AStarSearch()
        else:
            print("Algorithm not implemented")
            return

       # self.__distance_var.set("Distance: 700")
       # self.__path_var.set("Path: Nairobi to Mombasa to Lamu to Kisumu to Nyeri to Nairobi to Mombasa")

        #self.__town_graph.print_Path(self.__distance_var,self.__path_var)
        self.__town_graph.printDestinationPath(self.__target_town_var.get(),self.__distance_var,self.__path_var)
        self.__info_frame.grid()


GUI()
