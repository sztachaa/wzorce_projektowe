from director import Director
from computerbuilder import ComputerBuilder

director = Director()
builder = ComputerBuilder()
director.builder = builder

choice = input('1.Komputer podstawowy\n2.Komputer do gier\n')

def switch(choice):
    if choice == '1':
        print("Składam komputer podstawowy:")
        director.build_basic_computer()
        builder.product.list_parts()
        return "Miłego dnia!"
    elif choice == '2':
        print("Składam komputer do gier:")
        director.build_gaming_computer()
        builder.product.list_parts()
        return "Miłego dnia!"
    else:
        return 'Wybrano złą opcję!'


print(switch(choice))