import abc


class Vehicle(abc.ABC):

    def __init__(self, maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange):
        self.__maxVelocity = maxVelocity
        self.__mass = mass
        self.__paylod = paylod
        self.__make = make
        self.__model = model
        self.__year = year
        self.__warrantyPeriod = warrantyPeriod
        self.__autopilot = autopilot
        self.__vin = vin
        self.__maxRange = maxRange

    def get_maxVelocity(self):
        return self.__maxVelocity

    def set_maxVelocity(self, maxVelocity):
        self.__maxVelocity = maxVelocity

    def get_mass(self):
        return self.__mass

    def set_mass(self, mass):
        self.__mass = mass

    def get_paylod(self):
        return self.__paylod

    def set_paylod(self, paylod):
        self.__paylod = paylod

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_warrantyPeriod(self):
        return self.__warrantyPeriod

    def set_warrantyPeriod(self, warrantyPeriod):
        self.__warrantyPeriod = warrantyPeriod

    def get_autopilot(self):
        return self.__autopilot

    def set_autopilot(self, autopilot):
        self.__autopilot = autopilot

    def get_vin(self):
        return self.__vin

    def get_maxRange(self):
        return self.__maxRange

    def set_maxRange(self, maxRange):
        self.__maxRange = maxRange

    maxVelocity = property(get_maxVelocity, set_maxVelocity)
    mass = property(get_mass, set_mass)
    paylod = property(get_paylod, set_paylod)
    make = property(get_make)
    model = property(get_model)
    year = property(get_year)
    warrantyPeriod = property(get_warrantyPeriod, set_warrantyPeriod)
    autopilot = property(get_autopilot, set_autopilot)
    vin = property(get_vin)
    maxRange = property(get_maxRange, set_maxRange)

    @abc.abstractmethod
    def test_system(self):
        pass

    @abc.abstractmethod
    def move(self, range):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    def load_cargo(self, cargo_weight):
        if cargo_weight > self.paylod:
            print("Not possible")
        else:
            print(f"Load {cargo_weight}")

    def unload_cargo(self, cargo_weight):
        print(f"Unload {cargo_weight}")


class Engine:

    def __init__(self, engineType, power, volume):
        self.__engineType = engineType
        self.__power = power
        self.__volume = volume

    def get_engineType(self):
        return self.__engineType

    def get_power(self):
        return self.__power

    def get_volume(self):
        return self.__volume

    engineType = property(get_engineType)
    power = property(get_power)
    volume = property(get_volume)


class WheeledVehicle(Vehicle):

    def __init__(self, maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, axisCount, wheelsCount):
        super().__init__(maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange)
        self.__axisCount = axisCount
        self.__wheelsCount = wheelsCount

    def get_axisCount(self):
        return self.__axisCount

    def get_wheelsCount(self):
        return self.__wheelsCount

    axisCount = property(get_axisCount)
    wheelsCount = property(get_wheelsCount)

    def move(self, range):
        print(f"{self.model} drove {range}")


class AirVehicle(Vehicle):

    def __init__(self, maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, wingsCount, maxAltitude):
        super().__init__(maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange)
        self.__wingsCount = wingsCount
        self.__maxAltitude = maxAltitude

    def get_wingsCount(self):
        return self.__wingsCount

    def get_maxAltitude(self):
        return self.__maxAltitude

    def set_maxAltitude(self, maxAltitude):
        self.__maxAltitude = maxAltitude

    wingsCount = property(get_wingsCount)
    maxAltitude = property(get_maxAltitude, set_maxAltitude)

    def move(self, range):
        print(f"{self.model} flew {range}")

    def take_off(self):
        print(f"{self.model} take off!")

    def land(self):
        print(f"{self.model} started landing")


class WaterVehicle(Vehicle):

    def __init__(self, maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, displacement, underWaterSupport):
        super().__init__(maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange)
        self.__displacement = displacement
        self.__underWaterSupport = underWaterSupport

    def get_displacement(self):
        return self.__displacement

    def set_displacement(self, displacement):
        self.__displacement = displacement

    def get_underWaterSupport(self):
        return self.__underWaterSupport

    displacement = property(get_displacement, set_displacement)
    underWaterSupport = property(get_underWaterSupport)

    def move(self, range):
        print(f"{self.model} sailed {range}")


