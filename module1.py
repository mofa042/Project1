from datetime import datetime

def greet(name):
    hour = int(datetime.now().strftime(format="%H"))
    greet = ""
    
    if (hour >= 5):
        greet = "Morning"
    if (hour >= 12):
        greet = "Afternoon"
    if (hour >= 17):
        greet = "Evening"
    if (hour >= 21 or hour < 5):
        greet = "Night"
        
    print(f"Good {greet}, {name}!")