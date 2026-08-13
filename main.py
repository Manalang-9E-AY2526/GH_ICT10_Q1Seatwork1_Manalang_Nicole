from pyscript import display, document

# STRING
personname = "Nicole D. Manalang"

# INTEGER
personage = 15

# FLOAT
height123 = 152.4

# LIST
dream_countries = ['Korea', 'Italy', 'Sweden']

# BOOLEAN
student_type = False

# DICTIONARY
sample_dict = {
    'color': 'Blue',
    'car_brand': 'Ford',
    'shoe_size': '8',
    'best_friend': 'Shiloh & Sheir'
}

# SET
fav_fruits = {'Mango', 'Pomelo', 'Watermelon', 'Jackfruit', 'Rambutan'}

# TUPLE
days_week = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
)

display(f'Hello! My name is {personname}.', target='outcome')
display(f'I am {personage} years old.', target='outcome')
display(f'My height is {height123} cm.', target='outcome')
display(f'Someday, I would like to visit {dream_countries}.', target='outcome')
display(f'Is Nicole Manalang a new student at OBMC?: {student_type}.', target='outcome')
display(f'My favorite color is {sample_dict["color"]}.', target='outcome')
display(f'My favorite car brand is {sample_dict["car_brand"]}.', target='outcome')
display(f'My shoe size is {sample_dict["shoe_size"]}.', target='outcome')
display(f'My best friends are {sample_dict["best_friend"]}.', target='outcome')
display(f'My favorite fruits are {fav_fruits}.', target='outcome')
display(f'The days of the week are {days_week}.', target='outcome')