class RailVehicle(Vehicle):

    def __init__(self, maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, axisCount, Railswidth):
        super().__init__(maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange)
        self.__axisCount = axisCount
        self.__Railswidth = Railswidth

    def get_axisCount(self):
        return self.__axisCount

    def get_Railswidth(self):
        return self.__Railswidth

    axisCount = property(get_axisCount)
    Railswidth = property(get_Railswidth)

    def move(self, range):
        print(f"{self.model} drove on rails {range}")


class Car(WheeledVehicle):

    def __init__(self, maxVelocity, engine, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, axisCount, wheelsCount, doorCount, bodyType, colour, automatedGears):
        super().__init__(maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, axisCount, wheelsCount)
        self.__engine = engine
        self.__doorCount = doorCount
        self.__bodyType = bodyType
        self.__colour = colour
        self.__options = []
        self.__automatedGears = automatedGears

    def get_engine(self):
        return self.__engine

    def get_doorCount(self):
        return self.__doorCount

    def get_bodyType(self):
        return self.__bodyType

    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        self.__colour = colour

    def get_options(self):
        return self.__options

    def set_options(self, options):
        self.__options.extend(options)

    def get_automatedGears(self):
        return self.__automatedGears

    def set_automatedGears(self, automatedGears):
        self.__automatedGears = automatedGears

    engine = property(get_engine)
    doorCount = property(get_doorCount)
    bodyType = property(get_bodyType)
    colour = property(get_colour, set_colour)
    options = property(get_options, set_options)
    automatedGears = property(get_automatedGears, set_automatedGears)

    def start_engine(self):
        print(f"{self.engine} started")

    def test_system(self):
        print("Turn the key!")
        print("System test started!")

    def stop(self):
        print(f"{self.model} stopped as a car")

    def load_fuel(self, amount):
        print(f"Load {amount} fuel")


class AirPlane(AirVehicle, WheeledVehicle):

    def __init__(self, maxVelocity, engine, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, axisCount, wheelsCount, passengersCount, classType, minRunway, runwayType, entranceCount, engineCount):
        super().__init__(maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, axisCount, wheelsCount)
        self.__engine = engine
        self.__passengersCount = passengersCount
        self.__classType = classType
        self.__minRunway = minRunway
        self.__runwayType = runwayType
        self.__entranceCount = entranceCount
        self.__engineCount = engineCount

    def get_engine(self):
        return self.__engine

    def get_passengersCount(self):
        return self.__passengersCount

    def set_passengersCount(self, passengersCount):
        self.__passengersCount = passengersCount

    def get_classType(self):
        return self.__classType

    def get_minRunway(self):
        return self.__minRunway

    def set_minRunway(self, minRunway):
        self.__minRunway = minRunway

    def get_runwayType(self):
        return self.__runwayType

    def set_runwayType(self, runwayType):
        self.__runwayType = runwayType

    def get_entranceCount(self):
        return self.__entranceCount

    def get_engineCount(self):
        return self.__engineCount

    def set_engineCount(self, engineCount):
        self.__engineCount = engineCount

    engine = property(get_engine)
    passengersCount = property(get_passengersCount, set_passengersCount)
    classType = property(get_classType)
    minRunway = property(get_minRunway, set_minRunway)
    runwayType = property(get_runwayType, set_runwayType)
    entranceCount = property(get_entranceCount)
    engineCount = property(get_engineCount, set_engineCount)

    def start_engine(self):
        print(f"{self.engineCount} {self.engine} started")

    def test_system(self):
        print("Push the button!")
        print("System test started!")

    def stop(self):
        print(f"{self.model} stopped as a aeroplene")

    def load_fuel(self, amount):
        print(f"Load {amount} fuel")


class JetSki(WaterVehicle):

    def __init__(self, maxVelocity, engine, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, displacement, underWaterSupport, colour):
        super().__init__(maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, displacement, underWaterSupport)
        self.__engine = engine
        self.__colour = colour

    def get_engine(self):
        return self.__engine

    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        self.__colour = colour

    engine = property(get_engine)
    colour = property(get_colour, set_colour)

    def start_engine(self):
        print(f"{self.engine} started")

    def test_system(self):
        print("Turn the key!")
        print("System test started!")

    def stop(self):
        print(f"{self.model} stopped as a jetski")

    def load_fuel(self, amount):
        print(f"Load {amount} fuel")


