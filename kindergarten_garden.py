class Garden:
    def __init__(self, diagram, students = None):
        self.diagram = diagram.splitlines()
        self.students = students if students is not None else ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
        self.plant_name = {
            'V':'Violets',
            'R':'Radishes',
            'C':'Clover',
            'G':'Grass'
        }
    def plants(self, student):
        index = self.students.index(student)
        codes = [
            self.diagram[0][2 * index: 2 * index + 2],
            self.diagram[1][2 * index: 2 * index + 2]
        ]

        return [self.plant_name[code] for row in codes for code in row]
    

garden1 = Garden("VVCCGG\nVVCCGG")
print(garden1.plants('Alice'))
garden2 = Garden("VRCC\nVCGG", students=["Valorie", "Raven"])
print(garden2.plants('Valorie'))
garden3 =  garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
print(garden3.plants('Charlie'))
garden4 = Garden("VVCG\nVVRC")
print(garden4.plants('Bob'))
garden5 = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
print(garden5.plants('David'))