#from turtle import Turtle, Screen

#timmy  = Turtle()
#print(timmy)
#timmy.shape("turtle")
#timmy.color("blue4")
#timmy.forward(100)

#my_screen = Screen()
#print(my_screen.canvheight)

#my_screen.exitonclick()

#Import PrettyTable class
from prettytable import PrettyTable

#Generate table onject
table = PrettyTable()

#Add columns and data to table
table.add_column(
    fieldname = 'Pokemon Name',
    column = ['Pikachu', 'Squirtle', 'Charmander'])

table.add_column(
    fieldname = 'Type',
    column = ['Electric', 'Water', 'Fire'])

#Align text in table with the align attribute
table.align = 'c'

#Print tableS
print(table)