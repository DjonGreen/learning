def we_crash_all(name: str) -> str:    
    return 'Привет, ' + name + ', мы всё сломали!'

# Аннотированный класс
class Contact:
    def __init__(self, 
                 name: str, 
                 year_birth: int, 
                 is_programmer: bool) -> None:
        
        self.name = name
        self.year_birth = year_birth
        self.is_programmer = is_programmer
        
    def age_define(self) -> str:
        if 1946 < self.year_birth < 1980:
            return 'Олдскулл'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'
    
    def programmer_define(self) -> str:
        if self.is_programmer:
            return 'Программист'
        return 'Норм'

    def show_contact(self) -> str:
        return(f'{self.name}, '
               f'категория: {self.age_define()}, '
               f'статус: {self.programmer_define()}')
        
    def print_contact(self) -> None:
        print(self.show_contact())
        
        
# Компоновщики

from typing import Sequence, List, Union, Callable

def lower_join(seq: Sequence[str]) -> str:
    """Принимает на вход последовательность и создает из нее строку в нижнем регистре

    Args:
        seq (Sequence[str]): _description_

    Returns:
        str: _description_
    """
    return ''.join(seq).lower()

# Задача 2
def series_sum(incoming: List[Union[str, float]]) -> str:
    """ Принимает на вход список, приводит его элементы к строкам и конкатенирует их

    Args:
        incoming (List[Union[str, float]]): _description_

    Returns:
        str: _description_
    """
    result = ''
    for i in incoming:
        result += str(i)
    return result

# Задача 3

def add(number: float, func: Callable[[float], float]) -> float: 
    """Производит арифметические действия над числами.
    Принимает на вход число и функцию, выполняющую действие.

    Args:
        number (float): _description_
        func (Callable[[float], float]): _description_

    Returns:
        float: _description_
    """

    return func(number)

def adder20(number: float) -> float:
    return number**0.5

