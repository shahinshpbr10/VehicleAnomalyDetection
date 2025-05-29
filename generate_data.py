import random
import pandas as pd



def generate_data(sample=1000):
    data = []
    for _ in range(sample):
        engine_temp = round(random.uniform(60, 120), 2)
        rpm = random.randint(800, 5000)
        label = 1 if engine_temp > 100 else 0
        data.append([engine_temp, rpm, label])
    df = pd.DataFrame(data, columns=['engine_temp', 'rpm', 'label'])
    df.to_csv('engine_data.csv', index=False)
    print("Data saved as vehicle_data.csv ")
    
generate_data()
