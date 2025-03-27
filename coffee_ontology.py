import owlready2

# Create an empty ontology
onto = owlready2.get_ontology("file://coffee_ontology.owl")

with onto:
    class DomainThing(owlready2.Thing):
        pass


    class Country(DomainThing):
        pass


    class Drink(DomainThing):
        pass


    class Coffee(Drink):
        pass


    class CoffeeBase(DomainThing):
        pass


    class CoffeeTopping(DomainThing):
        pass


    class Milk(Drink):
        pass


    class Level(owlready2.Thing):
        pass


    class NamedCoffee(Coffee):
        pass


    # Define individuals for countries
    Brazil = Country("Brazil")
    Colombia = Country("Colombia")
    Ethiopia = Country("Ethiopia")
    Guatemala = Country("Guatemala")
    Hawaii = Country("Hawaii")
    India = Country("India")
    Kenya = Country("Kenya")
    Mexico = Country("Mexico")
    Peru = Country("Peru")
    Yemen = Country("Yemen")
    Italy = Country("Italy")
    Turkey = Country("Turkey")
    Ireland = Country("Ireland")
    Greece = Country("Greece")
    Australia = Country('Australia')


    class High(Level):
        pass


    class Medium(Level):
        pass


    class Low(Level):
        pass


    class NoLevel(Level):
        pass


    class WholeMilk(Milk):
        pass


    class AlmondMilk(Milk):
        pass


    class OatMilk(Milk):
        pass


    class LactoseFreeMilk(Milk):
        pass


    class hasBase(owlready2.ObjectProperty):
        domain = [Drink]
        range = [CoffeeBase]


    class isBaseOf(owlready2.ObjectProperty):
        domain = [CoffeeBase]
        range = [Drink]


    class isToppingOf(owlready2.ObjectProperty):
        domain = [CoffeeTopping]
        range = [Drink]


    class hasTopping(owlready2.ObjectProperty):
        domain = [Drink]
        range = [CoffeeTopping]
        inverse_property = isToppingOf


    class isMilkOf(owlready2.ObjectProperty):
        domain = [Milk]
        range = [Drink]


    class hasMilk(owlready2.ObjectProperty):
        domain = [Drink]
        range = [Milk]
        inverse_property = isMilkOf


    class hasOriginCountry(owlready2.ObjectProperty):
        domain = [Drink]
        range = [Country]


    class isKnownWorldwide(owlready2.DataProperty):
        domain = [Coffee]
        range = [bool]
        functional = True


    class isProteinRich(owlready2.DataProperty):
        domain = [Coffee]
        range = [bool]
        functional = True


    class isServedCold(owlready2.DataProperty):
        domain = [Coffee]
        range = [bool]
        functional = True


    class hasCaffeineContentValue(owlready2.DataProperty):
        domain = [Coffee]
        range = [int]
        functional = True


    class hasCalorificContentValue(owlready2.DataProperty):
        domain = [Coffee]
        range = [int]
        functional = True


    class hasSweetness(owlready2.DataProperty):
        domain = [CoffeeTopping]
        range = [Level]
        functional = True


    class hasIngredient(owlready2.ObjectProperty):
        domain = [Drink]
        range = [Drink]
        transitive = True


    class isIngredientOf(owlready2.ObjectProperty):
        domain = [Drink]
        range = [Drink]
        inverse_property = hasIngredient


    class Water(CoffeeBase):
        pass


    class ArabicaBean(CoffeeBase):
        pass


    class RobustaBean(CoffeeBase):
        pass


    class Sugar(CoffeeBase):
        pass


    class Whiskey(CoffeeBase):
        pass


    class Ice(CoffeeBase):
        pass


    class PistachioSyrup(CoffeeBase):
        pass


    class HazelnutSyrup(CoffeeBase):
        pass


    class CocoaPowder(CoffeeBase):
        pass


    class MacadamiaNutSyrup(CoffeeBase):
        pass


    class NaturalTopping(CoffeeTopping):
        equivalent_to = [CoffeeTopping & (hasSweetness.value(NoLevel))]


    class LiquidTopping(CoffeeTopping):
        pass


    class Caramel(LiquidTopping):
        equivalent_to = [LiquidTopping & (hasSweetness.value(High))]


    class Chocolate(LiquidTopping):
        equivalent_to = [LiquidTopping & (hasSweetness.value(High))]


    class Vanilla(LiquidTopping):
        equivalent_to = [LiquidTopping & (hasSweetness.value(High))]


    class MilkFoam(LiquidTopping):
        equivalent_to = [LiquidTopping & (hasSweetness.value(Medium))]


    class FruitTopping(CoffeeTopping):
        pass


    class Raspberry(FruitTopping):
        equivalent_to = [FruitTopping & (hasSweetness.value(Low))]


    class Strawberry(FruitTopping):
        equivalent_to = [FruitTopping & (hasSweetness.value(Low))]


    class Coconut(FruitTopping):
        equivalent_to = [FruitTopping & (hasSweetness.value(Low))]


    class NutTopping(CoffeeTopping):
        pass


    class CrushedMacadamiaNuts(NutTopping):
        equivalent_to = [NutTopping & (hasSweetness.value(Low))]


    class CrushedHazelnuts(NutTopping):
        equivalent_to = [NutTopping & (hasSweetness.value(Medium))]


    class CrushedPistachios(NutTopping):
        equivalent_to = [NutTopping & (hasSweetness.value(Medium))]


    class PowderTopping(CoffeeTopping):
        pass


    class Cardamom(PowderTopping):
        equivalent_to = [PowderTopping & (hasSweetness.value(Low))]


    class ProteinPowder(PowderTopping):
        equivalent_to = [PowderTopping & (hasSweetness.value(Medium))]


    class Cinnamon(PowderTopping):
        equivalent_to = [PowderTopping & (hasSweetness.value(Low))]


    class SnackTopping(CoffeeTopping):
        pass


    class Cookie(SnackTopping):
        equivalent_to = [SnackTopping & (hasSweetness.value(High))]


    class ProteinBar(SnackTopping):
        equivalent_to = [SnackTopping & (hasSweetness.value(High))]


    class IceCream(SnackTopping):
        equivalent_to = [SnackTopping & (hasSweetness.value(High))]


    class ArabianCoffee(Coffee):
        equivalent_to = (
                Coffee &
                hasBase.only(Water | ArabicaBean | RobustaBean) &
                hasMilk.only(WholeMilk | LactoseFreeMilk) &
                hasTopping.only(NaturalTopping) &
                hasOriginCountry.value(Yemen)
        )


    class BrazilianCoffee(Coffee):
        equivalent_to = (
                Coffee &
                hasBase.some(Water | ArabicaBean | RobustaBean) &
                hasMilk.some(WholeMilk | LactoseFreeMilk) &
                hasTopping.only(NaturalTopping) &
                hasOriginCountry.value(Brazil)
        )


    class ColombianCoffee(Coffee):
        equivalent_to = (
                Coffee &
                hasBase.some(Water | ArabicaBean | RobustaBean) &
                hasMilk.some(WholeMilk | LactoseFreeMilk) &
                hasTopping.only(NaturalTopping) &
                hasOriginCountry.value(Colombia)
        )


    class Espresso(NamedCoffee):
        equivalent_to = (
                NamedCoffee &
                hasBase.some(Water | ArabicaBean | RobustaBean) &
                hasTopping.some(Caramel | Chocolate | Cinnamon) &
                hasOriginCountry.value(Italy)
        )


    class Cappuccino(NamedCoffee):
        equivalent_to = (
                NamedCoffee &
                hasBase.some(Water | ArabicaBean | RobustaBean | Sugar) &
                hasMilk.some(WholeMilk | AlmondMilk | OatMilk | LactoseFreeMilk) &
                hasTopping.only(MilkFoam) &
                hasOriginCountry.value(Italy)
        )


    class Latte(NamedCoffee):
        equivalent_to = (
                NamedCoffee &
                hasBase.some(Water | ArabicaBean | RobustaBean | Sugar) &
                hasMilk.some(WholeMilk | AlmondMilk | OatMilk | LactoseFreeMilk) &
                hasTopping.some(MilkFoam | Caramel | Chocolate | Vanilla) &
                hasOriginCountry.value(Italy)
        )


    class Macchiato(NamedCoffee):
        equivalent_to = (
                NamedCoffee &
                hasBase.some(Water | ArabicaBean | RobustaBean | Sugar) &
                hasMilk.some(WholeMilk | AlmondMilk | OatMilk | LactoseFreeMilk) &
                hasTopping.some(Caramel | Chocolate | Cinnamon) &
                hasOriginCountry.value(Italy)
        )


    class Mocha(NamedCoffee):
        equivalent_to = (
                NamedCoffee &
                hasBase.some(Water | ArabicaBean | RobustaBean | Sugar | CocoaPowder) &
                hasMilk.some(WholeMilk | AlmondMilk | OatMilk | LactoseFreeMilk) &
                hasTopping.some(Caramel | Raspberry | Strawberry | Cinnamon) &
                hasOriginCountry.value(Italy)
        )


    class GreekCoffee(NamedCoffee):
        equivalent_to = (
                NamedCoffee &
                hasBase.some(Water | ArabicaBean | RobustaBean | Sugar) &
                hasTopping.some(Cardamom | Chocolate) &
                hasOriginCountry.value(Greece)
        )


    class IrishCoffee(NamedCoffee):
        equivalent_to = (
                NamedCoffee &
                hasBase.some(Water | ArabicaBean | RobustaBean | Sugar | Whiskey) &
                hasMilk.some(WholeMilk | AlmondMilk | OatMilk | LactoseFreeMilk) &
                hasTopping.some(Caramel | Chocolate) &
                hasOriginCountry.value(Ireland)
        )


    class Frappe(NamedCoffee):
        equivalent_to = (
                NamedCoffee &
                hasBase.some(Water | ArabicaBean | RobustaBean | Sugar | Ice) &
                hasMilk.some(WholeMilk | AlmondMilk | OatMilk | LactoseFreeMilk) &
                hasTopping.some(Caramel | Chocolate) &
                hasOriginCountry.value(Greece)
        )


    class FlatWhite(NamedCoffee):
        equivalent_to = (
                NamedCoffee &
                hasBase.some(Water | ArabicaBean | RobustaBean) &
                hasMilk.some(WholeMilk | AlmondMilk | OatMilk | LactoseFreeMilk) &
                hasTopping.some(Caramel | Chocolate) &
                hasOriginCountry.value(Australia)
        )


    class PistachioLatte(NamedCoffee):
        equivalent_to = (
                NamedCoffee &
                hasBase.some(Water | ArabicaBean | RobustaBean | PistachioSyrup) &
                hasMilk.some(WholeMilk | AlmondMilk | OatMilk | LactoseFreeMilk) &
                hasTopping.some(CrushedPistachios | Chocolate) &
                hasOriginCountry.value(Italy)
        )


    class HazelnutLatte(NamedCoffee):
        equivalent_to = (
                NamedCoffee &
                hasBase.some(Water | ArabicaBean | RobustaBean | HazelnutSyrup) &
                hasMilk.some(WholeMilk | AlmondMilk | OatMilk | LactoseFreeMilk) &
                hasTopping.some(CrushedHazelnuts | Chocolate | Caramel) &
                hasOriginCountry.value(Italy)
        )


    class TurkishCoffee(NamedCoffee):
        equivalent_to = (
                NamedCoffee &
                hasBase.some(Water | ArabicaBean | RobustaBean | Sugar) &
                hasTopping.some(Cardamom | Chocolate) &
                hasOriginCountry.value(Turkey)
        )


    class MacadamiaNutCoffee(NamedCoffee):
        equivalent_to = (
                NamedCoffee &
                hasBase.some(Water | ArabicaBean | RobustaBean | MacadamiaNutSyrup) &
                hasTopping.some(CrushedMacadamiaNuts | Chocolate | Caramel) &
                hasOriginCountry.value(Hawaii)
        )


    class LowCaffeineCoffee(Coffee):
        equivalent_to = (
                Coffee &
                hasCaffeineContentValue.some(lambda x: x < 30)
        )


    class MediumCaffeineCoffee(Coffee):
        equivalent_to = (
                Coffee &
                hasCaffeineContentValue.some(lambda x: x >= 30) &
                hasCaffeineContentValue.some(lambda x: x < 80)
        )


    class HighCaffeineCoffee(Coffee):
        equivalent_to = (
                Coffee &
                hasCaffeineContentValue.some(lambda x: x >= 80)
        )


    class PopularCoffee(Coffee):
        equivalent_to = (
                Coffee &
                hasTopping.some(Cookie | NutTopping) &
                isKnownWorldwide.value(True)
        )


    class ProteinCoffee(Coffee):
        equivalent_to = (
                Coffee &
                hasTopping.some(ProteinBar | ProteinPowder) &
                isProteinRich.value(True)
        )


    class IceCreamCoffee(Coffee):
        equivalent_to = (
                Coffee &
                hasTopping.some(IceCream) &
                hasCalorificContentValue.some(lambda x: x >= 200)
        )


    class CoconutCoffee(Coffee):
        equivalent_to = (
                Coffee &
                hasTopping.some(Coconut) &
                isServedCold.value(True)
        )