class Train(RailVehicle):

    def __init__(self, maxVelocity, engine, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, axisCount, Railswidth, locomotivesCount, maxEmptyCartsCount, cartsCount):
        super().__init__(maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, axisCount, Railswidth)
        self.__engine = engine
        self.__locomotivesCount = locomotivesCount
        self.__maxEmptyCartsCount = maxEmptyCartsCount
        self.__cartsCount = cartsCount

    def get_engine(self):
        return self.__engine

    def get_locomotivesCount(self):
        return self.__locomotivesCount

    def set_locomotivesCount(self, locomotivesCount):
        self.__locomotivesCount = locomotivesCount

    def get_maxEmptyCartsCount(self):
        return self.__maxEmptyCartsCount

    def set_maxEmptyCartsCount(self, maxEmptyCartsCount):
        self.__maxEmptyCartsCount = maxEmptyCartsCount

    def get_cartsCount(self):
        return self.__cartsCount

    def set_cartsCount(self, cartsCount):
        self.__cartsCount = cartsCount

    engine = property(get_engine)
    locomotivesCount = property(get_locomotivesCount, set_locomotivesCount)
    maxEmptyCartsCount = property(
        get_maxEmptyCartsCount, set_maxEmptyCartsCount)
    cartsCount = property(get_cartsCount, set_cartsCount)

    def start_engine(self):
        print(f"{self.engine} started")

    def test_system(self):
        print("System test started!")

    def stop(self):
        print(f"{self.model} stopped as a train")

    def load_fuel(self, amount):
        print(f"Load {amount} fuel")


class Helicopter(AirVehicle):

    def __init__(self, maxVelocity, engine, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, wingsCount, maxAltitude, passengersCount, propellerCount):
        super().__init__(maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, wingsCount, maxAltitude)
        self.__engine = engine
        self.__passengersCount = passengersCount
        self.__propellerCount = propellerCount

    def get_engine(self):
        return self.__engine

    def get_passengersCount(self):
        return self.__passengersCount

    def set_passengersCount(self, passengersCount):
        self.__passengersCount = passengersCount

    def get_propellerCount(self):
        return self.__propellerCount

    engine = property(get_engine)
    passengersCount = property(get_passengersCount, set_passengersCount)
    propellerCount = property(get_propellerCount)

    def start_engine(self):
        print(f"{self.engine} started")

    def test_system(self):
        print("Push the button!")
        print("System test started!")

    def stop(self):
        print(f"{self.model} stopped as a helicopter")

    def load_fuel(self, amount):
        print(f"Load {amount} fuel")


class Railcar(RailVehicle):

    def __init__(self, maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, axisCount, Railswidth, seatCount):
        super().__init__(maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, axisCount, Railswidth)
        self.__seatCount = seatCount

    def get_seatCount(self):
        return self.__seatCount

    def set_seatCount(self, seatCount):
        self.__seatCount = seatCount

    seatCount = property(get_seatCount, set_seatCount)

    def test_system(self):
        print("Checking a railcar by a railway worker")

    def stop(self):
        print(f"{self.model} stopped as a railcar")


class Bicycle(WheeledVehicle):

    def __init__(self, maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, axisCount, wheelsCount, classType, speedNumber):
        super().__init__(maxVelocity, mass, paylod, make, model, year, warrantyPeriod, autopilot, vin, maxRange, axisCount, wheelsCount)
        self.__classType = classType
        self.__speedNumber = speedNumber

    def get_classType(self):
        return self.__classType

    def get_speedNumber(self):
        return self.__speedNumber

    classType = property(get_classType)
    speedNumber = property(get_speedNumber)

    def test_system(self):
        print("Checking a bicycle by user")

    def stop(self):
        print(f"{self.model} stopped as a bicycle")


if __name__ == "__main__":
    
    hondaEngine = Engine("petrol", 156, 1.8)   
    honda = Car(260, hondaEngine, 2000, 500, "Japan", "accord", 2008, 3, "No", "difh34719247", 1000, 2, 4, 4, "sedan", "black", "No")
    print(honda.vin)
    
    apacheEngine = Engine("petrol", 500, 4.0)
    apache = Helicopter(1000,  apacheEngine, 4000, 1000, "USA", "AH-64", 2014, 3, "No", "asdfasf", 10000, 4, 3000, 6, 2)
    apache.test_system()
    
    potemkin = Railcar(30, 500, 500, "USSR", "Bear", "1950", "Na veka", "Only, if you are drunk", "balalaika", "No limit", 2, 1, 4)
    
    for i in [honda, apache, potemkin]:
        i.move(100)
