from owlready2 import *

# Load the ontology
ontology_path = "timetable.owl"
onto = get_ontology(ontology_path).load()

# Print all classes in the ontology
print("Classes in the ontology:")
for cls in onto.classes():
    print(cls)

# List all object properties in the ontology
print("\nObject Properties in the ontology:")
for prop in onto.object_properties():
    print(prop)

# Access a specific class and its relationships
multiplication_facts = onto.search_one(iri="*MultiplicationFacts")
print("\nDetails of MultiplicationFacts class:")
if multiplication_facts:
    print(f"Label: {multiplication_facts.label}")
    print(f"Subclasses: {[sub.name for sub in multiplication_facts.subclasses()]}")
# Add a new class
with onto:
    class DivisionFacts(Thing):
        pass

# Add a subclass relationship
DivisionFacts.is_a.append(onto.MultiplicationFacts)

# Save the updated ontology
onto.save(file="updated_interactive_times_table_tutor.owl")
print("\nNew class added and ontology saved!")

# Add an individual of a class
with onto:
    fact = onto.MultiplicationFacts("Fact_6x7")
    fact.label = ["6 x 7 = 42"]

print("\nNew individual added:")
print(f"Individual: {fact}, Label: {fact.label}")
# List all individuals of a specific class
print("\nIndividuals of MultiplicationFacts:")
for individual in multiplication_facts.instances():
    print(individual.name)