# Define some coffe individuals
HotLatte = Latte(name="HotLatte")
HotLatte.isServedCold.append(False)

IceProteinCappuccino = Cappuccino(name="IceProteinCappuccino")
IceProteinCappuccino.isProteinRich.append(True)
IceProteinCappuccino.isServedCold.append(True)

ProteinCappuccino = Cappuccino(name="ProteinCappuccino")
ProteinCappuccino.isProteinRich.append(True)

IceMocha = Mocha(name="IceMocha")
IceMocha.isServedCold.append(True)

CalorificMacchiato = Macchiato(name="CalorificMacchiato")
CalorificMacchiato.hasCalorificContentValue.append(100)

HotLatte = Latte(name="HotLatte")
HotLatte.isServedCold.append(False)

IceProteinCappuccino = Cappuccino(name="IceProteinCappuccino")
IceProteinCappuccino.isProteinRich.append(True)
IceProteinCappuccino.isServedCold.append(True)

ProteinCappuccino = Cappuccino(name="ProteinCappuccino")
ProteinCappuccino.isProteinRich.append(True)

IceMocha = Mocha(name="IceMocha")
IceMocha.isServedCold.append(True)

CalorificMacchiato = Macchiato(name="CalorificMacchiato")
CalorificMacchiato.hasCalorificContentValue.append(100)

