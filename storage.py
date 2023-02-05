# file system ,storing ,searching
from csv import writer, reader, DictWriter, DictReader
# with open('test.csv') as file:
#    csv_reader = reader(file, delimiter='\t')
#   data = list(csv_reader)
#    for row in data:
#       print(row)

''' with open('test.csv', 'w') as f:
            csv_writer = writer(f, lineterminator='/n')
            header = ['code', 'name', 'credit', 'pre_requizite']
            data = [
                ['MA101', 'bd studies', 3, 'mat101 mAat103']
                ['MA102', 'math', 3, 'mat101 mAat103']
                ['MA103', 'English', 3, 'mat101 mAat103']
            ]'''


# with dic writer

with open('test2.csv', 'w') as file:
    header = ('f', 'l', 'a')
    csv_writer = DictWriter(file, fieldnames=header, lineterminator='\n')

    # data = (('bangal', 'vai', 23)
    #        ('pagla', 'vai', 24)
    #        ('kaissa', 'vai', 29)
    #        )
    csv_writer.writeheader()
    csv_writer.writerow(
        {
            'f': 'bangla',
            'l': 'vai',
            'a': 23

        }
    )
