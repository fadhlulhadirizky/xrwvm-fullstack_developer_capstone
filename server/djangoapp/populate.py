from .models import CarMake, CarModel

def initiate():
    try:
        print("Starting populate...")
        
        car_make_data = [
            {"name":"NISSAN", "description":"Great cars. Japanese technology"},
            {"name":"Mercedes", "description":"Great cars. German technology"},
            {"name":"Audi", "description":"Great cars. German technology"},
            {"name":"Kia", "description":"Great cars. Korean technology"},
            {"name":"Toyota", "description":"Great cars. Japanese technology"},
        ]

        car_make_instances = []
        for data in car_make_data:
            car_make = CarMake.objects.create(name=data['name'], description=data['description'])
            car_make_instances.append(car_make)
            print(f"Created CarMake: {car_make.name}")

        # Create CarModel instances with the corresponding CarMake instances
        car_model_data = [
          {"name":"Pathfinder", "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
          {"name":"Qashqai", "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
          {"name":"XTRAIL", "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
          {"name":"A-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
          {"name":"C-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
          {"name":"E-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
          {"name":"A4", "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
          {"name":"A5", "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
          {"name":"A6", "type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
          {"name":"Sorrento", "type":"SUV", "year": 2023, "car_make":car_make_instances[3]},
          {"name":"Carnival", "type":"SUV", "year": 2023, "car_make":car_make_instances[3]},
          {"name":"Cerato", "type":"Sedan", "year": 2023, "car_make":car_make_instances[3]},
          {"name":"Corolla", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4]},
          {"name":"Camry", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4]},
          {"name":"Kluger", "type":"SUV", "year": 2023, "car_make":car_make_instances[4]},
        ]

        for data in car_model_data:
            car_model = CarModel.objects.create(
                name=data['name'], 
                car_make=data['car_make'], 
                type=data['type'], 
                year=data['year'],
                dealer_id=1  # Add a default dealer_id since it's required
            )
            print(f"Created CarModel: {car_model.car_make.name} {car_model.name}")

        print("Populate completed successfully!")
        
    except Exception as e:
        print(f"Error during populate: {e}")
        import traceback
        traceback.print_exc()