StrongLatte = Latte(name="StrongLatte")
StrongLatte.hasCaffeineContentValue.append(90)

StrongMacadamiaNutCoffee = MacadamiaNutCoffee(name="StrongMacadamiaNutCoffee")
StrongMacadamiaNutCoffee.hasCaffeineContentValue.append(85)

LightEspresso = Espresso(name="LightEspresso")
LightEspresso.hasCaffeineContentValue.append(20)

WakeUpCoffee = Espresso(name="WakeUpCoffee")
WakeUpCoffee.hasCaffeineContentValue.append(95)
WakeUpCoffee.isKnownWorldwide.append(True)

StrongIcePistachioLatte = PistachioLatte(name="StrongIcePistachioLatte")
StrongIcePistachioLatte.hasCaffeineContentValue.append(87)
StrongIcePistachioLatte.isServedCold.append(True)
StrongIcePistachioLatte.isKnownWorldwide.append(True)

# Save the ontology
onto.save(file="coffee_ontology.owl")
print("Ontology updated and saved as coffee_ontology.owl")

# Load the ontology
# onto = owlready2.get_ontology("coffee_ontology.owl").load()

# query 1
# cold_coffees = onto.search(Coffee, isServedCold=True)
# for coffee in cold_coffees:
#     print(coffee.name)

# query 2
# all_coffees = onto.search(type=onto.Coffee)
# high_caffeine_coffees = [coffee for coffee in all_coffees if coffee.hasCaffeineContentValue and
#                          coffee.hasCaffeineContentValue[0] > 80]
#
# for coffee in high_caffeine_coffees:
#     print(coffee.name)

# query 3
# popular_coffees = [coffee for coffee in all_coffees if coffee.isKnownWorldwide and coffee.isKnownWorldwide[0] is True]
# for coffee in popular_coffees:
#     print(coffee.name)
